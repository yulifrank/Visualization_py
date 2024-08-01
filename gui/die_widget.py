from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QScrollArea
from PyQt5.QtCore import Qt
from gui.quad_widget import QuadWidget

class DieWidget(QWidget):
    def __init__(self, data_manager):
        super().__init__()
        self.data_manager = data_manager
        self.die1 = None
        self.die2 = None
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Scroll area for Quad Matrix
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)

        # Container for Quad Matrix
        self.quad_container = QWidget()
        self.quad_layout = QGridLayout(self.quad_container)
        self.quad_layout.setSpacing(10)
        self.quad_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.addWidget(self.quad_container)
        self.scroll_area.setWidget(self.scroll_content)
        self.layout.addWidget(self.scroll_area)

        # Initially hide the quad_container
        self.quad_container.setVisible(False)

        # Load dies
        self.load_dies()

    def load_dies(self):
        try:
            self.die1 = self.data_manager.load_die(0)
            self.die2 = self.data_manager.load_die(1)
            print("DIEs loaded")
        except Exception as e:
            print(f"Error loading DIEs: {e}")

    def show_quads(self, die_index):
        try:
            die = self.die1 if die_index == 0 else self.die2
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
                            'border: 1px dashed black; min-width: 150px; min-height: 150px; background-color: lightgrey;')
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
            size = self.size().width() // 2 - 20
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
