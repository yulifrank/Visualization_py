from PyQt5.QtWidgets import QPushButton, QLabel, QGridLayout, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

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
                # Add items in a responsive grid layout within the detail widget
                grid_layout = QGridLayout()
                num_columns = 7  # Default number of columns
                num_items = len(self.data)
                num_rows = (num_items + num_columns - 1) // num_columns  # Compute the number of rows

                # Stretch factors for responsive resizing
                for i in range(num_rows):
                    grid_layout.setRowStretch(i, 1)
                for i in range(num_columns):
                    grid_layout.setColumnStretch(i, 1)

                # Add items to the grid layout
                for idx, item in enumerate(self.data):
                    row = idx // num_columns
                    col = idx % num_columns
                    grid_item = QLabel(f"Item: {item}")
                    grid_item.setStyleSheet('padding: 2px; margin: 2px;')
                    grid_item.setAlignment(Qt.AlignCenter)
                    grid_layout.addWidget(grid_item, row, col)

                self.layout.addLayout(grid_layout)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        self.layout.addWidget(close_button)
