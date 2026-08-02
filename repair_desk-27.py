# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: RepairDesk
def reset_demo_data():
    """Сбросить демо-данные (устройства, заявки, запчасти) в пустые списки."""
    global devices, tickets, parts
    devices.clear()
    tickets.clear()
    parts.clear()
    print("Демо-данные сброшены.")

def clear_state():
    """Очистить все данные и сбросить статус приложения."""
    reset_demo_data()
    print("Состояние полностью очищено.")
