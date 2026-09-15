from PySide6.QtCore import QObject, Signal

from resources.palette import THEMES, get_theme_name, set_theme_name


class ThemeManager(QObject):
    theme_changed = Signal(dict)

    def __init__(self) -> None:
        super().__init__()
        self.current_theme: dict[str, str] = THEMES.get(
            get_theme_name(), THEMES["Catppuccin Mocha"]
        )

    def set_theme(self, name: str) -> None:
        set_theme_name(name)
        self.current_theme = THEMES[name]
        self.theme_changed.emit(self.current_theme)


theme_manager = ThemeManager()
