import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


class ClusterInfoWidget(QWidget):
    def __init__(self, cluster_id, color, parent=None):
        super().__init__(parent)
        self.cluster_id = cluster_id
        self.color = color
        self.initUI()

    def initUI(self):
        self.setStyleSheet(
            f'background-color: lightgrey; border: 10px solid {self.color}; padding: 30px; border-radius: 10px;')
        self.label = QLabel(f'Cluster ID: {self.cluster_id}', self)
        self.label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.addWidget(self.label)


        self.setLayout(layout)
        self.setWindowState(Qt.WindowMaximized)  # Fullscreen mode