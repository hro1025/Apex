from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget

from palette import CATPPUCCIN_MOCHA


class Sidebar(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setFixedWidth(200)
        self.setObjectName("Sidebar")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        dashboard_button: QPushButton = QPushButton("Dashboard")
        transaction_button: QPushButton = QPushButton("Transaction")
        accounts_button: QPushButton = QPushButton("Accounts")
        settings_button: QPushButton = QPushButton("Settings")

        layout: QVBoxLayout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        layout.addWidget(dashboard_button)
        layout.addWidget(transaction_button)
        layout.addWidget(accounts_button)

        layout.addStretch()  # pushes everything after this to the bottom

        layout.addWidget(settings_button)

        self.setStyleSheet(f"""
            #Sidebar {{
                background-color: {CATPPUCCIN_MOCHA["header"]};
                border: 2px solid {CATPPUCCIN_MOCHA["border"]};
                border-radius: 10px;
            }}
            QPushButton {{
                color: {CATPPUCCIN_MOCHA["accent"]};
                background-color: {CATPPUCCIN_MOCHA["header_hover"]};
                border: none;
                border-radius: 10px;
                text-align: left;
                padding: 8px 12px;
                font-size: 16px;
            }}
            QPushButton:hover {{
                background-color: {CATPPUCCIN_MOCHA["header_active"]};
            }}
            QPushButton:pressed {{
                background-color: {CATPPUCCIN_MOCHA["border_light"]};
            }}
        """)
