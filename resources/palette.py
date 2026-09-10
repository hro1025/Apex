from PySide6.QtGui import QColor, QPalette

CATPPUCCIN_MOCHA = {
    "background": "#1e1e2e",  # Base
    "background_dark": "#181825",  # Mantle — one step darker than background
    "header": "#313244",  # Surface0 — panel/sidebar background
    "header_hover": "#45475a",  # Surface1 — hover state for panel items
    "header_active": "#585b70",  # Surface2 — pressed/active state, one step past hover
    "border": "#45475a",  # Surface1
    "border_light": "#6c7086",  # Overlay0 — a lighter border for emphasis
    "text": "#cdd6f4",  # Text
    "muted": "#7f849c",  # Overlay1
    "accent": "#cba6f7",  # Mauve
    "accent_hover": "#f5c2e7",  # Pink — a nearby hue Catppuccin pairs with mauve for hover
}


def build_qpalette() -> QPalette:
    p: QPalette = QPalette()
    p.setColor(QPalette.ColorRole.Window, QColor(CATPPUCCIN_MOCHA["background"]))
    p.setColor(QPalette.ColorRole.Base, QColor(CATPPUCCIN_MOCHA["header"]))
    p.setColor(QPalette.ColorRole.WindowText, QColor(CATPPUCCIN_MOCHA["text"]))
    p.setColor(QPalette.ColorRole.Text, QColor(CATPPUCCIN_MOCHA["text"]))
    p.setColor(QPalette.ColorRole.Button, QColor(CATPPUCCIN_MOCHA["header"]))
    p.setColor(QPalette.ColorRole.ButtonText, QColor(CATPPUCCIN_MOCHA["text"]))
    p.setColor(QPalette.ColorRole.Highlight, QColor(CATPPUCCIN_MOCHA["accent"]))
    p.setColor(
        QPalette.ColorRole.HighlightedText, QColor(CATPPUCCIN_MOCHA["background"])
    )
    p.setColor(QPalette.ColorRole.PlaceholderText, QColor(CATPPUCCIN_MOCHA["muted"]))
    return p
