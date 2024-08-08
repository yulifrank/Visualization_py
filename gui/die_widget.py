# die_widget.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QPushButton
from PyQt5.QtCore import Qt
from gui.quad_widget import QuadWidget
from gui.hbm_widget import HBMWidget

class DieWidget(QWidget):
    def __init__(self, data_manager, dies, main_window):
        super().__init__()
        self.data_manager = data_manager
        self.main_window = main_window
        self.dies = dies
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Container for Quad and HBM Widgets
        self.grid_container = QWidget()
        self.grid_layout = QGridLayout(self.grid_container)
        self.grid_layout.setSpacing(0)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.grid_container)

        # Back button
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

        # Initially hide the grid_container
        self.grid_container.setVisible(False)

    def show_quads(self, die_index):
        try:
            die = self.dies.get(die_index)
            if die is None:
                print("Error: die is None")
                return

            # Clear previous widgets from the grid layout
            self.clear_layout(self.grid_layout)

            # Display new matrix of 4 quads and position HBM widgets accordingly
            for i in range(2):
                for j in range(2):
                    quad = die.quads[i][j]
                    if quad:
                        quad_widget = QuadWidget(quad, (i, j), self)
                    else:
                        quad_widget = QLabel('Empty', self)
                        quad_widget.setAlignment(Qt.AlignCenter)
                        quad_widget.setStyleSheet(
                            'border: 1px dashed black; min-width: 150px; min-height: 150px; background-color: red;')

                    # Add quad widget to the grid
                    self.grid_layout.addWidget(quad_widget, i, j * 2, alignment=Qt.AlignCenter)

                    # Create HBM widget
                    hbm_widget = HBMWidget(quad.hbm)

                    # Determine HBM widget's position
                    if j == 0:  # For Quads 1 and 3 (left side)
                        self.grid_layout.addWidget(hbm_widget, i, j * 2 + 1, alignment=Qt.AlignCenter)  # HBM on the right
                    elif j == 1:  # For Quads 2 and 4 (right side)
                        self.grid_layout.addWidget(hbm_widget, i, j * 2 - 1, alignment=Qt.AlignCenter)  # HBM on the left

            # Adjust sizes and visibility
            self.adjust_sizes()
            self.grid_container.setVisible(True)
            print(f"Showing quads for DIE{die_index}")

        except Exception as e:
            print(f"Error showing quads: {e}")

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clear_layout(item.layout())
        layout.update()

    def adjust_sizes(self):
        try:
            size = self.size().width() // 6 + 150  # Adjust size to fit both quad and HBM
            for i in range(2):
                for j in range(2):
                    # Adjust size of quad
                    quad_item = self.grid_layout.itemAtPosition(i, j * 2)
                    if quad_item:
                        widget = quad_item.widget()
                        if widget:
                            widget.setFixedSize(size, size)

                    # Adjust size of HBM
                    hbm_left_item = self.grid_layout.itemAtPosition(i, j * 2 - 1)
                    hbm_right_item = self.grid_layout.itemAtPosition(i, j * 2 + 1)

                    if hbm_left_item:
                        widget = hbm_left_item.widget()
                        if widget:
                            widget.setFixedSize(size // 3, size // 2)  # Make HBM slightly taller

                    if hbm_right_item:
                        widget = hbm_right_item.widget()
                        if widget:
                            widget.setFixedSize(size // 3, size // 2)  # Make HBM slightly taller

            print("Adjusted sizes")
        except Exception as e:
            print(f"Error adjusting sizes: {e}")

    def resizeEvent(self, event):
        self.adjust_sizes()
        super().resizeEvent(event)

    def go_back(self):
        self.main_window.show_die_buttons()
