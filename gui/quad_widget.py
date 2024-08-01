
from PyQt5.QtWidgets import  QWidget, QGridLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from gui.cluster_widget import ClusterWidget


class QuadWidget(QWidget):
    def __init__(self, quad, parent=None):
        super().__init__(parent)
        self.quad = quad
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label = QLabel(self.quad.name, self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.setStyleSheet('border: 2px dashed red;')
        self.mousePressEvent = self.show_clusters

    def show_clusters(self, event):
        for i in reversed(range(self.layout().count())):
            widget = self.layout().itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        cluster_layout = QGridLayout()
        cluster_layout.setSpacing(0)
        self.layout().addLayout(cluster_layout)
        for row in self.quad.clusters:
            for cluster in row:
                cluster_widget = ClusterWidget(cluster, self)
                cluster_layout.addWidget(cluster_widget, cluster.row, cluster.col)

        # Adjust the size of the QuadWidget to fit the clusters
        self.adjustSize()
