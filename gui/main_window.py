# main_window.py
import json

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QScrollArea, QGridLayout
from PyQt5.QtCore import Qt
from gui.quad_widget import QuadWidget
class MainWindow(QWidget):
    def __init__(self, data_manager):
        super().__init__()
        self.data_manager = data_manager
        self.die1 = None
        self.die2 = None
        self.die_index = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Quad Matrix')
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Host Interface Label
        self.host_label = QLabel('Host Interface', self)
        self.host_label.setAlignment(Qt.AlignCenter)
        self.host_label.setStyleSheet('background-color: lightgrey; border: 1px dashed black; padding: 5px;')
        self.host_label.setFixedHeight(50)
        self.layout.addWidget(self.host_label)

        # Layout for DIE buttons
        self.button_layout = QHBoxLayout()
        self.die1_button = QPushButton("DIE1", self)
        self.die1_button.clicked.connect(self.show_die1)
        self.die2_button = QPushButton("DIE2", self)
        self.die2_button.clicked.connect(self.show_die2)
        self.button_layout.addWidget(self.die1_button)
        self.button_layout.addWidget(self.die2_button)
        self.layout.addLayout(self.button_layout)

        # Scroll area for Quad Matrix
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_area.setWidget(self.scroll_content)
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.quad_layout = QGridLayout()
        self.quad_layout.setSpacing(10)
        self.quad_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.addLayout(self.quad_layout)
        self.layout.addWidget(self.scroll_area)

        # Initially load and show quads for DIE1
        self.load_dies()
        self.show_quads(self.die_index)

    def load_dies(self):
        self.die1 = self.data_manager.load_die(0)
        self.die2 = self.data_manager.load_die(1)

    def show_quads(self, die_index):
        die = self.die1 if die_index == 0 else self.die2

        # Clear previous widgets from the quad layout
        for i in reversed(range(self.quad_layout.count())):
            widget = self.quad_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Display new matrix of 4 quads
        for i in range(2):
            for j in range(2):
                quad = die.quads[i][j]
                if quad:
                    quad_widget = QuadWidget(quad, self)
                else:
                    quad_widget = QLabel('Empty', self)
                    quad_widget.setAlignment(Qt.AlignCenter)
                    quad_widget.setStyleSheet('border: 1px dashed black; min-width: 300px; min-height: 300px;')
                self.quad_layout.addWidget(quad_widget, i, j, alignment=Qt.AlignCenter)

        self.adjust_quad_sizes()

    def adjust_quad_sizes(self):
        # Adjust the size of the QuadWidgets to fill the area evenly
        size = self.size().width() // 2 - 40  # Adjust size as needed
        for i in range(2):
            for j in range(2):
                quad_widget = self.quad_layout.itemAt(i * 2 + j).widget()
                if quad_widget:
                    quad_widget.setFixedSize(size, size)

    def resizeEvent(self, event):
        self.adjust_quad_sizes()
        super().resizeEvent(event)

    def show_die1(self):

        self.die_index = 0
        self.die1_button.hide()
        self.die2_button.show()

        self.show_quads(self.die_index)

    def show_die2(self):
        with open('chip_data.json', 'r') as config:
            data = json.load(config)
        total_dies = len(data.get("DIES", []))
        self.die_index = min(1, total_dies - 1)  # Adjust to ensure index does not exceed bounds
        self.die2_button.hide()
        self.die1_button.show()
        self.show_quads(self.die_index)
        if self.die_index != 0:
            self.die_index = 0
            self.show_quads(self.die_index)

    def show_die2(self):
        if self.die_index != 1:
            self.die_index = 1
            self.show_quads(self.die_index)
