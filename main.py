import sys

from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QWidget

from content_area import ContentArea
from palette import build_qpalette
from sidebar import Sidebar

app: QApplication = QApplication(sys.argv)
app.setPalette(build_qpalette())

window: QMainWindow = QMainWindow()

sidebar = Sidebar()
content_area = ContentArea()

sidebar.navigate_dashboard.connect(
    lambda: content_area.stack.setCurrentWidget(content_area.dashboard_page)
)
sidebar.navigate_transaction.connect(
    lambda: content_area.stack.setCurrentWidget(content_area.transaction_page)
)
sidebar.navigate_accounts.connect(
    lambda: content_area.stack.setCurrentWidget(content_area.account_page)
)
sidebar.navigate_settings.connect(
    lambda: content_area.stack.setCurrentWidget(content_area.settings_page)
)

central = QWidget()
central_layout = QHBoxLayout(central)
central_layout.setContentsMargins(10, 10, 10, 10)
central_layout.setSpacing(10)
central_layout.addWidget(sidebar)
central_layout.addWidget(content_area)

window.setCentralWidget(central)
window.setWindowTitle("Apex")
window.show()
sys.exit(app.exec())
