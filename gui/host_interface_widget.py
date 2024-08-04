from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
from component import Component
from constants import CLASTER_COLORS  # import constants

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

        # Create a button to toggle content visibility
        self.toggle_button = QPushButton("Show Details", self)
        self.toggle_button.clicked.connect(self.toggle_content)
        self.frame_layout.addWidget(self.toggle_button)

        # Create a button to close all details
        self.close_all_button = QPushButton("Close All Details", self)
        self.close_all_button.clicked.connect(self.close_all_details)
        self.frame_layout.addWidget(self.close_all_button)

        # Create a widget to contain the dynamic sections
        self.sections_widget = QWidget()
        self.sections_layout = QHBoxLayout()

        # Function to create a label for the "PCIe" and "BMT" sections
        def create_section_label(title, color, data):
            if not data or (isinstance(data, dict) and not data) or (isinstance(data, list) and not data):
                return None  # Skip creating a label if data is empty
            label = QLabel(f"{title}: {data}")
            label.setStyleSheet(
                f'background-color: {color}; border: 2px solid black; border-radius: 10px; padding: 5px; margin: 5px;'
            )
            label.setFixedSize(150, 50)  # Set a fixed size for the label
            return label

        # Function to create a button for the "H2G" and "G2H" sections
        def create_section_button(title, color, data):
            if not data or (isinstance(data, dict) and not data) or (isinstance(data, list) and not data):
                return None  # Skip creating a button if data is empty
            button = QPushButton(title)
            button.setStyleSheet(
                f'background-color: {color}; border: 2px solid black; border-radius: 10px; padding: 5px; margin: 5px;'
            )
            button.setFixedSize(150, 50)  # Set a fixed size for the button
            button.clicked.connect(lambda: self.show_details(title, data))
            return button

        # Generate sections dynamically based on host_interface data
        data_sections = {
            "BMT": self.host_interface.get_bmt(),
            "H2G": self.host_interface.get_h2g(),
            "G2H": self.host_interface.get_g2h(),
            "PCIe": self.host_interface.get_pcie()
        }

        for section_name, section_data in data_sections.items():
            color = CLASTER_COLORS.get(section_name, 'gray')  # Default color

            if section_name in ["BMT", "PCIe"]:
                section_label = create_section_label(section_name, color, section_data)
                if section_label:
                    self.sections_layout.addWidget(section_label)
            else:
                section_button = create_section_button(section_name, color, section_data)
                if section_button:
                    self.sections_layout.addWidget(section_button)

        self.sections_widget.setLayout(self.sections_layout)
        self.sections_widget.setVisible(False)

        # Add widget sections to the frame layout
        self.frame_layout.addWidget(self.sections_widget)
        self.outer_frame.setLayout(self.frame_layout)

        # Add the outer frame to the main layout
        self.main_layout.addWidget(self.outer_frame)
        self.setLayout(self.main_layout)

    def show_details(self, title, data):
        # Prepare details to display
        detail_frame = QFrame()
        detail_frame.setFrameShape(QFrame.StyledPanel)
        detail_layout = QGridLayout(detail_frame)

        if not data:
            detail_layout.addWidget(QLabel("No details to show"), 0, 0)
        elif isinstance(data, Component):
            if not data.name:  # Assuming name is an attribute that should be present
                detail_layout.addWidget(QLabel("No details to show"), 0, 0)
            else:
                detail_layout.addWidget(QLabel(f"Component ID: {data.id}, Component Name: {data.name}"), 0, 0)
        elif isinstance(data, dict):
            if not data:
                detail_layout.addWidget(QLabel("No details to show"), 0, 0)
            else:
                for i, (key, value) in enumerate(data.items()):
                    detail_layout.addWidget(QLabel(f"{key}: {value}"), i // 5, i % 5)  # Display 5 items per row
        elif isinstance(data, list):
            if not data:
                detail_layout.addWidget(QLabel("No details to show"), 0, 0)
            else:
                for i, item in enumerate(data):
                    detail_layout.addWidget(QLabel(f"Item: {item}"), i // 5, i % 5)  # Display 5 items per row

        # Close button for the detail frame
        close_button = QPushButton("Close")
        close_button.clicked.connect(detail_frame.hide)  # Hide the frame when clicked
        detail_layout.addWidget(close_button, (i // 5) + 1, 0, 1, 5)  # Place close button in the next row

        self.frame_layout.addWidget(detail_frame)

    def toggle_content(self):
        if self.sections_widget.isVisible():
            self.sections_widget.setVisible(False)
            self.toggle_button.setText("Show Details")
        else:
            self.sections_widget.setVisible(True)
            self.toggle_button.setText("Hide Details")

    def close_all_details(self):
        # Iterate over all widgets in the frame layout and hide detail frames
        for i in range(self.frame_layout.count()):
            widget = self.frame_layout.itemAt(i).widget()
            if isinstance(widget, QFrame):
                widget.hide()
