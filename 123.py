import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QVBoxLayout, QWidget
from ui_Test1 import Ui_MainWindow
from ui_Test2 import Ui_MainWindow2
from ui_Test3 import Ui_MainWindow3

class BridgeElement:
    def __init__(self, material_type, bridge_length_m, support_points_count, material_elasticity_kg_per_mm2, live_load_kN, member_section, fixed_load_kN, unit_weight_kg):
        self.material_type = material_type
        self.bridge_length_m = bridge_length_m
        self.support_points_count = support_points_count
        self.material_elasticity_kg_per_mm2 = material_elasticity_kg_per_mm2
        self.live_load_kN = live_load_kN
        self.member_section = member_section
        self.fixed_load_kN = fixed_load_kN
        self.unit_weight_kg = unit_weight_kg

# 자중 계산 함수
density = 7850  # kg/m^3
gravity = 9.81  # m/s^2

def calculate_weight(member_section, bridge_length_m):
    unit_weight_kg = density * gravity
    volume = member_section * bridge_length_m / 6  # 예시 그림에서 밑면의 부재 수가 6개였음
    weight = volume * unit_weight_kg
    fixed_load_kN = weight / bridge_length_m
    return weight, fixed_load_kN

# 휨 설계 계산 함수
material_elasticity_kg_per_mm2 = 345e6  # 항복응력 (N/m^2), 강재의 일반적인 값

def calculate_section_modulus(member_section):
    width = (member_section ** 0.5) / 2  # 가정: 플랜지와 웹의 비율에 따른 폭
    height = member_section / width  # 단면적에 따른 높이
    S = (width * height ** 2) / 6  # 대략적인 단면적 모멘트 계산
    return S

def calculate_flexural_strength(member_section, bridge_length_m, live_load_kN, fixed_load_kN):
    D = fixed_load_kN * bridge_length_m ** 2 / 8
    L = live_load_kN * bridge_length_m / 4
    Mu = 1.2 * D + 1.6 * L
    return Mu, D, L

def evaluate_safety(Mu, Mn):
    return "안전합니다" if Mu <= Mn else "안전하지 않습니다"

# 트러스 구조 생성 함수
def create_truss_structure(n):
    nodes = []
    elements = []

    for i in range(n):
        nodes.append([i, 0])
        nodes.append([i, 1])

    for i in range(n):
        if i < n - 1:
            elements.append([2 * i, 2 * (i + 1)])  # 아래 가로선
            elements.append([2 * i + 1, 2 * (i + 1) + 1])  # 위 가로선
            elements.append([2 * i, 2 * (i + 1) + 1])  # 대각선 (아래에서 위로)
            elements.append([2 * i + 1, 2 * (i + 1)])  # 대각선 (위에서 아래로)

    for i in range(n):
        elements.append([2 * i, 2 * i + 1])  # 세로선

    nodes = np.array(nodes)
    elements = np.array(elements)
    return nodes, elements

# 요소의 길이와 각도 계산
def element_properties(node1, node2):
    length = np.linalg.norm(node2 - node1)
    angle = np.arctan2(node2[1] - node1[1], node2[0] - node1[0])
    return length, angle

# 요소 강성 행렬 계산
def element_stiffness_matrix(length, angle, E, A):
    c = np.cos(angle)
    s = np.sin(angle)
    k = (E * A / length) * np.array([
        [c * c, c * s, -c * c, -c * s],
        [c * s, s * s, -c * s, -s * s],
        [-c * c, -c * s, c * c, c * s],
        [-c * s, -s * s, c * s, s * s]
    ])
    return k

# 전체 강성 행렬 조립
def assemble_global_stiffness(nodes, elements, E, A):
    n_nodes = nodes.shape[0]
    n_dof = 2 * n_nodes
    K = np.zeros((n_dof, n_dof))

    for element in elements:
        node1 = nodes[element[0]]
        node2 = nodes[element[1]]
        length, angle = element_properties(node1, node2)
        k = element_stiffness_matrix(length, angle, E, A)

        dof_indices = np.array([
            2 * element[0], 2 * element[0] + 1,
            2 * element[1], 2 * element[1] + 1
        ])

        for i in range(4):
            for j in range(4):
                K[dof_indices[i], dof_indices[j]] += k[i, j]

    return K

