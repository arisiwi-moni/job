# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: RepairDesk
def delete_record(table_name, record_id):
    if not table_name or not record_id:
        raise ValueError("Идентификатор таблицы и записи обязательны")
    try:
        cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (record_id,))
        return cursor.rowcount > 0
    except sqlite3.OperationalError as e:
        if "no such table" in str(e):
            raise ValueError(f"Таблица '{table_name}' не найдена")
        raise
