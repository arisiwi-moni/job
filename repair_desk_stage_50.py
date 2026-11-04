# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: RepairDesk
def format_price(amount) -> str:
    """Форматирует числовое значение стоимости как строку с разделителем."""

    return f"{amount:,.2f}"


def build_summary_line(item_name: str, quantity: int, unit_price: float) -> str:
    """Собирает строку описания позиции в итоговой ведомости."""

    return f"{item_name} × {quantity} @ {format_price(unit_price)} = {format_price(unit_price * quantity)}"


def render_receipt(appointment: dict) -> str:
    """Формирует аккуратный текстовый чек для заявки."""

    lines = [
        "════════════════════════════════════════",
        f"  RepairDesk — чек заявки №{appointment['id']}",
        "════════════════════════════════════════",
        f"  Устройство: {appointment['device']} {appointment['type']}",
        f"  Клиент:     {appointment['client']}",
        f"  Диагноз:    {appointment['diagnosis']}",
        "",
    ]

    parts = [build_summary_line(p["name"], p["quantity"], p["price"]) for p in appointment["parts"]]
    lines.extend(part for part in parts if part)

    labor = appointment["labor"]
    total = labor + sum(p["price"] * p["quantity"] for p in appointment["parts"])
    lines.append("─" * 45)
    lines.append(f"  Работа:       {format_price(labor)}")
    lines.append(f"  Итого:        {format_price(total)}")
    lines.append("════════════════════════════════════════")

    return "\n".join(lines)


def print_receipt(appointment: dict) -> None:
    """Выводит сформированный чек заявки в консоль."""

    print(render_receipt(appointment))
