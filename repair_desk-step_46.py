# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: RepairDesk
def migrate_version():
    """Upgrade RepairDesk structure to version 2.0."""
    global VERSION
    if VERSION < 2:
        VERSION = 2
        # Миграция: добавить поле 'warranty_end' в Device
        for device in devices:
            if 'warranty_end' not in device:
                device['warranty_end'] = None
        # Миграция: добавить поле 'estimated_cost' в Request
        for req in requests:
            if 'estimated_cost' not in req:
                req['estimated_cost'] = 0
        print("Migration to version 2.0 complete.")
