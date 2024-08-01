from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
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

        # Host Interface Label
        self.host_label = QLabel('Host Interface', self)
        self.host_label.setAlignment(Qt.AlignCenter)
        self.host_label.setStyleSheet('background-color: lightgrey; border: 1px dashed black; padding: 5px;')
        self.host_label.setFixedHeight(50)
        self.layout.addWidget(self.host_label)

        # Layout for DIE buttons
        self.button_layout = QHBoxLayout()
        self.die1_button = QPushButton("GO TO DIE1", self)
        self.die1_button.clicked.connect(self.show_die1)
        self.die2_button = QPushButton("GO TO DIE2", self)
        self.die2_button.clicked.connect(self.show_die2)
        self.button_layout.addWidget(self.die1_button)
        self.button_layout.addWidget(self.die2_button)
        self.layout.addLayout(self.button_layout)

        # Create and hide DieWidget initially
        self.die_widget = DieWidget(self.data_manager)
        self.die_widget.setVisible(False)
        self.layout.addWidget(self.die_widget)

    def show_die1(self):
        print("Showing DIE1")  # Debug print
        self.die1_button.hide()
        self.die2_button.show()
        self.die_widget.setVisible(True)
        self.die_widget.show_quads(0)  # Show DIE1 quads

    def show_die2(self):
        print("Showing DIE2")  # Debug print
        self.die2_button.hide()
        self.die1_button.show()
        self.die_widget.setVisible(True)
        self.die_widget.show_quads(1)  # Show DIE2 quads
