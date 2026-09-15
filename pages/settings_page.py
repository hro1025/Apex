from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox, QLabel, QVBoxLayout, QWidget

from resources.palette import THEMES, get_theme_name
from resources.theme_manager import theme_manager


class SettingsPage(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.title: QLabel = QLabel("Settings")

        self.separator: QWidget = QWidget()
        self.separator.setFixedHeight(2)
        self.separator.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.theme_label: QLabel = QLabel("Theme")

        self.theme_picker: QComboBox = QComboBox()
        self.theme_picker.addItems(list(THEMES.keys()))
        self.theme_picker.setCurrentText(get_theme_name())
        self.theme_picker.currentTextChanged.connect(theme_manager.set_theme)

        layout: QVBoxLayout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        layout.addWidget(self.title)
        layout.addWidget(self.separator)
        layout.addWidget(self.theme_label)
        layout.addWidget(self.theme_picker)
        layout.addStretch()

        theme_manager.theme_changed.connect(self.apply_theme)
        self.apply_theme(theme_manager.current_theme)

    def apply_theme(self, theme: dict[str, str]) -> None:
        self.title.setStyleSheet(
            f"color: {theme['text']}; font-size: 24px; font-weight: bold;"
        )
        self.separator.setStyleSheet(f"background-color: {theme['border']};")
        self.theme_label.setStyleSheet(f"color: {theme['text']}; font-size: 16px;")
        self.theme_picker.setStyleSheet(
            f"""
            color: {theme["text"]};
            background-color: {theme["header_hover"]};
            border: 1px solid {theme["border"]};
            border-radius: 6px;
            padding: 6px;
            """
        )
        self.setStyleSheet("background-color: transparent;")