# 응력 계산
def element_stress(node1, node2, u1, u2, length, angle, E):
    c = np.cos(angle)
    s = np.sin(angle)
    T = np.array([-c, -s, c, s])
    strain = (1 / length) * T @ np.concatenate((u1, u2))
    stress = E * strain
    return stress
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        self.hide()
        self.window2 = MainWindow2()
        self.window2.show()

class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui2 = Ui_MainWindow2()
        self.ui2.setupUi(self)
        self.ui2.pushButton.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        self.hide()
        self.window3 = MainWindow3()
        self.window3.show()

class MainWindow3(QMainWindow):
    def __init__(self):
        super(MainWindow3, self).__init__()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        try:
            # Retrieve input values
            material_type = self.ui.materialTypeInput.text()
            bridge_length_m_input = self.ui.bridgeLengthInput.text()
            support_points_count_input = self.ui.supportPointsInput.text()
            fixed_load_kN_input = self.ui.fixedLoadInput.text()
            live_load_kN_input = self.ui.liveLoadInput.text()
            member_section_input = self.ui.memberSectionInput.text()

            # Debug: Print input values
            print(f"material_type: {material_type}")
            print(f"bridge_length_m_input: {bridge_length_m_input}")
            print(f"support_points_count_input: {support_points_count_input}")
            print(f"fixed_load_kN_input: {fixed_load_kN_input}")
            print(f"live_load_kN_input: {live_load_kN_input}")
            print(f"member_section_input: {member_section_input}")

            # Validate and convert inputs
            bridge_length_m = self.validate_float_input(bridge_length_m_input, "교량 길이")
            support_points_count = self.validate_int_input(support_points_count_input, "지지점 수")
            fixed_load_kN = self.validate_float_input(fixed_load_kN_input, "고정 하중")
            live_load_kN = self.validate_float_input(live_load_kN_input, "설계 하중")
            member_section = self.validate_float_input(member_section_input, "단면적")

            bridge_params = {
                'material_type': material_type,
                'bridge_length_m': bridge_length_m,
                'support_points_count': support_points_count,
                'live_load_kN': live_load_kN,
                'member_section': member_section
            }

            # 자중 계산
            self_weight, fixed_load_kN = calculate_weight(member_section, bridge_length_m)

            # 휨 설계 계산
            Mu, D, L = calculate_flexural_strength(member_section, bridge_length_m, live_load_kN, fixed_load_kN)
            S = calculate_section_modulus(member_section)
            Mn = material_elasticity_kg_per_mm2 * S
            safety_status = evaluate_safety(Mu, Mn)

        except ValueError as ve:
            QMessageBox.critical(self, "입력 오류", str(ve))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def validate_float_input(self, input_value, input_name):
        try:
            return float(input_value)
        except ValueError:
            raise ValueError(f"{input_name} 입력 값이 잘못되었습니다: {input_value}")

    def validate_int_input(self, input_value, input_name):
        try:
            return int(input_value)
        except ValueError:
            raise ValueError(f"{input_name} 입력 값이 잘못되었습니다: {input_value}")

# Ensure the ResultsWindow class remains the same as you provided:
class ResultsWindow(QWidget):
    def __init__(self, bridge_params, self_weight, fixed_load_kN, Mu, D, L, S, Mn, safety_status):
        super().__init__()
        self.setWindowTitle("Results")
        layout = QVBoxLayout()

        results_label = QLabel(
            f"Material Type: {bridge_params['material_type']}\n"
            f"Bridge Length: {bridge_params['bridge_length_m']:.2f} m\n"
            f"Support Points Count: {bridge_params['support_points_count']}\n"
            f"Live Load: {bridge_params['live_load_kN']:.2f} kN\n"
            f"Member Section: {bridge_params['member_section']:.2f} mm^2\n\n"
            f"Self Weight: {self_weight:.2f} kg\n"
            f"Fixed Load: {fixed_load_kN:.2f} kN\n"
            f"Mu: {Mu:.2f} kNm\n"
            f"D: {D:.2f} kNm\n"
            f"L: {L:.2f} kNm\n"
            f"S: {S:.2f} mm^3\n"
            f"Mn: {Mn:.2f} kNm\n"
            f"Safety Status: {safety_status}"
        )

        layout.addWidget(results_label)
        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
