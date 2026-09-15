from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHeaderView,
    QLabel,
    QTableWidget,
    QVBoxLayout,
    QWidget,
)

from resources.theme_manager import theme_manager


class DashboardPage(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.title: QLabel = QLabel("Dashboard")

        self.separator: QWidget = QWidget()
        self.separator.setFixedHeight(2)
        self.separator.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.accounts_table: QTableWidget = QTableWidget()
        self.accounts_table.setColumnCount(3)
        self.accounts_table.setFrameShape(QFrame.Shape.NoFrame)
        self.accounts_table.horizontalHeader().setVisible(False)
        self.accounts_table.verticalHeader().setVisible(False)
        self.accounts_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.accounts_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        layout: QVBoxLayout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        layout.addWidget(self.title)
        layout.addWidget(self.separator)
        layout.addWidget(self.accounts_table)

        theme_manager.theme_changed.connect(self.apply_theme)
        self.apply_theme(theme_manager.current_theme)

    def apply_theme(self, theme: dict[str, str]) -> None:
        self.title.setStyleSheet(
            f"color: {theme['text']}; font-size: 24px; font-weight: bold;"
        )
        self.separator.setStyleSheet(f"background-color: {theme['border']};")

        self.setStyleSheet(f"""
    QWidget {{
        background-color: transparent;
    }}
    #add_account_button {{
        color: {theme["accent"]};
        background-color: {theme["header_hover"]};
        border: none;
        border-radius: 10px;
        text-align: left;
        padding: 8px 12px;
        font-size: 14px;
    }}
    #add_account_button:hover {{
        background-color: {theme["header_active"]};
    }}
    #add_account_button:pressed {{
        background-color: {theme["border_light"]};
    }}
""")
