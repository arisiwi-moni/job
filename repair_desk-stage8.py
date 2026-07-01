# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: RepairDesk
class RepairDeskCLI:
    def __init__(self):
        self.menu = {
            '1': ('Управление заявками', lambda s: s.manage_requests()),
            '2': ('Управление устройствами', lambda s: s.manage_devices()),
            '3': ('Управление запчастями', lambda s: s.manage_parts()),
            '4': ('Выход', lambda _: exit(0))
        }

    def print_menu(self):
        print("\n=== RepairDesk CLI ===")
        for key, (desc, _) in self.menu.items():
            print(f"[{key}] {desc}")
        try:
            choice = input("Выберите действие: ").strip()
            if choice in self.menu:
                action, handler = self.menu[choice]
                print(f"\n--- {action} ---")
                handler(self)
            else:
                print("Неверный выбор.")
        except KeyboardInterrupt:
            print("\nВыход из программы.")

    def manage_requests(self):
        print("1. Создать заявку\n2. Просмотреть заявки\n3. Вернуться в меню")
        try:
            choice = input("Выберите действие: ").strip()
            if choice == '1':
                model = input("Модель устройства: ")
                issue = input("Описание проблемы: ")
                print(f"Заявка создана для {model}: {issue}")
            elif choice == '2':
                print("Список заявок (пусто)")
            else:
                self.print_menu()
        except KeyboardInterrupt:
            pass

    def manage_devices(self):
        print("1. Добавить устройство\n2. Вернуться в меню")
        try:
            choice = input("Выберите действие: ").strip()
            if choice == '1':
                model = input("Модель устройства: ")
                sn = input("Серийный номер: ")
                print(f"Устройство {model} ({sn}) добавлено.")
            else:
                self.print_menu()
        except KeyboardInterrupt:
            pass

    def manage_parts(self):
        print("1. Добавить запчасть\n2. Вернуться в меню")
        try:
            choice = input("Выберите действие: ").strip()
            if choice == '1':
                name = input("Название запчасти: ")
                price = float(input("Цена: "))
                print(f"Запчасть {name} добавлена.")
            else:
                self.print_menu()
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    app = RepairDeskCLI()
    while True:
        app.print_menu()
