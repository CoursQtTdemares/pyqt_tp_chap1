import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

label = QLabel()
label.setTextFormat(Qt.TextFormat.RichText)
label.setText("<b>Hello</b>, <i>PyQt6</i>!")

with open("style.qss", "r", encoding="utf-8") as file:
    qss_style = file.read()
    app.setStyleSheet(qss_style)

label.show()

sys.exit(app.exec())
