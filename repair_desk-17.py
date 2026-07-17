# === Stage 17: Добавь группировку записей по категориям ===
# Project: RepairDesk
from collections import defaultdict


def group_records_by_category(records, category_field):
    grouped = defaultdict(list)
    for record in records:
        key = record.get(category_field, 'Uncategorized')
        grouped[key].append(record)
    return dict(grouped)
