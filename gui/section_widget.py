from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QFrame, QGridLayout
from PyQt5.QtCore import Qt
from component import Component
from constants import CLASTER_COLORS


class SectionWidget(QWidget):
    def __init__(self, host_interface, parent=None):
        super().__init__(parent)
        self.host_interface = host_interface
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()  # Use QVBoxLayout for vertical stacking

        # Create a grid layout for sections
        self.grid_layout = QGridLayout()

        self.data_sections = {
            "BMT": self.host_interface.get_bmt(),
            "H2G": self.host_interface.get_h2g(),
            "G2H": self.host_interface.get_g2h(),
            "PCIe": self.host_interface.get_pcie()
        }

        # Add the section labels/buttons to the grid layout
        row = 0
        col = 0
        for section_name, section_data in self.data_sections.items():
            color = CLASTER_COLORS.get(section_name, 'gray')
            widget = None
            if section_name in ["BMT", "PCIe"]:
                widget = self.create_section_label(section_name, color, section_data)
            else:
                widget = self.create_section_button(section_name, color, section_data)

            if widget:
                self.grid_layout.addWidget(widget, row, col)
                col += 1
                if col >= 4:  # Move to the next row after 4 columns
                    col = 0
                    row += 1

        self.layout.addLayout(self.grid_layout)

        self.setLayout(self.layout)

    def create_section_label(self, title, color, data):
        if not data or (isinstance(data, dict) and not data) or (isinstance(data, list) and not data):
            return None
        label = QLabel(f"{title}: {data}")
        label.setStyleSheet(
            f'background-color: {color}; border: 2px solid black; border-radius: 10px; padding: 5px; margin: 5px;'
        )
        label.setFixedSize(150, 50)
        return label

    def create_section_button(self, title, color, data):
        if not data or (isinstance(data, dict) and not data) or (isinstance(data, list) and not data):
            return None
        button = QPushButton(title)
        button.setStyleSheet(
            f'background-color: {color}; border: 2px solid black; border-radius: 10px; padding: 5px; margin: 5px;'
        )
        button.setFixedSize(150, 50)
        button.setCheckable(True)  # Make the button checkable
        button.clicked.connect(lambda checked, t=title, d=data: self.toggle_details(t, d, button))
        return button

    def toggle_details(self, title, data, button):
        if not button.isChecked():
            self.remove_details()
            return

        # Remove any existing detail frame to avoid overlap
        self.remove_details()

        detail_frame = QFrame()
        detail_frame.setFrameShape(QFrame.StyledPanel)
        detail_frame.setStyleSheet(
            'background-color: lightgray; border: 2px solid black; border-radius: 10px; padding: 10px;')
        detail_layout = QVBoxLayout()
        detail_frame.setLayout(detail_layout)

        if not data:
            detail_layout.addWidget(QLabel("No details to show"))
        elif isinstance(data, Component):
            if not data.data:
                detail_layout.addWidget(QLabel("No details to show"))
            else:
                detail_layout.addWidget(QLabel(f"Component ID: {data.id}, Component Name: {data.data}"))
        elif isinstance(data, dict):
            if not data:
                detail_layout.addWidget(QLabel("No details to show"))
            else:
                for key, value in data.items():
                    detail_layout.addWidget(QLabel(f"{key}: {value}"))
        elif isinstance(data, list):
            if not data:
                detail_layout.addWidget(QLabel("No details to show"))
            else:
                # Add items in a grid layout within the detail frame
                grid_layout = QGridLayout()
                for idx, item in enumerate(data):
                    row = idx // 4  # Adjust the number of columns here
                    col = idx % 4
                    grid_item = QLabel(f"Item: {item}")
                    grid_item.setStyleSheet('padding: 2px; margin: 2px;')
                    grid_layout.addWidget(grid_item, row, col)
                detail_layout.addLayout(grid_layout)

        close_button = QPushButton("Close")
        close_button.clicked.connect(lambda: self.close_detail_frame(button))
        detail_layout.addWidget(close_button)

        self.layout.addWidget(detail_frame)
        self.detail_frame = detail_frame  # Store the detail frame to manage its visibility

    def close_detail_frame(self, button):
        if hasattr(self, 'detail_frame'):
            self.detail_frame.hide()
            self.layout.removeWidget(self.detail_frame)
            self.detail_frame.deleteLater()
            del self.detail_frame
        button.setChecked(False)  # Uncheck the button

    def remove_details(self):
        if hasattr(self, 'detail_frame'):
            self.detail_frame.hide()
            self.layout.removeWidget(self.detail_frame)
            self.detail_frame.deleteLater()
            del self.detail_frame
