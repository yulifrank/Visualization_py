from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

from gui.cluster_info_widget import ClusterInfoWidget


# הסרת הייבוא של ClusterWidget כאן כדי למנוע מעגליות
# נייבא את ClusterWidget רק כשנשתמש בו
class QuadWidget(QWidget):
    def __init__(self, quad, parent=None):
        super().__init__(parent)
        self.quad = quad
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.label = QLabel(self.quad.name, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)
        self.setStyleSheet('border: 2px dashed red;')
        self.mousePressEvent = self.show_clusters

    def show_clusters(self, event=None):
        from gui.cluster_widget import ClusterWidget  # ייבוא כאן כדי למנוע מעגליות
        self.clear_layout()

        cluster_layout = QGridLayout()
        cluster_layout.setSpacing(0)
        self.layout.addLayout(cluster_layout)

        for row in self.quad.clusters:
            for cluster in row:
                if cluster is not None:
                    cluster_widget = ClusterWidget(cluster, self)
                    cluster_layout.addWidget(cluster_widget, cluster.row, cluster.col)

        back_button = QPushButton("Back")
        back_button.clicked.connect(self.show_quad)
        cluster_layout.addWidget(back_button, 8, 0, 1, 8)  # Adding the back button at the bottom

        self.adjustSize()

    def show_cluster_info(self, cluster):
        self.clear_layout()

        cluster_info_widget = ClusterInfoWidget(cluster.id, cluster.color, self)
        self.layout.addWidget(cluster_info_widget)

        back_button = QPushButton("Back")
        back_button.clicked.connect(self.show_clusters)
        self.layout.addWidget(back_button)

    def show_quad(self):
        self.clear_layout()

        self.label = QLabel(self.quad.name, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.setStyleSheet('border: 2px dashed red;')
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
