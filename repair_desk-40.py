# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: RepairDesk
import argparse

def main():
    parser = argparse.ArgumentParser(description="RepairDesk CLI")
    sub = parser.add_subparsers(dest="command")

    p_new_ticket = sub.add_parser("new-ticket", help="Создать заявку")
    p_new_ticket.add_argument("device_id", help="ID устройства")
    p_new_ticket.add_argument("--description", "-d", help="Описание проблемы")
    p_new_ticket.add_argument("--status", "-s", choices=["open", "closed", "pending"], default="open")

    p_list = sub.add_parser("list", help="Показать все заявки")

    p_show = sub.add_parser("show", help="Показать заявку")
    p_show.add_argument("ticket_id", help="ID заявки")

    p_close = sub.add_parser("close", help="Закрыть заявку")
    p_close.add_argument("ticket_id", help="ID заявки")

    p_help = sub.add_parser("help", help="Справка")

    args = parser.parse_args()

    if args.command == "new-ticket":
        print(f"Новая заявка #? для устройства {args.device_id} ({args.description or ''}) — статус: {args.status}")
    elif args.command == "list":
        print("Список заявок: (реализовать)")
    elif args.command == "show":
        print(f"Заявка #{args.ticket_id}: (реализовать)")
    elif args.command == "close":
        print(f"Заявка #{args.ticket_id} закрыта — (реализовать)")
    elif args.command == "help":
        parser.print_help()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
