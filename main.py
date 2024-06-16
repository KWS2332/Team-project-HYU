import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from openpyxl import Workbook
from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout, QFormLayout,
                             QLineEdit, QPushButton, QComboBox, QMessageBox,
                             QTableWidget, QTableWidgetItem)

matplotlib.use('Qt5Agg')  # Matplotlib 백엔드를 Qt5Agg로 설정

class BridgeElement:
    def __init__(self, bridge_length_m, support_points_count, material_elasticity_kg_per_mm2, fixed_load_kN,
                 live_load_kN, unit_weight_kg, member_section):
        self.material_type = "철"  # 재료 종류 고정
        self.bridge_length_m = bridge_length_m  # 교량 길이 (m)
        self.support_points_count = support_points_count  # 절점 갯수 (개)
        self.material_elasticity_kg_per_mm2 = material_elasticity_kg_per_mm2  # 재료 탄성 계수 (kg/mm^2)
        self.fixed_load_kN = fixed_load_kN  # 고정 하중 (kN)
        self.live_load_kN = live_load_kN  # 활 하중 (kN)
        self.unit_weight_kg = unit_weight_kg  # 재료의 단위 중량 (kg/m^3)
        self.member_section = member_section  # 부재 단면 (H빔 또는 I빔)

class TrussApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('트러스 구조 설계 프로그램')

        layout = QVBoxLayout()

        form_layout = QFormLayout()

        # 재료 종류 고정
        self.material_input = QLineEdit("철")
        self.material_input.setReadOnly(True)

        # 기타 입력 변수들
        self.length_input = QLineEdit()
        self.nodes_input = QLineEdit()
        self.elastic_modulus_input = QLineEdit()
        self.dead_load_input = QLineEdit()
        self.live_load_input = QLineEdit()
        self.unit_weight_input = QLineEdit()

        # 부재 단면 선택
        self.cross_section_input = QComboBox()
        self.cross_section_input.addItems(["H빔", "I빔"])

        form_layout.addRow('재료 종류:', self.material_input)
        form_layout.addRow('교량 길이 (m):', self.length_input)
        form_layout.addRow('절점 갯수:', self.nodes_input)
        form_layout.addRow('재료 탄성 계수 (kg/mm^2):', self.elastic_modulus_input)
        form_layout.addRow('고정 하중 (kN):', self.dead_load_input)
        form_layout.addRow('활 하중 (kN):', self.live_load_input)
        form_layout.addRow('재료의 단위 중량 (kg/m^3):', self.unit_weight_input)
        form_layout.addRow('부재 단면:', self.cross_section_input)

        self.submit_btn = QPushButton('제출')
        self.submit_btn.clicked.connect(self.submit)

        layout.addLayout(form_layout)
        layout.addWidget(self.submit_btn)

        # 테이블 위젯 추가
        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.setLayout(layout)

        # 도면을 표시할 FigureCanvas 추가
        self.figure, self.ax = plt.subplots(figsize=(10, 5))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

    def submit(self):
        try:
            length = float(self.length_input.text())
            num_nodes = int(self.nodes_input.text())
            elastic_modulus = float(self.elastic_modulus_input.text())
            dead_load = float(self.dead_load_input.text())
            live_load = float(self.live_load_input.text())
            unit_weight = float(self.unit_weight_input.text())
            cross_section = self.cross_section_input.currentText()

            bridge_element = BridgeElement(
                bridge_length_m=length,
                support_points_count=num_nodes,
                material_elasticity_kg_per_mm2=elastic_modulus,
                fixed_load_kN=dead_load,
                live_load_kN=live_load,
                unit_weight_kg=unit_weight,
                member_section=cross_section
            )

            truss_data, member_forces = self.calculate_truss(bridge_element)  # 이 부분 수정

            is_safe, failed_members, unstable_parameters = self.check_stability(member_forces, bridge_element)
            self.create_excel_file(truss_data, member_forces)
            self.plot_truss(truss_data, member_forces, is_safe)
            self.show_table(truss_data, is_safe, failed_members, unstable_parameters, member_forces)  # 이 부분 수정

            if is_safe:
                QMessageBox.information(self, '결과', '교량이 안전합니다.')
            else:
                QMessageBox.warning(self, '결과',
                                    f'교량이 안전하지 않습니다. 실패한 부재: {failed_members}, 불안정한 매개 변수: {unstable_parameters}')

        except Exception as e:
            QMessageBox.critical(self, '오류 발생', f'오류가 발생했습니다: {str(e)}')


    def show_table(self, truss_data, is_safe, failed_members, unstable_parameters, member_forces):
        self.table.setRowCount(len(truss_data))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["부재", "길이 (m)", "탄성 계수 (kg/mm^2)", "하중 (kN)", "평가 결과"])

        for row, data in enumerate(truss_data):
            member, length, _, elastic_modulus, _, _, _, _ = data
            force = sum(member_force[1] for member_force in member_forces if member_force[0] == member)
            item_member = QTableWidgetItem(f"{member}")
            item_length = QTableWidgetItem(f"{length:.2f}")
            item_elastic_modulus = QTableWidgetItem(f"{elastic_modulus:.2f}")
            item_force = QTableWidgetItem(f"{force:.2f}")
            item_evaluation = QTableWidgetItem("안전" if abs(force) <= 250 else "불안전")
            self.table.setItem(row, 0, item_member)
            self.table.setItem(row, 1, item_length)
            self.table.setItem(row, 2, item_elastic_modulus)
            self.table.setItem(row, 3, item_force)
            self.table.setItem(row, 4, item_evaluation)

        # 안전하지 않은 부재 및 불안정한 매개 변수 표시
        if not is_safe:
            failed_members_str = ", ".join([f"{member} ({force:.2f} kN)" for member, force in failed_members])
            unstable_parameters_str = ", ".join(unstable_parameters)
            QMessageBox.warning(self, '결과', f'안전하지 않은 부재: {failed_members_str}\n불안정한 매개 변수: {unstable_parameters_str}')

        self.table.resizeColumnsToContents()
    def calculate_truss(self, bridge_element):
        length = bridge_element.bridge_length_m
        num_nodes = bridge_element.support_points_count
        elastic_modulus = bridge_element.material_elasticity_kg_per_mm2
        dead_load = bridge_element.fixed_load_kN
        live_load = bridge_element.live_load_kN
        unit_weight = bridge_element.unit_weight_kg
        cross_section = bridge_element.member_section

        panel_length = length / (num_nodes - 1)
        nodes = []

        for i in range(num_nodes):
            x = i * panel_length
            y = 0 if i % 2 == 0 else panel_length
            nodes.append((x, y))

        members = []
        for i in range(num_nodes - 1):
            members.append((nodes[i], nodes[i + 1]))
            if i < num_nodes - 2:
                members.append((nodes[i], nodes[i + 2]))

        truss_data = []
        for member in members:
            x1, y1 = member[0]
            x2, y2 = member[1]
            length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            angle = np.degrees(np.arctan2((y2 - y1), (x2 - x1)))
            truss_data.append([member, length, angle, elastic_modulus, dead_load, live_load, unit_weight, cross_section])

        member_forces = self.analyze_forces(truss_data)

        return truss_data, member_forces

    def analyze_forces(self, truss_data):
        member_forces = []
        for data in truss_data:
            member, length, angle, elastic_modulus, dead_load, live_load, unit_weight, cross_section = data
            force = (dead_load + live_load) * length * 9.81 * unit_weight * 1e-3  # force 변환
            member_forces.append([member, force])
        return member_forces

    def check_stability(self, member_forces, bridge_element):
        max_allowable_force = 250  # 허용 가능한 최대 하중
        failed_members = []
        unstable_parameters = []

        for member, force in member_forces:
            if abs(force) > max_allowable_force:
                failed_members.append((member, force))
                # 안전하지 않은 부재의 길이를 기준으로 안정성을 향상시킬 수 있는 변수를 찾음
                length = np.sqrt((member[1][0] - member[0][0]) ** 2 + (member[1][1] - member[0][1]) ** 2)
                if length > bridge_element.bridge_length_m / 2:
                    unstable_parameters.append("교량 길이를 늘리십시오.")
                else:
                    unstable_parameters.append("부재 단면적을 증가시키십시오.")

        return len(failed_members) == 0, failed_members, unstable_parameters

    def create_excel_file(self, truss_data, member_forces):
        wb = Workbook()
        ws = wb.active
        ws.title = "Truss Data"

        ws.append(["부재", "길이 (m)", "각도 (도)", "탄성 계수 (kg/mm^2)", "고정 하중 (kN)", "활 하중 (kN)", "단위 중량 (kg/m^3)", "부재 단면",
                   "부재력 (kN)"])
        for data, force_data in zip(truss_data, member_forces):
            member, length, angle, elastic_modulus, dead_load, live_load, unit_weight, cross_section = data
            force = force_data[1]
            ws.append(
                [f"{member}", length, angle, elastic_modulus, dead_load, live_load, unit_weight, cross_section, force])

        filename = "truss_structure.xlsx"
        wb.save(filename)
        return filename

    def plot_truss(self, truss_data, member_forces, is_safe):
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)

        for data, force_data in zip(truss_data, member_forces):
            member, length, angle, elastic_modulus, dead_load, live_load, unit_weight, cross_section = data
            (x1, y1), (x2, y2) = member
            color = "green" if is_safe else "red"
            self.ax.plot([x1, x2], [y1, y2], color=color, linewidth=2)
            self.ax.text((x1 + x2) / 2, (y1 + y2) / 2, f"{force_data[1]:.2f} kN", color="blue", fontsize=8, ha='center')

        self.ax.axis('off')
        self.ax.set_aspect('equal', adjustable='box')
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TrussApp()
    ex.show()
    sys.exit(app.exec_())
