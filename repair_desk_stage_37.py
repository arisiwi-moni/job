# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: RepairDesk
import unittest


class TestRepairDesk(unittest.TestCase):
    def test_device_creation(self):
        from repair_desk.models import Device
        d = Device(name="iPhone 14", model="A2883")
        self.assertEqual(d.name, "iPhone 14")
        self.assertEqual(d.model, "A2883")
        self.assertFalse(d.is_diagnosed)

    def test_ticket_status_flow(self):
        from repair_desk.models import Ticket
        t = Ticket(device=Device(name="Samsung S21"))
        self.assertEqual(t.status, "open")
        t.diagnose("screen cracked")
        self.assertEqual(t.status, "diagnosed")
        t.fix("replaced screen", cost=1500)
        self.assertEqual(t.status, "fixed")

    def test_invoice_total(self):
        from repair_desk.models import Invoice, InvoiceLine
        inv = Invoice()
        inv.add_line(InvoiceLine("screen", 1500, 1))
        inv.add_line(InvoiceLine("labor", 1000, 1))
        self.assertEqual(inv.total, 2500)

    def test_part_inventory(self):
        from repair_desk.models import Part
        p = Part(name="OLED screen", sku="OLED-001", price=1500)
        self.assertEqual(p.price, 1500)
        p.stock = 5
        p.consume(2)
        self.assertEqual(p.stock, 3)


if __name__ == "__main__":
    unittest.main()
