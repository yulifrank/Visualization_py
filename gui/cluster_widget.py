from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel

from gui.cluster_info_widget import ClusterInfoWidget


class ClusterWidget(QWidget):
    def __init__(self, cluster, parent=None):
        super().__init__(parent)
        self.cluster = cluster
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        color = QColor(self.cluster.color)
        text_color = color.name()
        self.label = QLabel(f'{self.cluster.type_name}\nCluster {self.cluster.id}', self)

        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet(f'color: {text_color};')
        layout.addWidget(self.label)
        self.setStyleSheet(f'background-color: lightgrey; border: 2px dashed {text_color}; ')

        self.mousePressEvent = self.show_cluster_info

    def show_cluster_info(self, event):
        if hasattr(self.parent(), 'info_widget'):
            self.parent().info_widget.deleteLater()
        self.parent().info_widget = ClusterInfoWidget(self.cluster.id, self.cluster.color, self.parent())
        self.parent().info_widget.show()
