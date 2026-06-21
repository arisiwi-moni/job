# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: RepairDesk
class RepairData:
    def __init__(self):
        self.devices = {}
        self.requests = []
        self.parts = {}
    
    def validate_device_name(self, name: str) -> bool:
        return isinstance(name, str) and len(name.strip()) > 0
    
    def validate_serial_number(self, serial: str) -> bool:
        return isinstance(serial, str) and len(serial) >= 6
    
    def add_device(self, name: str, model: str, serial: str):
        if not self.validate_device_name(name) or not self.validate_serial_number(serial):
            raise ValueError("Некорректные данные устройства")
        self.devices[serial] = {"name": name.strip(), "model": model}
    
    def add_request(self, device_serial: str, diagnosis: str, parts_needed: list, cost: float) -> dict | None:
        if not self.validate_device_name(diagnosis):
            raise ValueError("Некорректная диагностика")
        if not isinstance(parts_needed, list) or len(parts_needed) == 0:
            raise ValueError("Список запчастей пуст или некорректен")
        for part in parts_needed:
            if not self.validate_device_name(part):
                raise ValueError(f"Некорректная часть: {part}")
        if cost < 0:
            raise ValueError("Стоимость должна быть положительной")
        
        device = self.devices.get(device_serial)
        if not device:
            return None
        
        request_id = len(self.requests) + 1
        new_request = {
            "id": request_id,
            "device": device["name"],
            "diagnosis": diagnosis.strip(),
            "parts": parts_needed.copy(),
            "cost": cost
        }
        self.requests.append(new_request)
        return new_request
