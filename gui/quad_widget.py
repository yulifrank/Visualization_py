from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QPushButton
from PyQt5.QtCore import Qt
from gui.cluster_info_widget import ClusterInfoWidget
from gui.cluster_widget import ClusterWidget  # Ensure you import this to avoid circular imports

class QuadWidget(QWidget):
    def __init__(self, quad, is_right_side=True, parent=None):
        super().__init__(parent)
        self.quad = quad
        self.is_right_side = is_right_side
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
        self.grid_layout.addWidget(self.label_quad, 1, 1)

        # Add HBM labels
        self.add_hbm()

        # Set stretch factors for the columns and rows
        self.grid_layout.setColumnStretch(0, 1)
        self.grid_layout.setColumnStretch(1, 2)
        self.grid_layout.setColumnStretch(2, 1)
        self.grid_layout.setRowStretch(0, 1)
        self.grid_layout.setRowStretch(1, 1)
        self.grid_layout.setRowStretch(2, 1)

        # Set initial size for the widget
        self.setMinimumSize(500, 500)  # Set this to the desired size

        # Set border style and color based on enable status
        self.update_style()

    def update_style(self):
        self.setStyleSheet(f'background-color: lightgrey; border: 2px dashed {"green" if self.quad.is_enable else "lightgrey"};')
        self.setEnabled(self.quad.is_enable)

    def add_hbm(self):
        self.label_hbm = QLabel("hbm " + self.quad.hbm.type_name, self)
        self.label_hbm.setAlignment(Qt.AlignCenter)

        if self.quad.id in [1, 3]:
            # Display HBM on the right side for quads 1 and 3
            self.grid_layout.addWidget(self.label_hbm, 1, 2)
        else:
            # Display HBM on the left side for quads 2 and 4
            self.grid_layout.addWidget(self.label_hbm, 1, 0)

    def mousePressEvent(self, event):
        if not self.is_hbm(event.pos()):
            self.show_clusters()

    def is_hbm(self, pos):
        return self.label_hbm.geometry().contains(pos)

    def show_clusters(self, event=None):
        # Hide the Quad label
        if self.label_quad:
            self.label_quad.hide()

        # Remove old cluster layout if it exists
        if hasattr(self, 'cluster_layout'):
            while self.cluster_layout.count():
                item = self.cluster_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

        self.cluster_layout = QGridLayout()
        self.cluster_layout.setSpacing(0)
        self.grid_layout.addLayout(self.cluster_layout, 1, 1, 1, 1)  # Re-add to the grid layout, same row, full width

        for row in self.quad.clusters:
            for cluster in row:
                if cluster is not None:
                    cluster_widget = ClusterWidget(cluster, self)
                    self.cluster_layout.addWidget(cluster_widget, cluster.row, cluster.col)

        back_button = QPushButton("Back To " + self.quad.name)
        back_button.clicked.connect(self.show_quad)
        self.cluster_layout.addWidget(back_button, 8, 0, 1, 8)  # Adding the back button at the bottom

        self.adjustSize()

    def show_cluster_info(self, cluster):
        self.clear_layout()
        cluster_info_widget = ClusterInfoWidget(cluster.id, cluster.color, self)
        self.layout.addWidget(cluster_info_widget)

    def show_quad(self, init=0):
        self.clear_layout()  # Ensure layout is cleared before resetting

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        # Re-add Quad label
        self.label_quad = QLabel(self.quad.name, self)
        self.label_quad.setAlignment(Qt.AlignCenter)
        self.grid_layout.addWidget(self.label_quad, 1, 1)

        # Re-add HBM label
        self.add_hbm()

        # Set stretch factors for the columns and rows
        self.grid_layout.setColumnStretch(0, 1)
        self.grid_layout.setColumnStretch(1, 2)
        self.grid_layout.setColumnStretch(2, 1)
        self.grid_layout.setRowStretch(0, 1)
        self.grid_layout.setRowStretch(1, 1)
        self.grid_layout.setRowStretch(2, 1)

        # Update widget style
        self.update_style()

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
