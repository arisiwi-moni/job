# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: RepairDesk
def edit_record(record_id, updates):
    if record_id not in records:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    
    for key, value in updates.items():
        if hasattr(records[record_id], key):
            setattr(records[record_id], key, value)
    
    print(f"Запись #{record_id} успешно обновлена.")
    return True
