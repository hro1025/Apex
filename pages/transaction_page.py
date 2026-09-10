from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class TransactionPage(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        label: QLabel = QLabel("Transaction")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px;")

        layout: QVBoxLayout = QVBoxLayout(self)
        layout.addWidget(label)
