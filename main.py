# main.py :
import sys
from PyQt5.QtWidgets import QApplication

from controller import DataManager
from gui.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    data_manager = DataManager('chip_data.json','sl.json')
    main_window = MainWindow(data_manager)
    main_window.show()
    sys.exit(app.exec_())
