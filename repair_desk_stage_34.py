# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: RepairDesk
TEMPLATES = {
    'laptop_screen': {
        'device_type': 'Laptop',
        'description': 'Сломан экран',
        'diagnosis': 'Замена матрицы',
        'parts': {'Screen': 5000},
        'labor_hours': 2,
        'labor_rate': 1500,
    },
    'phone_battery': {
        'device_type': 'Phone',
        'description': 'Села батарея',
        'diagnosis': 'Замена аккумулятора',
        'parts': {'Battery': 2000},
        'labor_hours': 1,
        'labor_rate': 1000,
    },
}
