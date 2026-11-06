# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: RepairDesk
import datetime

def log_change(table, record_id, field, old_value, new_value):
    change = {
        "table": table,
        "record_id": record_id,
        "field": field,
        "old_value": old_value,
        "new_value": new_value,
        "timestamp": datetime.datetime.now().isoformat()
    }
    with open("repairdesk_changes.json", "a", encoding="utf-8") as f:
        f.write("\n" + json.dumps(change, ensure_ascii=False))

def get_changes(table=None, days=7):
    changes = []
    cutoff = (datetime.datetime.now() - datetime.timedelta(days=days)).isoformat()
    with open("repairdesk_changes.json", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            change = json.loads(line)
            if table is None or change.get("table") == table:
                changes.append(change)
    return changes

def show_recent_changes(table=None, days=7):
    print("=== Журнал изменений ===")
    for change in get_changes(table, days):
        print(f"[{change['timestamp']}] {change['table']} #{change['record_id']} "
              f"{change['field']}: {change['old_value']} -> {change['new_value']}")
