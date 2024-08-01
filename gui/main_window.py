
import json
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QVBoxLayout, QLabel, QHBoxLayout, QScrollArea
from PyQt5.QtCore import Qt

from ויזואליזציה.die import Die
from ויזואליזציה.gui.quad_widget import QuadWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
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

        # Layout for navigation buttons
        self.button_layout = QHBoxLayout()
        self.prev_button = QPushButton("Previous DIE", self)
        self.prev_button.clicked.connect(self.show_previous_die)
        self.next_button = QPushButton("Next DIE", self)
        self.next_button.clicked.connect(self.show_next_die)
        self.button_layout.addWidget(self.prev_button)
        self.button_layout.addWidget(self.next_button)
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

        # Initially show quads for DIE1
        self.show_quads(self.die_index)

    def show_quads(self, die_index):
        with open('chip_data.json', 'r') as config:
            data = json.load(config)
        die_json = data.get("DIES", [])[die_index]
        die = Die(die_index, die_json)

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

    def show_previous_die(self):
        self.die_index = max(0, self.die_index - 1)
        self.show_quads(self.die_index)

    def show_next_die(self):
        with open('../chip_data.json', 'r') as config:
            data = json.load(config)
        total_dies = len(data.get("DIES", []))
        self.die_index = min(total_dies - 1, self.die_index + 1)
        self.show_quads(self.die_index)
