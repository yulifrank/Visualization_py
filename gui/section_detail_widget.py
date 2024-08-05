from PyQt5.QtWidgets import QPushButton, QLabel, QGridLayout, QVBoxLayout, QWidget

from component import Component


class SectionDetailWidget(QWidget):
    def __init__(self, host_interface, data, parent=None):
        super().__init__(parent)
        self.host_interface = host_interface
        self.data = data
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Show details based on the type of data
        if not self.data:
            self.layout.addWidget(QLabel("No details to show"))
        elif isinstance(self.data, Component):
            if not self.data.data:
                self.layout.addWidget(QLabel("No details to show"))
            else:
                self.layout.addWidget(QLabel(f"Component ID: {self.data.id}, Component Name: {self.data.data}"))
        elif isinstance(self.data, dict):
            if not self.data:
                self.layout.addWidget(QLabel("No details to show"))
            else:
                for key, value in self.data.items():
                    self.layout.addWidget(QLabel(f"{key}: {value}"))
        elif isinstance(self.data, list):
            if not self.data:
                self.layout.addWidget(QLabel("No details to show"))
            else:
                # Add items in a grid layout within the detail widget
                grid_layout = QGridLayout()
                for idx, item in enumerate(self.data):
                    row = idx // 7  # Adjust the number of columns here
                    col = idx % 7
                    grid_item = QLabel(f"Item: {item}")
                    grid_item.setStyleSheet('padding: 2px; margin: 2px;')
                    grid_layout.addWidget(grid_item, row, col)
                self.layout.addLayout(grid_layout)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        self.layout.addWidget(close_button)
