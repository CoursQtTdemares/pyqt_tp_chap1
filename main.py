import sys

from PyQt6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

label = QLabel("Hello, PyQt6!")

with open("style.qss", "r", encoding="utf-8") as file:
    qss_style = file.read()
    app.setStyleSheet(qss_style)

label.show()

sys.exit(app.exec())
