from PyQt6.QtWidgets import QHBoxLayout, QLineEdit, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget


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

        line_edit = QLineEdit()
        line_edit.textChanged.connect(self.on_line_edit_changed)
        horizontal_layout.addWidget(line_edit)

        button = QPushButton("Click me")
        button.clicked.connect(self.on_button_clicked)
        horizontal_layout.addWidget(button)

        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self.on_text_edit_changed)
        layout.addWidget(self.text_edit)

    def on_line_edit_changed(self, text: str) -> None:
        print(f"Line edit changed: {text}")

    def on_button_clicked(self) -> None:
        print("Button clicked")

    def on_text_edit_changed(self) -> None:
        text = self.text_edit.toPlainText()
        print(f"Text edit changed: {text}")
