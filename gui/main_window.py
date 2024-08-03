import os
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QApplication
from PyQt5.QtCore import Qt
import qtawesome as qta
from gui.die_widget import DieWidget  # Import the DieWidget class

class MainWindow(QWidget):
    def __init__(self, data_manager):
        super().__init__()
        self.data_manager = data_manager
        self.die_widget = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Quad Matrix')
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Load external stylesheet
        style_path = os.path.join(os.path.dirname(__file__), 'styles.css')
        with open(style_path, 'r', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

        # Host Interface Label
        self.host_label = QLabel('Host Interface', self)
        self.host_label.setAlignment(Qt.AlignCenter)
        self.host_label.setStyleSheet('background-color: lightgrey; border: 1px dashed black; padding: 5px;')
        self.host_label.setFixedHeight(50)
        self.layout.addWidget(self.host_label)

        # Layout for DIE buttons
        self.button_layout = QHBoxLayout()

        # Add icons to buttons using QtAwesome
        die1_icon = die2_icon = qta.icon('fa5s.folder-open')

        self.die1_button = QPushButton("GO TO DIE1", self)
        self.die1_button.setIcon(die1_icon)
        self.die1_button.clicked.connect(self.show_die1)

        self.die2_button = QPushButton("GO TO DIE2", self)
        self.die2_button.setIcon(die2_icon)
        self.die2_button.clicked.connect(self.show_die2)

        self.button_layout.addWidget(self.die1_button)
        self.button_layout.addWidget(self.die2_button)
        self.layout.addLayout(self.button_layout)

        # Create and hide DieWidget initially
        self.die_widget = DieWidget(self.data_manager, self)
        self.die_widget.setVisible(False)
        self.layout.addWidget(self.die_widget)

    def show_die1(self):
        print("Showing DIE1")  # Debug print
        self.die1_button.hide()
        self.die2_button.hide()
        self.die_widget.setVisible(True)
        self.die_widget.show_quads(0)  # Show DIE1 quads

    def show_die2(self):
        print("Showing DIE2")  # Debug print
        self.die1_button.hide()
        self.die2_button.hide()
        self.die_widget.setVisible(True)
        self.die_widget.show_quads(1)  # Show DIE2 quads

    def show_die_buttons(self):
        self.die1_button.show()
        self.die2_button.show()
        self.die_widget.setVisible(False)

