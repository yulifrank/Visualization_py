import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QLabel, QHBoxLayout, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class ClusterInfoWidget(QWidget):
    def __init__(self, cluster_id, color, parent=None):
        super().__init__(parent)
        self.cluster_id = cluster_id
        self.color = color
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'background-color: lightgrey; border: 3px dashed {self.color}; padding: 5px;')
        self.label = QLabel(f'Cluster ID: {self.cluster_id}', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.label)
        self.setFixedSize(300, 300)
