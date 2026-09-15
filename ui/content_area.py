from PySide6.QtCore import Qt
from PySide6.QtWidgets import QStackedWidget, QVBoxLayout, QWidget

from pages.account_page import AccountPage
from pages.dashboard_page import DashboardPage
from pages.settings_page import SettingsPage
from pages.transaction_page import TransactionPage
from resources.theme_manager import theme_manager


class ContentArea(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("ContentArea")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, on=True)

        self.dashboard_page = DashboardPage()
        self.transaction_page = TransactionPage()
        self.account_page = AccountPage()
        self.settings_page = SettingsPage()

        self.stack = QStackedWidget()
        self.stack.addWidget(self.dashboard_page)
        self.stack.addWidget(self.transaction_page)
        self.stack.addWidget(self.account_page)
        self.stack.addWidget(self.settings_page)

        layout: QVBoxLayout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        layout.addWidget(self.stack)

        theme_manager.theme_changed.connect(self.apply_theme)
        self.apply_theme(theme_manager.current_theme)

    def apply_theme(self, theme: dict[str, str]) -> None:
        self.setStyleSheet(f"""
            #ContentArea {{
                background-color: {theme["header"]};
                border: 2px solid {theme["border"]};
                border-radius: 10px;
            }}
        """)
