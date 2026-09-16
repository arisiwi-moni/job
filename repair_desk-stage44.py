# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: RepairDesk
def backup_data(filename="repair_data.json", backup_dir="./backups"):
    import os, shutil
    os.makedirs(backup_dir, exist_ok=True)
    now = datetime.now()
    ts = now.strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"repair_data_{ts}.json")
    shutil.copy2(filename, backup_path)
    return backup_path
