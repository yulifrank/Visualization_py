from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QFrame
from PyQt5.QtCore import Qt
from component import Component
from constants import CLASTER_COLORS
from gui.section_detail_widget import SectionDetailWidget


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
                if col >= 7:  # Move to the next row after 7 columns
                    col = 0
                    row += 1

        self.layout.addLayout(self.grid_layout)

        self.setLayout(self.layout)

    def create_section_label(self, title, color, data):
        if not data or (isinstance(data, dict) and not data) or (isinstance(data, list) and not data):
            return None
        label = QLabel(f"{title}: {data}")
        label.setStyleSheet(
            f'background-color: {color}; border: 2px solid black; border-radius: 7px; padding: 5px; margin: 5px;'
        )
        label.setFixedSize(150, 50)
        return label

    def create_section_button(self, title, color, data):
        if not data or (isinstance(data, dict) and not data) or (isinstance(data, list) and not data):
            return None
        button = QPushButton(title)
        button.setStyleSheet(
            f'background-color: {color}; border: 2px solid black; border-radius: 7px; padding: 5px; margin: 5px;'
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

        self.detail_widget = SectionDetailWidget(self.host_interface, data)
        self.layout.addWidget(self.detail_widget)
        self.detail_widget.show()

        button.setChecked(True)  # Ensure the button stays checked

    def remove_details(self):
        if hasattr(self, 'detail_widget'):
            self.detail_widget.hide()
            self.layout.removeWidget(self.detail_widget)
            self.detail_widget.deleteLater()
            del self.detail_widget
