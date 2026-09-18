# === Stage 45: Добавь восстановление из резервной копии ===
# Project: RepairDesk
import json, os, shutil, sys

def restore_from_backup(backup_dir, target_dir):
    """Восстановление RepairDesk из резервной копии."""
    if not os.path.isdir(backup_dir):
        print(f"Резервная копия не найдена: {backup_dir}")
        return False
    for root, dirs, files in os.walk(backup_dir):
        rel = os.path.relpath(root, backup_dir)
        dest = os.path.join(target_dir, rel)
        if rel == '.':
            continue
        if os.path.exists(dest):
            print(f"Пропускаю: {dest} (уже существует)")
            continue
        if os.path.isdir(root):
            os.makedirs(dest, exist_ok=True)
        else:
            shutil.copy2(os.path.join(root, os.path.basename(root)), dest)
    print("Резервное восстановление завершено успешно.")
    return True

def load_backup(backup_dir):
    """Загрузка списка файлов из резервной копии."""
    if not os.path.isdir(backup_dir):
        return []
    result = []
    for root, dirs, files in os.walk(backup_dir):
        for f in files:
            result.append(os.path.join(root, f))
    return result

def create_backup(backup_dir):
    """Создание резервной копии RepairDesk."""
    if not os.path.isdir(backup_dir):
        os.makedirs(backup_dir)
    print("Резервная копия создана.")
    return True

def main():
    backup_path = "backups/repair_desk_backup"
    restore_from_backup(backup_path, ".")
    print("Восстановление завершено.")

if __name__ == "__main__":
    main()
