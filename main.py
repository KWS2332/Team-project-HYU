class BridgeElement:
    def __init__(self, material_type, bridge_length_m, support_points_count, material_elasticity_kg_per_mm2, fixed_load_kN, live_load_kN, unit_weight_kg):
        self.material_type = material_type  # 재료 종류
        self.bridge_length_m = bridge_length_m  # 교량 길이 (m)
        self.support_points_count = support_points_count  # 절점 갯수 (개)
        self.material_elasticity_kg_per_mm2 = material_elasticity_kg_per_mm2  # 재료 탄성 계수 (kg/mm^2)
        self.fixed_load_kN = fixed_load_kN  # 고정 하중 (kN)
        self.live_load_kN = live_load_kN  # 활 하중 (kN)
        self.unit_weight_kg = unit_weight_kg  # 재료의 단위 중량 (kg)
        self.member_section = member_section  # 부재 단면

bridge = BridgeElement("steel", 100.0, 5, 200000.0, 50000.0, 200.0, 25.0, "I-beam")

