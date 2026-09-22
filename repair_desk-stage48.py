# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: RepairDesk
def _format_cost(total, fmt='currency'):
    """Format a numeric cost value for display."""
    if fmt == 'currency':
        return f'{total:.2f}₽'
    return f'{total}'

def _split_invoice(items, total):
    """Return a list of dicts: each item = {name, qty, unit, price, subtotal}."""
    rows = []
    for it in items:
        sub = it['price'] * it['qty']
        rows.append({
            'name': it['name'],
            'qty': it['qty'],
            'unit': it.get('unit', 'шт'),
            'price': it['price'],
            'subtotal': sub,
        })
    return rows

def _print_receipt(receipt):
    """Pretty-print a receipt to stdout."""
    lines = []
    lines.append('╔══════════════════════════════════╗')
    lines.append('║        RepairDesk — Чек          ║')
    lines.append('╠══════════════════════════════════╣')
    lines.append(f'║ Дата: {receipt["date"]}          ║')
    lines.append(f'║ Заказ: #{receipt["order_id"]:04d}   ║')
    lines.append('╠══════════════════════════════════╣')
    for r in receipt['items']:
        lines.append(f'║ {r["name"]:20s} x{r["qty"]:2d} @ {r["price"]:>7,.2f}₽ ║')
    lines.append('╠══════════════════════════════════╣')
    lines.append(f'║ ИТОГО: {receipt["total"]:>20,.2f}₽ ║')
    lines.append('╚══════════════════════════════════╝')
    print('\n'.join(lines))
