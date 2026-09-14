from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

from resources.palette import CATPPUCCIN_MOCHA


class AddAccountDialog(QDialog):
    """Ported from Apex.Dialog.AccountAddButtonDialog."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setFixedSize(300, 400)
        self.setObjectName("AddAccountDialog")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        label: QLabel = QLabel("Enter account information")
        label.setStyleSheet(f"color: {CATPPUCCIN_MOCHA['text']}; font-size: 16px;")

        self.name_input: QLineEdit = QLineEdit()
        self.name_input.setPlaceholderText("Name")

        self.category_input: QLineEdit = QLineEdit()
        self.category_input.setPlaceholderText("Category")

        self.balance_input: QLineEdit = QLineEdit()
        self.balance_input.setPlaceholderText("0.00")

        for input_field in (self.name_input, self.category_input, self.balance_input):
            input_field.setStyleSheet(
                f"""
                color: {CATPPUCCIN_MOCHA["text"]};
                border: 1px solid {CATPPUCCIN_MOCHA["border"]};
                border-radius: 6px;
                padding: 6px;
                """
            )

        fields_column: QVBoxLayout = QVBoxLayout()
        fields_column.setSpacing(10)
        fields_column.addWidget(label)
        fields_column.addWidget(self.name_input)
        fields_column.addWidget(self.category_input)
        fields_column.addWidget(self.balance_input)

        import_button: QPushButton = QPushButton("Import")
        import_button.setStyleSheet(
            f"""
            color: {CATPPUCCIN_MOCHA["accent"]};
            background-color: {CATPPUCCIN_MOCHA["header_hover"]};
            border: none;
            border-radius: 8px;
            padding: 8px 16px;
            font-size: 14px;
            """
        )

        add_button: QPushButton = QPushButton("Add")
        add_button.setStyleSheet(
            f"""
            color: {CATPPUCCIN_MOCHA["accent"]};
            background-color: {CATPPUCCIN_MOCHA["header_hover"]};
            border: none;
            border-radius: 8px;
            padding: 8px 16px;
            font-size: 14px;
            """
        )
        add_button.clicked.connect(self.accept)

        button_row: QHBoxLayout = QHBoxLayout()
        button_row.addWidget(import_button)
        button_row.addStretch()
        button_row.addWidget(add_button)

        layout: QVBoxLayout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.addLayout(fields_column)
        layout.addStretch()
        layout.addLayout(button_row)

        self.setStyleSheet(f"""
            #AddAccountDialog {{
                background-color: {CATPPUCCIN_MOCHA["header"]};
                border: 2px solid {CATPPUCCIN_MOCHA["border"]};
            }}
        """)
