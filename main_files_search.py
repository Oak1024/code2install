#import sys
from sys import argv, exit
from files_search import Ui_MainWindow

from PyQt5.QtWidgets import QApplication, QMainWindow


# class main_logic(Ui_MainWindow):
#     def __init__(self, parent=None):
#         super(main_logic, self).__init__(parent)


if __name__ == '__main__':
    app = QApplication(argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    # ui = main_logic()
    # 向主窗口上添加控件s
    ui.setupUi(MainWindow)

    MainWindow.show()
    exit(app.exec_())