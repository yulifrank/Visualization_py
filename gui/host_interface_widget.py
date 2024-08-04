from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt

class HostInterfaceWidget(QWidget):
    def __init__(self, host_interface, parent=None):
        super().__init__(parent)
        self.host_interface = host_interface
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()  # Use horizontal layout

        # Function to create a section with title and content
        def create_section(title, content):
            frame = QFrame()
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setFrameShadow(QFrame.Raised)
            frame.setStyleSheet('border: 2px solid #333; border-radius: 10px; padding: 10px; margin: 5px;')  # Added border style
            section_layout = QVBoxLayout()
            title_label = QLabel(f"<b>{title}</b>")
            title_label.setAlignment(Qt.AlignCenter)
            section_layout.addWidget(title_label)
            section_layout.addWidget(content)
            frame.setLayout(section_layout)
            return frame

        # Create BMT section
        bmt_label = QLabel(f"BMT: {self.host_interface.get_bmt()}")
        bmt_section = create_section("BMT", bmt_label)
        layout.addWidget(bmt_section)

        # Create H2G section
        h2g_layout = QVBoxLayout()
        h2g_data = self.host_interface.get_h2g()
        for key, value in h2g_data.items():
            label = QLabel(f"{key}: {value}")
            h2g_layout.addWidget(label)
        h2g_section = create_section("H2G", QWidget().setLayout(h2g_layout))
        layout.addWidget(h2g_section)

        # Create G2H section
        g2h_layout = QVBoxLayout()
        g2h_data = self.host_interface.get_g2h()
        for eq in g2h_data:
            eq_label = QLabel(f"EQ ID {eq['id']}: {eq['event_queue']}")
            g2h_layout.addWidget(eq_label)
        g2h_section = create_section("G2H", QWidget().setLayout(g2h_layout))
        layout.addWidget(g2h_section)

        # Create PCIe section
        pcie_label = QLabel("PCIe information here")  # Adjust as needed based on PCIe data
        pcie_section = create_section("PCIe", pcie_label)
        layout.addWidget(pcie_section)

        self.setLayout(layout)
