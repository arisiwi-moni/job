# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: RepairDesk
def get_weekly_stats():
    stats = {}
    for ticket in all_tickets:
        date = ticket["created_at"][:10]
        wday = (datetime.strptime(date, "%Y-%m-%d").weekday() + 1) % 7
        key = f"{date} (Вт {wday})"
        stats[key] = stats.get(key, 0) + 1
    return stats

def print_weekly_stats():
    stats = get_weekly_stats()
    if not stats:
        print("Нет данных для статистики.")
        return
    print("\nНедельная статистика по датам:")
    for day, count in sorted(stats.items()):
        print(f"  {day}: {count} заявок")
