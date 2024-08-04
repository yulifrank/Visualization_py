from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt
from constants import CLASTER_COLORS  # ייבוא קבועים

class HostInterfaceWidget(QWidget):
    def __init__(self, host_interface, parent=None):
        super().__init__(parent)
        self.host_interface = host_interface
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()  # Use vertical layout for the main widget

        # Create a frame for the whole panel with a title
        outer_frame = QFrame()
        outer_frame.setFrameShape(QFrame.StyledPanel)
        outer_frame.setFrameShadow(QFrame.Raised)

        # Create a title for the frame
        title_label = QLabel("<b>HostInterface</b>")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet('border-bottom: 2px solid black; padding-bottom: 5px; margin-bottom: 10px;')

        # Create a layout for the frame
        frame_layout = QVBoxLayout()
        frame_layout.addWidget(title_label)

        # Create a widget to contain the dynamic sections
        sections_widget = QWidget()
        sections_layout = QHBoxLayout()

        # Function to create a section with title and color
        def create_section(title, color):
            section_frame = QFrame()
            section_frame.setFrameShape(QFrame.StyledPanel)
            section_frame.setFrameShadow(QFrame.Raised)
            section_frame.setStyleSheet(
                f'background-color: {color}; border: 2px solid black; border-radius: 10px; padding: 10px; margin: 5px;')  # Set background color
            section_layout = QVBoxLayout()
            title_label = QLabel(f"<b>{title}</b>")
            title_label.setAlignment(Qt.AlignCenter)
            section_layout.addWidget(title_label)
            section_frame.setLayout(section_layout)
            return section_frame

        # Generate sections dynamically based on host_interface data
        data_sections = {
            "BMT": self.host_interface.get_bmt(),
            "H2G": self.host_interface.get_h2g(),
            "G2H": self.host_interface.get_g2h(),
            "PCIe": self.host_interface.get_pcie()
        }

        for section_name, section_data in data_sections.items():
            # Determine the color based on the section type
            color = 'gray'  # Default color if not found in CLASTER_COLORS
            if section_name in CLASTER_COLORS:
                color = CLASTER_COLORS[section_name]

            section_frame = create_section(section_name, color)
            sections_layout.addWidget(section_frame)

        sections_widget.setLayout(sections_layout)

        # Add sections widget to the frame layout
        frame_layout.addWidget(sections_widget)
        outer_frame.setLayout(frame_layout)

        # Add the outer frame to the main layout
        main_layout.addWidget(outer_frame)
        self.setLayout(main_layout)
