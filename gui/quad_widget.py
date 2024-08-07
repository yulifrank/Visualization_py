from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QPushButton
from PyQt5.QtCore import Qt

class QuadWidget(QWidget):
    def __init__(self, quad, parent=None):
        super().__init__(parent)
        self.quad = quad
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()  # Use horizontal layout
        self.layout.setSpacing(5)  # Reduced spacing
        self.layout.setContentsMargins(5, 5, 5, 5)  # Add small margins
        self.setLayout(self.layout)

        # Create a vertical layout for the quad
        self.quad_layout = QVBoxLayout()
        self.quad_label = QLabel(self.quad.name, self)
        self.quad_label.setAlignment(Qt.AlignCenter)
        self.quad_layout.addWidget(self.quad_label)

        color = "green" if self.quad.is_enable else "lightgrey"
        self.setStyleSheet(f'background-color: lightgrey; border: 2px dashed {color};')
        self.setEnabled(self.quad.is_enable)

        # Add quad info to layout
        self.layout.addLayout(self.quad_layout)

        # Add hbm info
        if self.quad.hbm:
            self.hbm_widget = QLabel(f"HBM: {self.quad.hbm}", self)  # Display HBM information
            self.hbm_widget.setAlignment(Qt.AlignCenter)
            self.hbm_widget.setStyleSheet('background-color: lightblue; border: 1px solid black;')
            # Set fixed size for hbm widget
            self.hbm_widget.setFixedSize(100, 600)
            self.layout.addWidget(self.hbm_widget)

        # Set fixed size for quad widget to be twice the size of the hbm widget
        if self.quad.hbm:
            self.setFixedSize(self.hbm_widget.width() * 2, self.hbm_widget.height() * 2)

        self.mousePressEvent = self.show_clusters

    def show_clusters(self, event=None):
        from gui.cluster_widget import ClusterWidget  # Import to avoid circular import
        self.clear_layout()

        cluster_layout = QGridLayout()
        cluster_layout.setSpacing(0)  # Reduced spacing
        self.layout.addLayout(cluster_layout)

        for row in self.quad.clusters:
            for cluster in row:
                if cluster is not None:
                    cluster_widget = ClusterWidget(cluster, self)
                    cluster_layout.addWidget(cluster_widget, cluster.row, cluster.col)

        back_button = QPushButton("Back To " + self.quad.name)
        back_button.clicked.connect(self.show_quad)
        cluster_layout.addWidget(back_button, 8, 0, 1, 8)  # Adding the back button at the bottom

        self.adjustSize()

    def show_cluster_info(self, cluster):
        self.clear_layout()

        from gui.cluster_info_widget import ClusterInfoWidget
        cluster_info_widget = ClusterInfoWidget(cluster.id, cluster.color, self)
        self.layout.addWidget(cluster_info_widget)

        back_button = QPushButton("Back To clusters")
        back_button.clicked.connect(self.show_clusters)
        self.layout.addWidget(back_button)

    def show_quad(self):
        self.clear_layout()

        self.quad_label = QLabel(self.quad.name, self)
        self.quad_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.quad_label)

        self.mousePressEvent = self.show_clusters
        self.adjustSize()

    def clear_layout(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                while item.layout().count():
                    sub_item = item.layout().takeAt(0)
                    sub_widget = sub_item.widget()
                    if sub_widget is not None:
                        sub_widget.deleteLater()
                    elif sub_item.layout() is not None:
                        while sub_item.layout().count():
                            sub_sub_item = sub_item.layout().takeAt(0)
                            sub_sub_widget = sub_sub_item.widget()
                            if sub_sub_widget is not None:
                                sub_sub_widget.deleteLater()
                        item.layout().removeItem(sub_item)
