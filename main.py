import sys

from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QWidget

from palette import build_qpalette
from sidebar import Sidebar

app: QApplication = QApplication(sys.argv)
app.setPalette(build_qpalette())

window: QMainWindow = QMainWindow()

sidebar = Sidebar()
content_area = QWidget()  # placeholder for now — your pages will go here later

central = QWidget()
central_layout = QHBoxLayout(central)
central_layout.setContentsMargins(10, 10, 0, 10)
central_layout.addWidget(sidebar)
central_layout.addWidget(content_area)

window.setCentralWidget(central)
window.setWindowTitle("Apex")
window.show()
sys.exit(app.exec())
