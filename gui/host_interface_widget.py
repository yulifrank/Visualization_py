from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QLabel
from PyQt5.QtCore import Qt
from gui.section_widget import SectionWidget

class HostInterfaceWidget(QWidget):
    def __init__(self, host_interface, parent=None):
        super().__init__(parent)
        self.host_interface = host_interface
        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout()

        # Create a frame for the entire panel with a title
        self.outer_frame = QFrame()
        self.outer_frame.setFrameShape(QFrame.StyledPanel)
        self.outer_frame.setFrameShadow(QFrame.Raised)

        # Create a title for the frame
        self.title_label = QLabel("<b>HostInterface</b>")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet('border-bottom: 2px solid black; padding-bottom: 5px; margin-bottom: 10px;')

        # Create a layout for the frame
        self.frame_layout = QVBoxLayout()
        self.frame_layout.addWidget(self.title_label)

        # Create a horizontal layout for the buttons
        self.button_layout = QHBoxLayout()

        # Create a button to toggle content visibility
        self.toggle_button = QPushButton("Show Details", self)
        self.toggle_button.clicked.connect(self.toggle_content)
        self.button_layout.addWidget(self.toggle_button)

        # Add the button layout to the frame layout
        self.frame_layout.addLayout(self.button_layout)

        # Create a widget to contain the dynamic sections
        self.sections_widget = SectionWidget(self.host_interface)
        self.sections_widget.setVisible(False)

        # Add widget sections to the frame layout
        self.frame_layout.addWidget(self.sections_widget)
        self.outer_frame.setLayout(self.frame_layout)

        # Add the outer frame to the main layout
        self.main_layout.addWidget(self.outer_frame)
        self.setLayout(self.main_layout)

    def toggle_content(self):
        if self.sections_widget.isVisible():
            self.sections_widget.setVisible(False)
            self.toggle_button.setText("Show Details")
        else:
            self.sections_widget.setVisible(True)
            self.toggle_button.setText("Hide Details")
