# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: RepairDesk
def parse_date(date_str):
    """Парсит дату в формате ДД.ММ.ГГГГ или ГГГГ-ММ-ДД, возвращает datetime.date."""
    import datetime
    date_str = date_str.strip()
    for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            return datetime.datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Неправильный формат даты: {date_str}. Ожидаются форматы ДД.ММ.ГГГГ или ГГГГ-ММ-ДД.")
