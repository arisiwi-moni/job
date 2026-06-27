# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: RepairDesk
def filter_records(status=None, category=None, tags=None):
    filtered = []
    for record in records:
        if status and record['status'] != status: continue
        if category and record.get('category') != category: continue
        if tags:
            rec_tags = set(record.get('tags', [])).intersection(set(tags))
            if not rec_tags: continue
        filtered.append(record)
    return filtered

def search_records(query):
    results = []
    query_lower = query.lower()
    for record in records:
        text = f"{record['device']} {record.get('diagnosis', '')} {' '.join(record.get('tags', []))}".lower()
        if query_lower in text: results.append(record)
    return results

def get_records_by_date_range(start_date, end_date):
    filtered = []
    for record in records:
        date_str = record.get('created_at', '')
        if start_date and date_str < start_date: continue
        if end_date and date_str > end_date: continue
        filtered.append(record)
    return filtered
