# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: RepairDesk
def print_summary():
    """Generate a brief summary of current data."""
    print("\n=== RepairDesk Summary ===")
    total_tickets = len(tickets) if 'tickets' in globals() else 0
    open_tickets = sum(1 for t in tickets.values() if t.get('status') == 'open')
    closed_tickets = sum(1 for t in tickets.values() if t.get('status') == 'closed')
    print(f"Total tickets: {total_tickets}")
    print(f"Open: {open_tickets}, Closed: {closed_tickets}")

    total_devices = len(devices) if 'devices' in globals() else 0
    print(f"Devices tracked: {total_devices}")

    total_parts = sum(len(parts.get(d, [])) for d in parts) if 'parts' in globals() else 0
    print(f"Parts used: {total_parts}")

    total_cost = sum(
        t.get('cost', 0) + sum(p.get('price', 0) * p.get('qty', 1) for p in (parts.get(t.get('device_id'), []) or []))
        for t in tickets.values()
    ) if 'tickets' in globals() else 0
    print(f"Total cost: {total_cost:.2f}")
