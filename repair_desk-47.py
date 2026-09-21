# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: RepairDesk
def demo():
    print("=" * 60)
    print("RepairDesk Demo — создание заявки на ремонт")
    print("=" * 60)

    # 1. Регистрация клиента
    client = Client("Иванов Иван", "+79991234567", "Москва")
    client.save()
    print(f"Клиент зарегистрирован: {client.name}")

    # 2. Добавление устройства
    device = Device("Samsung Galaxy S21", "SM-G991B", "2022-03-15")
    device.save()
    print(f"Устройство добавлено: {device.name}")

    # 3. Добавление запчасти
    part = SparePart("Экран дисплей", "Samsung E5527-2", 3500.0, 2)
    part.save()
    print(f"Запчасть добавлена: {part.name} — {part.price} руб.")

    # 4. Создание заявки
    ticket = Ticket(
        client_id=client.id,
        device_id=device.id,
        issue="Экран разбит, трещина по диагонали",
        priority="high",
        estimated_cost=part.price,
    )
    ticket.add_diagnosis("Замена матрицы")
    ticket.add_diagnosis("Проверка разъёма зарядки")
    ticket.add_spare_part(part)
    ticket.save()
    print(f"Заявка #{ticket.id} создана")
    print(f"  Приоритет: {ticket.priority}")
    print(f"  Диагностика: {', '.join(ticket.diagnoses)}")
    print(f"  Стоимость: {ticket.total_cost()} руб.")

    # 5. Вывод отчёта
    report = TicketReport.generate(ticket)
    print("\n--- Отчёт по заявке ---")
    print(report)

    # 6. Поиск по клиенту
    client_tickets = Ticket.find_by_client(client.id)
    print(f"\nКлиент {client.name} имеет {len(client_tickets)}(ы) заявок.")

    # 7. Статистика
    stats = TicketStats()
    stats.update_from_tickets(Ticket.all())
    print(f"\nСтатистика: {stats}")

    print("\nДемо завершён. Все данные сохранены в SQLite.")
    return ticket, client, stats
