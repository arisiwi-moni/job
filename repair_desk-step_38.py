# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: RepairDesk
def test_edge_cases():
    assert RepairDesk().get_applications() == []
    assert RepairDesk().get_applications("nonexist") == []
    assert RepairDesk().get_applications(42) == []
    assert RepairDesk().get_applications(0.5) == []

    desk = RepairDesk()
    desk.add_device("phone", "iPhone 15", "SM-1", "2024-01-01")
    desk.add_device("laptop", "MacBook Pro", "SM-2", "2024-02-01")
    desk.add_device("phone", "iPhone 15", "SM-1", "2024-01-01")  # duplicate
    assert len(desk.get_devices()) == 2

    desk.add_application("app1", "phone", "SM-1", "2024-03-01")
    desk.add_application("app2", "laptop", "SM-2", "2024-03-01")
    desk.add_application("app3", "phone", "SM-1", "2024-03-01")  # duplicate
    assert len(desk.get_applications()) == 2

    assert desk.get_application("nonexist") is None
    assert desk.get_application(42) is None

    desk.add_diagnosis("app1", "broken", "screen cracked")
    desk.add_diagnosis("app1", "broken", "broken screen")  # duplicate
    assert len(desk.get_diagnoses("app1")) == 1

    desk.add_part("app1", "screen", 500, "2024-03-15")
    desk.add_part("app1", "screen", 500, "2024-03-15")  # duplicate
    assert len(desk.get_parts("app1")) == 1

    assert desk.calculate_total_cost("app1") == 500
    assert desk.calculate_total_cost("app2") == 0

    desk.add_cost("app1", 700)
    assert desk.calculate_total_cost("app1") == 1200

    assert desk.calculate_total_cost("nonexist") == 0
    assert desk.calculate_total_cost(42) == 0
    assert desk.calculate_total_cost("app1", "nonexist") == 0

    assert desk.get_statistics() == {
        "devices": {"phone": 1, "laptop": 1},
        "applications": {"phone": 1, "laptop": 1},
        "diagnoses": {"broken": 1},
        "parts": {"screen": 1},
        "costs": {"app1": 1200},
    }
