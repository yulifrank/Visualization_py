from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QScrollArea
import qtawesome as qta
from gui.die_widget import DieWidget
from gui.host_interface_widget import HostInterfaceWidget

class MainWindow(QWidget):
    def __init__(self, data_manager):
        super().__init__()
        self.data_manager = data_manager
        self.die_widget = None
        self.host_interface_widget = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Quad Matrix')
        self.setGeometry(100, 100, 800, 600)

        # Main layout for the window
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # Create a scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Create a container widget for all content inside the scroll area
        self.scroll_content_widget = QWidget()
        self.scroll_content_layout = QVBoxLayout(self.scroll_content_widget)
        self.scroll_content_layout.setContentsMargins(0, 0, 0, 0)

        # Add the container widget to the scroll area
        self.scroll_area.setWidget(self.scroll_content_widget)
        self.main_layout.addWidget(self.scroll_area)

        # Create HostInterfaceWidget and add to scroll content layout
        host_interface_data = self.data_manager.load_host_interface()
        self.host_interface_widget = HostInterfaceWidget(host_interface_data, self)
        self.scroll_content_layout.addWidget(self.host_interface_widget)

        # Layout for DIE buttons
        self.button_layout = QVBoxLayout()

        # Add icons to buttons using QtAwesome
        die_icon = qta.icon('fa5s.folder-open')

        self.die1_button = QPushButton("GO TO DIE1", self)
        self.die1_button.setIcon(die_icon)
        self.die1_button.clicked.connect(self.show_die1)

        self.die2_button = QPushButton("GO TO DIE2", self)
        self.die2_button.setIcon(die_icon)
        self.die2_button.clicked.connect(self.show_die2)

        self.die2die_button = QPushButton("DIE TO DIE", self)
        # Connect the die2die_button to an empty slot for now
        self.die2die_button.clicked.connect(self.show_die2die)

        # Add buttons to the layout in the desired order
        self.button_layout.addWidget(self.die1_button)
        self.button_layout.addWidget(self.die2die_button)  # Place this button between the other two
        self.button_layout.addWidget(self.die2_button)

        self.scroll_content_layout.addLayout(self.button_layout)

        # Create and hide DieWidget initially
        self.die_widget = DieWidget(self.data_manager, self)
        self.die_widget.setVisible(False)
        self.scroll_content_layout.addWidget(self.die_widget)

        # Apply the stylesheet from the file
        self.apply_stylesheet()

    def apply_stylesheet(self):
        with open("gui/styles.css", 'r', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

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

    def show_die2die(self):
        print("Showing DIE2DIE")  # Debug print
        # Implement functionality for DIE2DIE if needed
        pass
    def show_die_buttons(self):
        print("Showing DIE Buttons")  # Debug print
        self.die1_button.show()
        self.die2_button.show()
        self.die_widget.setVisible(False)