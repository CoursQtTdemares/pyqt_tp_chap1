import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


def on_button_clicked() -> None:
    print("Button clicked")


def on_checkable_button_clicked() -> None:
    global checkable_button
    text = "Coche" if checkable_button.isChecked() else "Décoche"
    checkable_button.setText(text)
    message = "Checkable button clicked" if checkable_button.isChecked() else "Checkable button unchecked"
    print(message)


app = QApplication(sys.argv)


main_widget = QWidget()
layout = QVBoxLayout()

main_widget.setLayout(layout)

label = QLabel()
label.setTextFormat(Qt.TextFormat.RichText)
label.setText("<b>Hello</b>, <i>PyQt6</i>!")
layout.addWidget(label)

button = QPushButton("Click me")
button.clicked.connect(on_button_clicked)
layout.addWidget(button)

checkable_button = QPushButton("Checkable")
checkable_button.setCheckable(True)
checkable_button.toggled.connect(on_checkable_button_clicked)
layout.addWidget(checkable_button)


with open("style.qss", "r", encoding="utf-8") as file:
    qss_style = file.read()
    app.setStyleSheet(qss_style)

main_widget.show()

sys.exit(app.exec())
