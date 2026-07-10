# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: RepairDesk
def search_repair_desks(query):
    if not query:
        return []
    query = query.lower().strip()
    results = []
    for desk in RepairDesk.all():
        fields_to_check = [
            'name', 'brand', 'model', 'serial_number',
            'status', 'priority', 'diagnosis', 'description'
        ]
        if any(query in field.lower() for field in fields_to_check):
            results.append(desk)
    return results
