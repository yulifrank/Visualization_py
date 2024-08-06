from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
# הייבוא של ClusterInfoWidget נשאר כאן
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
        text_color=text_color if self.cluster.is_enable else "lightgrey"
        self.label.setStyleSheet(f'color: {text_color }; font-size: 16px;')
        layout.addWidget(self.label)
        self.setStyleSheet(f'background-color: lightgrey; border:  2px dashed {text_color};')

        self.setEnabled(self.cluster.is_enable)
        self.mousePressEvent = self.show_cluster_info

    def show_cluster_info(self, event):
        from gui.quad_widget import QuadWidget  # ייבוא כאן כדי למנוע מעגליות
        parent_widget = self.parent()
        while parent_widget and not isinstance(parent_widget, QuadWidget):
            parent_widget = parent_widget.parent()
        if parent_widget:
            parent_widget.show_cluster_info(self.cluster)
