from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QPushButton
from PyQt5.QtCore import Qt
from gui.quad_widget import QuadWidget
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

        # Container for Quad Matrix
        self.quad_container = QWidget()
        self.quad_layout = QGridLayout(self.quad_container)
        self.quad_layout.setSpacing(0)  # Reduced spacing
        self.quad_layout.setContentsMargins(0, 0,0, 0)  # Add small margins
        self.layout.addWidget(self.quad_container)

        # Back button
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

        # Initially hide the quad_container
        self.quad_container.setVisible(False)

    def show_quads(self, die_index):
        try:
            die = self.dies.get(die_index)
            if die is None:
                print("Error: die is None")
                return

            # Clear previous widgets from the quad layout
            self.clear_layout(self.quad_layout)

            # Display new matrix of 4 quads
            for i in range(2):
                for j in range(2):
                    quad = die.quads[i][j]
                    if quad:
                        quad_widget = QuadWidget(quad, self)
                    else:
                        quad_widget = QLabel('Empty', self)
                        quad_widget.setAlignment(Qt.AlignCenter)
                        quad_widget.setStyleSheet(
                            'border: 1px dashed black; min-width: 150px; min-height: 150px; background-color: red;')
                    self.quad_layout.addWidget(quad_widget, i, j, alignment=Qt.AlignCenter)

            self.adjust_quad_sizes()
            self.quad_container.setVisible(True)
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

    def adjust_quad_sizes(self):
        try:
            size = self.size().width() // 3 +150
            for i in range(2):
                for j in range(2):
                    item = self.quad_layout.itemAtPosition(i, j)
                    if item:
                        widget = item.widget()
                        if widget:
                            widget.setFixedSize(size, size)
            print("Adjusted quad sizes")
        except Exception as e:
            print(f"Error adjusting quad sizes: {e}")

    def resizeEvent(self, event):
        self.adjust_quad_sizes()
        super().resizeEvent(event)

    def go_back(self):
        self.main_window.show_die_buttons()
