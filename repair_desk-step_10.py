# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: RepairDesk
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "requests": requests_list,
        "devices": devices_dict,
        "diagnostics": diagnostics_dict,
        "parts": parts_list,
        "costs": costs_list
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
