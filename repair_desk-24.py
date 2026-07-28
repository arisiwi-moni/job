# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: RepairDesk
def print_ticket(ticket):
    parts = []
    parts.append(f"ID: {ticket['id']}")
    parts.append(f"Устройство: {ticket.get('device', 'Не указано')}")
    parts.append(f"Проблема: {ticket.get('problem', 'Не указана')}")
    if ticket.get('diagnosis'):
        parts.append(f"Диагностика: {ticket['diagnosis']}")
    if ticket.get('parts_used'):
        total = sum(p.get('price', 0) for p in ticket['parts_used'])
        parts.append(f"Запчасти ({len(ticket['parts_used'])}): {total} руб.")
    if ticket.get('labor_cost') is not None:
        parts.append(f"Стоимость работы: {ticket['labor_cost']} руб.")
    if ticket.get('status'):
        parts.append(f"Статус: {ticket['status']}")
    print("─" * 40)
    print(", ".join(parts))
