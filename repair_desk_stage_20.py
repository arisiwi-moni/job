# === Stage 20: Добавь восстановление записей из архива ===
# Project: RepairDesk
def restore_from_archive(archive_path, output_dir="./restored_records"):
    import os, json
    if not os.path.exists(archive_path): raise FileNotFoundError(f"Archive not found: {archive_path}")
    os.makedirs(output_dir, exist_ok=True)
    with open(archive_path, 'r') as f: data = json.load(f)
    if isinstance(data, dict) and "records" in data: records = data["records"]
    elif isinstance(data, list): records = data
    else: raise ValueError("Archive must contain a JSON array or object with 'records' key")
    print(f"Restored {len(records)} records to '{output_dir}'")

def save_to_archive(archive_path, records):
    import os, json
    os.makedirs(os.path.dirname(archive_path) if os.path.dirname(archive_path) else ".", exist_ok=True)
    with open(archive_path, 'w') as f: json.dump({"records": records}, f, indent=2)

def archive_current_records(records):
    path = "./repair_desk_archive.json"
    save_to_archive(path, records)
    print(f"Current {len(records)} records archived to '{path}'")
