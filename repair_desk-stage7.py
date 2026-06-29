# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: RepairDesk
def sort_records(records, key='date', reverse=False):
    if not records: return []
    order_map = {'low': 1, 'medium': 2, 'high': 3}
    def sort_key(item):
        val = item.get(key)
        if isinstance(val, str): return (0, val.lower(), '')
        if key == 'priority': return (order_map.get(val, 0), '', '')
        if key == 'date': return (val or float('inf'), '', '')
        return (0, '', val or '')
    return sorted(records, key=sort_key, reverse=reverse)
