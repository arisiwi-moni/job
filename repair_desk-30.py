# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: RepairDesk
class UserProfile:
    def __init__(self, name, role='user'):
        self.name = name
        self.role = role

    def __repr__(self):
        return f"UserProfile({self.name}, {self.role})"

class UserStore:
    def __init__(self):
        self._profiles = {}
        self._current = None

    def add(self, name, role='user'):
        u = UserProfile(name, role)
        self._profiles[name] = u
        return u

    def login(self, name):
        if name not in self._profiles:
            raise ValueError(f'Unknown user: {name}')
        self._current = self._profiles[name]
        return self._current

    def logout(self):
        self._current = None

    def get_current(self):
        return self._current

    def current_name(self):
        return self._current.name if self._current else None
