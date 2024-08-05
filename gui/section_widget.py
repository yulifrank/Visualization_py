from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
from constants import CLASTER_COLORS
from gui.section_detail_widget import SectionDetailWidget

class SectionWidget(QWidget):
    def __init__(self, host_interface, parent=None):
        super().__init__(parent)
        self.host_interface = host_interface
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.grid_layout = QGridLayout()
        self.data_sections = {
            "BMT": self.host_interface.get_bmt(),
            "PCIe": self.host_interface.get_pcie()
        }
        self.update_sections()
        self.layout.addLayout(self.grid_layout)
        self.setLayout(self.layout)

    def update_sections(self):
        for i in range(self.grid_layout.count()):
            item = self.grid_layout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()

        row = 0
        col = 0
        for section_name, section_data in self.data_sections.items():
            color = CLASTER_COLORS.get(section_name, 'gray')
            widget = self.create_section_label(section_name, color, section_data)
            if widget:
                self.grid_layout.addWidget(widget, row, col)
                col += 1
                if col >= 7:
                    col = 0
                    row += 1

    def create_section_label(self, title, color, data):
        if not data or (isinstance(data, dict) and not data) or (isinstance(data, list) and not data):
            return None
        label = QLabel(f"{title}: {data}")
        label.setStyleSheet(
            f'background-color: {color}; border: 2px solid black; border-radius: 7px; padding: 5px; margin: 5px;'
        )
        label.setFixedSize(150, 50)
        return label

    def update_section_data(self, section_name, data):
        self.data_sections[section_name] = data
        self.update_sections()
