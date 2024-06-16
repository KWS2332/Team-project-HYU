import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QVBoxLayout, QWidget
from ui_Test1 import Ui_MainWindow
from ui_Test2 import Ui_MainWindow2
from ui_Test3 import Ui_MainWindow3

# 재료 및 기하학적 특성
E = 210e9  # Young's modulus (Pa)
density = 7850  # kg/m^3
gravity = 9.81  # m/s^2
material_elasticity_kg_per_mm2 = 345e6  # 항복응력 (N/m^2), 강재의 일반적인 값

class BridgeElement:
    def __init__(self, material_type, bridge_length_m, support_points_count, live_load_kN, member_section):
        self.material_type = material_type
        self.bridge_length_m = bridge_length_m
        self.support_points_count = support_points_count
        self.live_load_kN = live_load_kN
        self.member_section = member_section

# 자중 계산 함수
def calculate_weight(member_section, bridge_length_m):
    unit_weight_kg = density * gravity
    volume = member_section * bridge_length_m / 6  # 예시 그림에서 밑면의 부재 수가 6개였음
    weight = volume * unit_weight_kg
    fixed_load_kN = weight / bridge_length_m
    return weight, fixed_load_kN

# 휨 설계 계산 함수
def calculate_flexural_strength(member_section, bridge_length_m, live_load_kN, fixed_load_kN):
    D = fixed_load_kN * bridge_length_m ** 2 / 8
    L = live_load_kN * bridge_length_m / 4
    Mu = 1.2 * D + 1.6 * L
    return Mu, D, L

# 단면적 모멘트 계산 함수
def calculate_section_modulus(member_section):
    width = (member_section ** 0.5) / 2  # 가정: 플랜지와 웹의 비율에 따른 폭
    height = member_section / width  # 단면적에 따른 높이
    S = (width * height ** 2) / 6  # 대략적인 단면적 모멘트 계산
    return S

# 평가 함수
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
def element_stiffness_matrix(length, angle):
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
def assemble_global_stiffness(nodes, elements):
    n_nodes = nodes.shape[0]
    n_dof = 2 * n_nodes
    K = np.zeros((n_dof, n_dof))

    for element in elements:
        node1 = nodes[element[0]]
        node2 = nodes[element[1]]
        length, angle = element_properties(node1, node2)
        k = element_stiffness_matrix(length, angle)

        dof_indices = np.array([
            2 * element[0], 2 * element[0] + 1,
            2 * element[1], 2 * element[1] + 1
        ])

        for i in range(4):
            for j in range(4):
                K[dof_indices[i], dof_indices[j]] += k[i, j]

    return K

# 응력 계산
def element_stress(node1, node2, u1, u2, length, angle):
    c = np.cos(angle)
    s = np.sin(angle)
    T = np.array([-c, -s, c, s])
    strain = (1 / length) * T @ np.concatenate((u1, u2))
    stress = E * strain
    return stress

# 시각화 함수
def plot_truss(nodes, elements, stresses):
    plt.figure(figsize=(10, 6))
    for element, stress in zip(elements, stresses):
        node1 = nodes[element[0]]
        node2 = nodes[element[1]]
        x_values = [node1[0], node2[0]]
        y_values = [node1[1], node2[1]]
        plt.plot(x_values, y_values, 'b-o')
        plt.text(np.mean(x_values), np.mean(y_values), f'{stress:.2f}', color='red')

    plt.xlabel('')
    plt.ylabel('')
    plt.title('Truss Structure with Stresses')
    plt.grid(False)
    plt.show()

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

# MainWindow2 클래스 예시
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

# MainWindow3 클래스 예시
class MainWindow3(QMainWindow):
    def __init__(self):
        super(MainWindow3, self).__init__()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculate_results)

    def safe_str_to_float(self, value, field_name):
        try:
            float_value = float(value)
            print(f"Successfully converted {field_name} to float: {float_value}")
            return float_value
        except ValueError:
            raise ValueError(f"{field_name}에는 유효한 숫자를 입력해주세요.")
        except Exception as e:
            raise ValueError(f"{field_name}에는 유효한 숫자를 입력해주세요. ({e})")

    def safe_str_to_int(self, value, field_name):
        try:
            int_value = int(value)
            print(f"Successfully converted {field_name} to int: {int_value}")
            return int_value
        except ValueError:
            raise ValueError(f"{field_name}에는 유효한 정수를 입력해주세요.")
        except Exception as e:
            raise ValueError(f"{field_name}에는 유효한 정수를 입력해주세요. ({e})")

    def calculate_results(self):
        try:
            # 입력 값 가져오기
            material_type = self.ui.materialTypeInput.text()
            support_points = int(self.ui.supportPointsInput.text())
            bridge_length = float(self.ui.bridgeLengthInput.text())
            fixed_load = float(self.ui.fixedLoadInput.text())
            live_load = float(self.ui.liveLoadInput.text())
            member_section = self.ui.memberSectionInput.text()

            # 디버깅을 위한 출력
            print(f"Material Type: {material_type}")
            print(f"Bridge Length Input: {bridge_length_input}")
            print(f"Support Points Input: {support_points_input}")
            print(f"Fixed Load Input: {fixed_load_kN_input}")
            print(f"Live Load Input: {live_load_kN_input}")
            print(f"Member Section Input: {member_section_input}")

            # 변환
            bridge_length_m = self.safe_str_to_float(bridge_length_input, "교량 길이")
            support_points_count = self.safe_str_to_int(support_points_input, "절점 갯수")
            live_load_kN = self.safe_str_to_float(live_load_kN_input, "활하중")
            member_section = self.safe_str_to_float(member_section_input, "부재 단면적")
            fixed_load_kN = self.safe_str_to_float(fixed_load_kN_input, "고정하중")

            # 계산
            nodes, elements = create_truss_structure(support_points_count)
            K = assemble_global_stiffness(nodes, elements)
            weight, fixed_load_kN = calculate_weight(member_section, bridge_length_m)
            Mu, D, L = calculate_flexural_strength(member_section, bridge_length_m, live_load_kN, fixed_load_kN)
            S = calculate_section_modulus(member_section)
            Mn = material_elasticity_kg_per_mm2 * S
            safety = evaluate_safety(Mu, Mn)

            # 결과 출력
            self.ui.resultLabel.setText(f"휨 모멘트: {Mu:.2f} kN·m\n단면계수: {S:.2f} mm³\n강도: {Mn:.2f} N·mm\n평가: {safety}")

            stresses = []
            for element in elements:
                node1, node2 = nodes[element[0]], nodes[element[1]]
                u1 = np.zeros(2)  # 실제로는 구조해석을 통해 변위를 계산해야 합니다
                u2 = np.zeros(2)
                length, angle = element_properties(node1, node2)
                stress = element_stress(node1, node2, u1, u2, length, angle)
                stresses.append(stress)

            plot_truss(nodes, elements, stresses)
        except ValueError as e:
            QMessageBox.warning(self, "입력 오류", str(e))
        except Exception as e:
            QMessageBox.warning(self, "오류", f"알 수 없는 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
