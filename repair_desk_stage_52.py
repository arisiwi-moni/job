# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: RepairDesk
def export_report():
    if not data['requests']:
        print("Нет заявок для отчёта")
        return
    lines = ["ОТЧЁТ ПО РЕМОНТУ", "=" * 20, ""]
    for r in data['requests']:
        parts = []
        for p in r.get('parts', []):
            parts.append(f"{p['name']} x{p['qty']} = {p['price'] * p['qty']}")
        lines.append(f"Заявка {r['id']}: {r['device']} - {r['diag']}")
        lines.append(f"Стоимость: {sum(p['price'] * p['qty'] for p in r.get('parts', []))}")
        lines.append("Запчасти: " + "; ".join(parts))
        lines.append("")
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("Отчёт сохранён в report.txt")
