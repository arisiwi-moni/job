# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: RepairDesk
def switch_profile(self, profile_name):
        profiles = list(self.profiles.keys())
        if profile_name not in profiles:
            raise ValueError(f"Профиль '{profile_name}' не найден. Доступные: {profiles}")
        self.active_profile = profile_name
        for ticket in self.tickets:
            ticket.apply_profile(profile_name)
        for device in self.devices:
            device.apply_profile(profile_name)
        for part in self.parts:
            part.apply_profile(profile_name)
        for diag in self.diagnoses:
            diag.apply_profile(profile_name)
        print(f"Переключение на профиль: {profile_name}")
