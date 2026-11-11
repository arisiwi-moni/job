# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: RepairDesk
def export_records(path, records, sep="\t"):
    """Экспорт списка записей в текстовый файл (TSV/CSV)."""
    if not records:
        print("Нет записей для экспорта")
        return
    if not path:
        print("Не указан путь к файлу")
        return
    headers = records[0].keys()
    with open(path, "w", encoding="utf-8-sig") as f:
        f.write(sep.join(headers) + "\n")
        for row in records:
            values = [str(row.get(h, "")) for h in headers]
            f.write(sep.join(values) + "\n")
    print(f"Экспортировано записей: {len(records)} -> {path}")
