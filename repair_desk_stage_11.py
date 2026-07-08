# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: RepairDesk
import json, os

DATA_FILE = "repair_desk_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"devices": [], "tickets": [], "diagnostics": {}, "parts": {}}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
