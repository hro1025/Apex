from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QWidget

from palette import CATPPUCCIN_MOCHA


class ContentArea(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("ContentArea")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, on=True)

        layout: QVBoxLayout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        self.setStyleSheet(f"""
    #ContentArea {{
        background-color: {CATPPUCCIN_MOCHA["header"]};
        border: 2px solid {CATPPUCCIN_MOCHA["border"]};
        border-radius: 10px;
    }}
""")
