# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: RepairDesk
class Color:
    """ANSI color codes with automatic reset and disable support."""
    _on = os.environ.get("REPAIRDESK_COLOR", "1") == "1"
    _codes = {
        "reset": "\033[0m",
        "bold": "\033[1m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "bright_red": "\033[91m",
        "bright_green": "\033[92m",
        "bright_yellow": "\033[93m",
        "bright_blue": "\033[94m",
        "bright_magenta": "\033[95m",
        "bright_cyan": "\033[96m",
    }

    @classmethod
    def off(cls):
        cls._on = False
        cls._reset()

    @classmethod
    def on(cls):
        cls._on = True
        cls._reset()

    @classmethod
    def _reset(cls):
        if not cls._on:
            cls._codes["reset"] = ""
            cls._codes["bold"] = ""
            for k in list(cls._codes):
                if k != "reset" and k != "bold":
                    cls._codes[k] = ""

    @classmethod
    def c(cls, color, text=""):
        if cls._on:
            return cls._codes.get(color, "") + text + cls._codes["reset"]
        return text

    @classmethod
    def header(cls, text):
        return cls.c("bold", text)

    @classmethod
    def success(cls, text):
        return cls.c("bright_green", text)

    @classmethod
    def error(cls, text):
        return cls.c("bright_red", text)

    @classmethod
    def warning(cls, text):
        return cls.c("bright_yellow", text)

    @classmethod
    def info(cls, text):
        return cls.c("bright_blue", text)

    @classmethod
    def dim(cls, text):
        return cls.c("dim", text) if hasattr(cls, "_codes") else text
