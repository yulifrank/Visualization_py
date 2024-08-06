from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QFrame, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from gui.section_data_handler import SectionDataHandler
from gui.section_widget import SectionWidget

class HostInterfaceWidget(QWidget):
    def __init__(self, host_interface, parent=None):
        super().__init__(parent)
        self.host_interface = host_interface
        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout()

        self.outer_frame = QFrame()
        self.outer_frame.setFrameShape(QFrame.StyledPanel)
        self.outer_frame.setFrameShadow(QFrame.Raised)

        self.title_label = QLabel("<b>HostInterface</b>")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet('border-bottom: 2px solid black; padding-bottom: 5px; margin-bottom: 10px;')

        self.frame_layout = QVBoxLayout()
        self.frame_layout.addWidget(self.title_label)

        self.button_layout = QHBoxLayout()
        self.toggle_button = QPushButton("Show Details", self)
        self.toggle_button.clicked.connect(self.toggle_content)
        self.button_layout.addWidget(self.toggle_button)

        self.frame_layout.addLayout(self.button_layout)

        self.sections_widget = SectionWidget(self.host_interface)
        self.sections_widget.setVisible(False)
        self.frame_layout.addWidget(self.sections_widget)

        self.outer_frame.setLayout(self.frame_layout)

        self.extra_buttons_layout = QHBoxLayout()

        self.h2g_button = QPushButton("H2G")
        self.h2g_button.setFixedSize(200, 70)
        self.h2g_button.setStyleSheet(
            'background-color: lightcoral; border: 2px solid black; border-radius: 7px; padding: 10px; margin: 10px;'
        )
        self.h2g_button.clicked.connect(lambda: self.show_details('H2G'))
        self.extra_buttons_layout.addWidget(self.h2g_button)

        self.g2h_button = QPushButton("G2H")
        self.g2h_button.setFixedSize(200, 70)
        self.g2h_button.setStyleSheet(
            'background-color: lightgreen; border: 2px solid black; border-radius: 7px; padding: 10px; margin: 10px;'
        )
        self.g2h_button.clicked.connect(lambda: self.show_details('G2H'))
        self.extra_buttons_layout.addWidget(self.g2h_button)

        self.extra_buttons_widget = QWidget()
        self.extra_buttons_widget.setLayout(self.extra_buttons_layout)
        self.extra_buttons_widget.setVisible(False)  # Initially hide the extra buttons

        self.section_data_handler = SectionDataHandler(self.host_interface)
        self.main_layout.addWidget(self.outer_frame)
        self.main_layout.addWidget(self.extra_buttons_widget)
        self.main_layout.addWidget(self.section_data_handler)  # Add SectionDataHandler to the layout

        self.setLayout(self.main_layout)

    def toggle_content(self):
        is_visible = self.sections_widget.isVisible()
        self.sections_widget.setVisible(not is_visible)
        self.extra_buttons_widget.setVisible(not is_visible)  # Toggle the visibility of the extra buttons
        self.toggle_button.setText("Hide Details" if not is_visible else "Show Details")

    def show_details(self, section_name):
        self.section_data_handler.display_section_data(section_name)
