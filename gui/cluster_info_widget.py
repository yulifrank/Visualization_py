import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class ClusterInfoWidget(QWidget):
    def __init__(self, cluster_id, color, parent=None):
        super().__init__(parent)
        self.cluster_id = cluster_id
        self.color = color
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'background-color: lightgrey; border: 10px solid {self.color}; padding: 30px;')
        self.label = QLabel(f'Cluster ID: {self.cluster_id}', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.label)
        self.setFixedSize(500, 500)

        back_button = QPushButton("Back")
        back_button.clicked.connect(self.close)
        self.layout().addWidget(back_button)




