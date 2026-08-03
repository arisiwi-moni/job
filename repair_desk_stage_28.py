# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: RepairDesk
import statistics


def compute_project_metrics():
    """Compute and display key RepairDesk project metrics."""
    if not devices:
        return None

    total_revenue = sum(device.get("total_cost", 0) for device in devices.values())
    avg_price = (sum(device.get("price", 0) for device in devices.values()) / len(devices)) if devices else 0
    avg_total_cost = (sum(device.get("total_cost", 0) for device in devices.values()) / len(devices)) if devices else 0

    status_counts = {}
    for device in devices.values():
        st = device.get("status", "pending")
        status_counts[st] = status_counts.get(st, 0) + 1

    diagnosis_distribution = {}
    for device in devices.values():
        diag = device.get("diagnosis", None)
        if diag:
            diagnosis_distribution[diag] = diagnosis_distribution.get(diag, 0) + 1

    cost_deviation = [(device.get("total_cost", 0) - device.get("price", 0)) / max(device.get("price", 1), 1) * 100 for device in devices.values()]
    avg_cost_deviation = statistics.mean(cost_deviation) if cost_deviation else 0

    return {
        "total_devices": len(devices),
        "pending_count": status_counts.get("pending", 0),
        "repaired_count": status_counts.get("repaired", 0),
        "returned_count": status_counts.get("returned", 0),
        "total_revenue": total_revenue,
        "avg_price": avg_price,
        "avg_total_cost": avg_total_cost,
        "diagnosis_distribution": diagnosis_distribution,
        "avg_cost_deviation_percent": round(avg_cost_deviation, 2) if cost_deviation else 0.0,
    }


def print_metrics():
    metrics = compute_project_metrics()
    if not metrics:
        print("Нет устройств в системе для расчёта метрик.")
        return

    print("\n=== Ключевые метрики проекта RepairDesk ===")
    print(f"Общее кол-во устройств: {metrics['total_devices']}")
    print(f"В ожидании: {metrics['pending_count']}")
    print(f"Отремонтировано: {metrics['repaired_count']}")
    print(f"Вернулось клиенту: {metrics['returned_count']}")
    print(f"\nДоход (по total_cost): {metrics['total_revenue']:.2f}")
    print(f"Средняя цена устройства: {metrics['avg_price']:.2f}")
    print(f"Средняя итоговая стоимость: {metrics['avg_total_cost']:.2f}")

    if metrics['diagnosis_distribution']:
        print("\nРаспределение диагнозов:")
        for diag, count in sorted(metrics['diagnosis_distribution'].items()):
            print(f"  '{diag}': {count}")

    print(f"\nСреднее отклонение итоговой стоимости от цены: {metrics['avg_cost_deviation_percent']:.2f}%")
