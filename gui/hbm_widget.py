# hbm_widget.py
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class HBMWidget(QWidget):
    def __init__(self, hbm, parent=None):
        super().__init__(parent)
        self.hbm = hbm
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label_hbm = QLabel(f"HBM: {self.hbm.type_name}", self)
        self.label_hbm.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_hbm)

        self.setStyleSheet('border: 1px solid black;')
        self.setFixedSize(100, 150)  # Default size, will be adjusted in DieWidget

    def setFixedSize(self, width, height):
        super().setFixedSize(width, height)
