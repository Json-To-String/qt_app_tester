#some_component.py
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class SomeComponent(QWidget):

    def __init__(self):
        super().__init__()
        self.button = QPushButton("Some Component's Button")
        self.button.setFont(QFont('Arial', 14))
        self.button.clicked.connect(lambda: self.text_label.setText("Changed!"))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SomeComponent()
    ex.show()
    sys.exit(app.exec_())
