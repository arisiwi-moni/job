# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: RepairDesk
# Quick demo commands for manual testing — run each line in REPL after importing RepairDesk module
def _demo():
    print("=== RepairDesk Demo Commands ===")
    from repairdesk import App, DeviceType, DiagnosticStep, Part, OrderStatus, TicketPriority

    app = App()
    app.seed_demo_data(5)  # 5 demo tickets

    for ticket in app.tickets:
        print(f"\n--- Ticket #{ticket.id} ({ticket.status}, priority={ticket.priority}) ---")
        print(f"Device: {ticket.device_type.name}")
        print(f"Symptoms: {', '.join(ticket.symptoms)}")
        if hasattr(ticket, 'diagnostics'):
            for step in ticket.diagnostics:
                print(f"  Step: {step.name} → result={step.result}")
        if hasattr(ticket, 'parts_used'):
            for p in ticket.parts_used:
                cost = app.price_db.get_price(p.part_id) if hasattr(app, 'price_db') else None
                print(f"  Part: {p.part_name}, qty={p.quantity}, price={cost}")
        total_cost = sum(getattr(ticket, '_total_cost', 0)) if hasattr(ticket, '_total_cost') else 0
        print(f"Total cost: ${total_cost:.2f}")

    # Show all device types and part catalog summary
    print("\n=== Available Devices ===")
    for dt in DeviceType:
        print(f"- {dt.name}: {dt.description[:60]}…")

    print("\n=== Sample Parts Catalog (first 5) ===")
    parts = sorted(app.price_db.catalog, key=lambda p: p.part_id)[:5] if hasattr(app, 'price_db') else []
    for p in parts:
        price = app.price_db.get_price(p.part_id) if hasattr(app, 'price_db') else 0
        print(f"- {p.part_name}: ${price:.2f}")

_demo()
