from datetime import datetime
from zoneinfo import ZoneInfo

from PyQt6.QtWidgets import QHBoxLayout, QLineEdit, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget

PARIS_TZ = ZoneInfo("Europe/Paris")


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Ma Première Application, TP chapitre 1")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        horizontal_layout = QHBoxLayout()
        layout.addLayout(horizontal_layout)

        self.line_edit = QLineEdit()
        horizontal_layout.addWidget(self.line_edit)

        button = QPushButton("Click me")
        button.clicked.connect(self.on_button_clicked)
        horizontal_layout.addWidget(button)

        self.text_edit = QTextEdit()
        self.text_edit.setEnabled(False)
        layout.addWidget(self.text_edit)

    def on_button_clicked(self) -> None:
        line_edit_text = self.line_edit.text()
        date_string = datetime.now(PARIS_TZ).strftime("%d/%m/%Y %H:%M:%S")
        previous_text = self.text_edit.toPlainText()
        self.text_edit.setText(f"{date_string} - {line_edit_text}\n{previous_text}")
