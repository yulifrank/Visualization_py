import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QLabel, QHBoxLayout, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from die import Die
from ויזואליזציה.gui.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())