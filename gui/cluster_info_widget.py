from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt



class ClusterInfoWidget(QWidget):
    def __init__(self, cluster_id, color, parent=None):
        super().__init__(parent)
        self.cluster_id = cluster_id
        self.color = color
        self.initUI()
        self.mousePressEvent = self.closeEvent

    def initUI(self):
        self.setStyleSheet(
            f'background-color: lightgrey; border: 10px solid {self.color}; padding: 30px; border-radius: 20px;')

        layout = QVBoxLayout()

        header_layout = QHBoxLayout()
        close_button = QPushButton("X")
        close_button.clicked.connect(self.close)
        close_button.setStyleSheet(
            "background-color: red; color: white; font-weight: bold; border: none; padding: 15px;")
        header_layout.addWidget(close_button, alignment=Qt.AlignRight)

        layout.addLayout(header_layout)

        self.label = QLabel(f'Cluster ID: {self.cluster_id}', self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle("Cluster Info")

    def closeEvent(self, event):
        from gui.quad_widget import QuadWidget

        # Ensure the parent widget is an instance of QuadWidget
        if isinstance(self.parent(), QuadWidget):
            self.parent().show_quad(1)
        else:
            super().closeEvent(event)
