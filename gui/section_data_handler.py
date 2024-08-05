
from gui.section_detail_widget import SectionDetailWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout, QWidget
class SectionDataHandler(QWidget):
    def __init__(self, host_interface, parent=None):
        super().__init__(parent)
        self.host_interface = host_interface
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def get_section_data(self, section_name):
        if section_name == 'H2G':
            return self.host_interface.get_h2g()
        elif section_name == 'G2H':
            return self.host_interface.get_g2h()
        elif section_name == 'BMT':
            return self.host_interface.get_bmt()
        elif section_name == 'PCIe':
            return self.host_interface.get_pcie()
        else:
            return None

    def display_section_data(self, section_name):
        data = self.get_section_data(section_name)
        if data:
            # Clear existing content
            for i in reversed(range(self.layout.count())):
                widget = self.layout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()

            # Create and add the section detail widget
            detail_widget = SectionDetailWidget(self.host_interface, data)
            self.layout.addWidget(detail_widget)
            self.show()  # Ensure widget is visible
        else:
            # Display message if no data is available
            self.layout.addWidget(QLabel(f"No data available for {section_name}"))