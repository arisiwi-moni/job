# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: RepairDesk
import json, uuid
from datetime import date

class RepairDesk:
    def __init__(self):
        self.requests = []
        self.devices = {}
        self.parts = {}
    
    def add_demo_data(self):
        # Демо-запрос
        req_id = str(uuid.uuid4())[:8]
        new_req = {
            "id": req_id,
            "device_type": "Smartphone",
            "model": "Galaxy S21",
            "issue": "Не работает камера",
            "status": "new",
            "created_at": date.today().isoformat()
        }
        self.requests.append(new_req)
        
        # Демо-устройство (связь с запросом по типу и модели для простоты демо)
        dev_id = f"DEV-{req_id}"
        self.devices[dev_id] = {
            "type": new_req["device_type"],
            "model": new_req["model"],
            "serial": "SN123456",
            "status": "in_repair"
        }
        
        # Демо-запчасть
        part_id = f"P-{req_id}"
        self.parts[part_id] = {
            "name": "Камера модуль",
            "price": 2500.0,
            "stock": 10
        }

if __name__ == "__main__":
    app = RepairDesk()
    app.add_demo_data()
    print(f"Демо-данные добавлены: {len(app.requests)} заявок.")
