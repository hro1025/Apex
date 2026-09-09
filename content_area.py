from PySide6.QtGui import Qt
from PySide6.QtWidgets import QStackedWidget, QVBoxLayout, QWidget

from account_page import AccountPage
from dashboard_page import DashboardPage
from palette import CATPPUCCIN_MOCHA
from settings_page import SettingsPage
from transaction_page import TransactionPage


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

        self.setStyleSheet(f"""
            #ContentArea {{
                background-color: {CATPPUCCIN_MOCHA["header"]};
                border: 2px solid {CATPPUCCIN_MOCHA["border"]};
                border-radius: 10px;
            }}
        """)
