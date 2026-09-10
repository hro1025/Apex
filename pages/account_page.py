from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QPushButton,
    QTableWidget,
    QVBoxLayout,
    QWidget,
)

from resources.palette import CATPPUCCIN_MOCHA


class AccountPage(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        title: QLabel = QLabel("Account")
        title.setStyleSheet(
            f"color: {CATPPUCCIN_MOCHA['text']}; font-size: 24px; font-weight: bold;"
        )

        name_label: QLabel = QLabel("Name")
        category_label: QLabel = QLabel("Category")
        balance_label: QLabel = QLabel("Balance")
        for label in (name_label, category_label, balance_label):
            label.setStyleSheet(
                f"color: {CATPPUCCIN_MOCHA['text']}; font-size: 14px; font-weight: bold;"
            )

        add_account_button: QPushButton = QPushButton("Add account")
        add_account_button.setObjectName("add_account_button")

        columns_row: QHBoxLayout = QHBoxLayout()
        columns_row.addWidget(name_label, 1)
        columns_row.addWidget(category_label, 1)
        columns_row.addWidget(balance_label, 1)
        columns_row.addStretch()
        columns_row.addWidget(add_account_button)

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
        layout.addLayout(columns_row)
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
