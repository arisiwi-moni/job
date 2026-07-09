# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: RepairDesk
import json, os

def load_data(filepath):
    if not os.path.exists(filepath):
        return None, "Файл не найден: " + filepath
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            return None, "JSON должен содержать массив записей"
        for i, item in enumerate(data):
            if not isinstance(item, dict):
                return None, "Запись на строке " + str(i+1) + " не является объектом JSON"
        return data, None
    except json.JSONDecodeError as e:
        return None, "Ошибка формата JSON: " + str(e)
    except PermissionError:
        return None, "Нет прав доступа к файлу: " + filepath

print(load_data("repair_desk.json"))
