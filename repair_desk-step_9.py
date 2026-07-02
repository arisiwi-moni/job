# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: RepairDesk
import json, sys

def load_initial_data(json_string: str) -> dict:
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        # Валидация структуры данных
        required_keys = ["devices", "diagnostics", "parts"]
        for key in required_keys:
            if key not in data:
                raise KeyError(f"Отсутствует ключ {key}")

        # Преобразование списков в словари для быстрого поиска по ID
        devices_map = {d["id"]: d for d in data.get("devices", [])}
        diagnostics_map = {d["id"]: d for d in data.get("diagnostics", [])}
        parts_map = {p["id"]: p for p in data.get("parts", [])}

        # Проверка целостности связей (опционально, можно отключить)
        # Для начальных данных часто связи могут быть неполными, поэтому проверка мягкая
        
        return {
            "devices": devices_map,
            "diagnostics": diagnostics_map,
            "parts": parts_map,
            "metadata": data.get("metadata", {})
        }

    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyError as e:
        print(f"Ошибка структуры данных: {e}", file=sys.stderr)
        sys.exit(1)

# Пример использования (раскомментируйте для теста):
if __name__ == "__main__":
    initial_json = '''
    {
        "devices": [
            {"id": 1, "model": "iPhone 13", "serial": "A123456789"},
            {"id": 2, "model": "Samsung S22", "serial": "B987654321"}
        ],
        "diagnostics": [
            {"id": 101, "device_id": 1, "issue": "Разбит экран"},
            {"id": 102, "device_id": 2, "issue": "Не включается"}
        ],
        "parts": [
            {"id": 501, "name": "Экран", "price": 3000},
            {"id": 502, "name": "Батарея", "price": 1500}
        ]
    }
    '''
    
    loaded_data = load_initial_data(initial_json)
    print(f"Загружено устройств: {len(loaded_data['devices'])}")
    print(f"Диагностика: {list(d.keys()) for d in loaded_data['diagnostics'].values()}")
