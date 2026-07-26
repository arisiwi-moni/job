# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: RepairDesk
def print_table(rows, columns):
    widths = [max(len(str(row[i])) for row in rows) if rows else 0 for i in range(columns)]
    header = ' | '.join(f'{col:^{widths[i]}}' for i, col in enumerate(map(lambda _: '', columns)))
    print(header)
    divider = '-+-'.join('-' * widths[i] for i in range(len(columns)))
    print(divider)
    for row in rows:
        line = ' | '.join(str(row[i]) if i < len(row) else '' for i in range(columns))
        print(line.replace(' ', ' ').lstrip().rstrip())

def format_cost(cost):
    return f'{cost:,.2f} руб.'
