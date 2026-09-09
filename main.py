import sys

from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QWidget

from content_area import ContentArea
from palette import build_qpalette
from sidebar import Sidebar

app: QApplication = QApplication(sys.argv)
app.setPalette(build_qpalette())

window: QMainWindow = QMainWindow()

sidebar = Sidebar()
contentArea = ContentArea()

central = QWidget()
central_layout = QHBoxLayout(central)
central_layout.setContentsMargins(10, 10, 10, 10)
central_layout.setSpacing(10)
central_layout.addWidget(sidebar)
central_layout.addWidget(contentArea)

window.setCentralWidget(central)
window.setWindowTitle("Apex")
window.show()
sys.exit(app.exec())
