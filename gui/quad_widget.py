# quad_widget.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
from gui.cluster_info_widget import ClusterInfoWidget
from gui.cluster_widget import ClusterWidget

class QuadWidget(QWidget):
    def __init__(self, quad, position, parent=None):
        super().__init__(parent)
        self.quad = quad
        self.position = position
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        # Add Quad label
        self.label_quad = QLabel(self.quad.name, self)
        self.label_quad.setAlignment(Qt.AlignCenter)
        self.grid_layout.addWidget(self.label_quad, 0, 0)

        self.setStyleSheet('border: 2px dashed black;')
        color = "green" if self.quad.is_enable else "lightgrey"
        self.setStyleSheet(f'background-color: lightgrey; border: 2px dashed {color};')
        self.setEnabled(self.quad.is_enable)

    def mousePressEvent(self, event):
        if not self.is_hbm(event.pos()):
            self.show_clusters()

    def is_hbm(self, pos):
        return False  # No HBM handling here anymore

    def show_clusters(self, event=None):
        if self.label_quad:
            self.label_quad.hide()

        if hasattr(self, 'cluster_layout'):
            while self.cluster_layout.count():
                item = self.cluster_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

        self.cluster_layout = QGridLayout()
        self.cluster_layout.setSpacing(0)
        self.grid_layout.addLayout(self.cluster_layout, 0, 0, 1, 1)

        for row in self.quad.clusters:
            for cluster in row:
                if cluster is not None:
                    cluster_widget = ClusterWidget(cluster, self)
                    self.cluster_layout.addWidget(cluster_widget, cluster.row, cluster.col)

        back_button = QPushButton("Back To " + self.quad.name)
        back_button.clicked.connect(self.show_quad)
        self.cluster_layout.addWidget(back_button, 8, 0, 1, 8)

        self.adjustSize()

    def show_cluster_info(self, cluster):
        self.clear_layout()
        cluster_info_widget = ClusterInfoWidget(cluster.id, cluster.color, self)
        self.layout.addWidget(cluster_info_widget)

    def show_quad(self, init=0):
        self.setStyleSheet('border: 2px dashed black;')
        color = "green" if self.quad.is_enable else "lightgrey"
        self.setStyleSheet(f'background-color: lightgrey; border: 2px dashed {color};')
        self.clear_layout()

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        self.label_quad = QLabel(self.quad.name, self)
        self.label_quad.setAlignment(Qt.AlignCenter)
        self.grid_layout.addWidget(self.label_quad, 0, 0)

        self.grid_layout.setColumnStretch(0, 3)

        self.adjustSize()
        if init:
            self.show_clusters()

    def clear_layout(self, layout=None):
        if layout is None:
            layout = self.layout

        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            elif item.layout():
                self.clear_layout(item.layout())

        layout.update()
