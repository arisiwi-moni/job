# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: RepairDesk
def monthly_statistics(tickets):
    from collections import defaultdict
    stats = defaultdict(lambda: {'count': 0, 'total_cost': 0})
    for t in tickets:
        if isinstance(t['date'], datetime.date):
            key = (t['date'].year, t['date'].month)
        else:
            key = ('unknown', 'unknown')
        stats[key]['count'] += 1
        cost = sum(item.get('cost', 0) for item in t.get('parts', []))
        stats[key]['total_cost'] += cost
    return dict(stats)
