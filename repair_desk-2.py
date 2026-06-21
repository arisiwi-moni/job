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

# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: RepairDesk
class RepairData:
    def __init__(self):
        self.devices = {}
        self.diagnostics = []
        self.parts = {}
    
    def validate_device_name(self, name):
        if not isinstance(name, str) or len(name.strip()) < 2:
            raise ValueError("Имя устройства должно быть строкой длиной не менее 2 символов.")
        return name.strip()
    
    def add_device(self, name, model, serial_number):
        validated_name = self.validate_device_name(name)
        if not isinstance(model, str) or len(model) < 3:
            raise ValueError("Модель устройства должна быть строкой длиной не менее 3 символов.")
        if not isinstance(serial_number, str) or len(serial_number) > 20:
            raise ValueError("Серийный номер должен быть строкой длиной до 20 символов.")
        
        self.devices[validated_name] = {
            "model": model,
            "serial_number": serial_number,
            "status": "active"
        }
    
    def add_diagnostic(self, device_name: str, issue_type: str, description: str):
        if not isinstance(issue_type, str) or len(issue_type) < 2:
            raise ValueError("Тип проблемы должен быть строкой длиной не менее 2 символов.")
        
        if device_name not in self.devices:
            raise KeyError(f"Устройство '{device_name}' не найдено в системе.")
        
        self.diagnostics.append({
            "device": device_name,
            "issue_type": issue_type,
            "description": description,
            "timestamp": datetime.now().isoformat()
        })
    
    def add_part(self, part_name: str, price: float):
        if not isinstance(part_name, str) or len(part_name.strip()) < 2:
            raise ValueError("Название запчасти должно быть строкой длиной не менее 2 символов.")
        
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Цена запчасти должна быть положительным числом.")
        
        self.parts[part_name.strip()] = {
            "price": float(price),
            "stock_count": 100
        }

import datetime
