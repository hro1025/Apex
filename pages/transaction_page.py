from PySide6.QtGui import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHeaderView,
    QLabel,
    QTableWidget,
    QVBoxLayout,
    QWidget,
)

from resources.palette import CATPPUCCIN_MOCHA


class TransactionPage(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        title: QLabel = QLabel("Transaction")
        title.setStyleSheet(
            f"color: {CATPPUCCIN_MOCHA['text']}; font-size: 24px; font-weight: bold;"
        )

        separator: QWidget = QWidget()
        separator.setFixedHeight(2)
        separator.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        separator.setStyleSheet(f"background-color: {CATPPUCCIN_MOCHA['border']};")

        accounts_table: QTableWidget = QTableWidget()
        accounts_table.setColumnCount(3)
        accounts_table.setFrameShape(QFrame.Shape.NoFrame)
        accounts_table.horizontalHeader().setVisible(False)
        accounts_table.verticalHeader().setVisible(False)
        accounts_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        accounts_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        layout: QVBoxLayout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        layout.addWidget(title)
        layout.addWidget(separator)
        layout.addWidget(accounts_table)

        self.setStyleSheet(f"""
            #add_account_button {{
                color: {CATPPUCCIN_MOCHA["accent"]};
                background-color: {CATPPUCCIN_MOCHA["header_hover"]};
                border: none;
                border-radius: 10px;
                text-align: left;
                padding: 8px 12px;
                font-size: 14px;
            }}
            #add_account_button:hover {{
                background-color: {CATPPUCCIN_MOCHA["header_active"]};
            }}
            #add_account_button:pressed {{
                background-color: {CATPPUCCIN_MOCHA["border_light"]};
            }}
""")
