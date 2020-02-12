# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'files_search.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets  # QtGui,
from PyQt5.QtWidgets import QFileDialog,  QMessageBox  # QWidget, QTableView, QVBoxLayout, QHeaderView,
from PyQt5.QtCore import pyqtSignal, QObject
#from PyQt5.QtGui import QStandardItemModel, QStandardItem
#import os
#import re
from re import search, IGNORECASE
from get_filelist import get_filelist, readTxt, readCsv, readExcel, readPptx, readDocx


class Ui_MainWindow(QObject):
#class Ui_MainWindow(object):
    sendmsg = pyqtSignal(list, list)
    no_checked_notice = pyqtSignal(str)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 50, 420, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.check_py = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_py.setObjectName("check_py")
        self.gridLayout.addWidget(self.check_py, 0, 3, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.check_txt = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_txt.setObjectName("check_txt")
        self.gridLayout.addWidget(self.check_txt, 0, 2, 1, 1)
        self.check_docx = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_docx.setObjectName("check_docx")
        self.gridLayout.addWidget(self.check_docx, 1, 1, 1, 1)
        self.check_pptx = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_pptx.setObjectName("check_pptx")
        self.gridLayout.addWidget(self.check_pptx, 1, 0, 1, 1)
        self.check_m = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_m.setObjectName("check_m")
        self.gridLayout.addWidget(self.check_m, 0, 1, 1, 1)
        self.check_csv = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_csv.setObjectName("check_csv")
        self.gridLayout.addWidget(self.check_csv, 0, 4, 1, 1)
        self.check_cpp_c = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_cpp_c.setObjectName("check_cpp_c")
        self.gridLayout.addWidget(self.check_cpp_c, 1, 2, 1, 1)
        self.check_xlsx = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_xlsx.setObjectName("check_xlsx")
        self.gridLayout.addWidget(self.check_xlsx, 1, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 4, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(700, 50, 300, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.check_file_name = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.check_file_name.setObjectName("check_file_name")
        self.horizontalLayout.addWidget(self.check_file_name)
        self.check_file_content = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.check_file_content.setObjectName("check_file_content")
        self.horizontalLayout.addWidget(self.check_file_content)


        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(500, 50, 150, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # 关键字 label
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        # keyword LineEdit
        self.line_edit_keyword = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.line_edit_keyword.setObjectName("line_edit_keyword")
        self.horizontalLayout_2.addWidget(self.line_edit_keyword)


        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(0, 0, 51, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(70, 170, 400, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # 选择文件夹 按钮
        self.btn_file_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.btn_file_1.setObjectName("btn_file_1")
        # 选择文件夹 内容
        self.horizontalLayout_3.addWidget(self.btn_file_1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        # 搜索 按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 180, 61, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        # 结果 显示
        # 设置数据层次结构，4行4列
        # self.model = QStandardItemModel(4, 2)
        # # 设置水平方向四个头标签文本内容
        # self.model.setHorizontalHeaderLabels(['内容', '地址'])
        #
        # self.tableView = QTableView()
        # self.tableView.setModel(self.model)
        #
        # # 设置布局
        # layout = QVBoxLayout()
        # layout.setGeometry(QtCore.QRect(70, 200, 400, 51))
        # layout.addWidget(self.tableView)
        # #self.setLayout(layout)

        # tableview
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(70, 220, 1440, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(4)



        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        file_list_temp =['file1', 'file2', 'file3']
        conteht_list_temp = ['co1', 'co2', 'co3']

        self.showTable(file_list_temp, conteht_list_temp)


        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.check_arr = [self.checkBox, self.check_m, self.check_txt, self.check_py, self.check_csv,
                          self.check_pptx, self.check_docx, self.check_cpp_c, self.check_xlsx,
                          self.check_file_name, self.check_file_content, None]
        self.state_arr = [False, False, False, False, False, False, False, False, False, False, False]

        self.check_arr[0].stateChanged.connect(lambda: self.state_changed(self.check_arr[0], 0))
        self.check_arr[1].stateChanged.connect(lambda: self.state_changed(self.check_arr[1], 1))
        self.check_arr[2].stateChanged.connect(lambda: self.state_changed(self.check_arr[2], 2))
        self.check_arr[3].stateChanged.connect(lambda: self.state_changed(self.check_arr[3], 3))
        self.check_arr[4].stateChanged.connect(lambda: self.state_changed(self.check_arr[4], 4))
        self.check_arr[5].stateChanged.connect(lambda: self.state_changed(self.check_arr[5], 5))
        self.check_arr[6].stateChanged.connect(lambda: self.state_changed(self.check_arr[6], 6))
        self.check_arr[7].stateChanged.connect(lambda: self.state_changed(self.check_arr[7], 7))
        self.check_arr[8].stateChanged.connect(lambda: self.state_changed(self.check_arr[8], 8))
        self.check_arr[9].stateChanged.connect(lambda: self.state_changed(self.check_arr[9], 9))
        self.check_arr[10].stateChanged.connect(lambda: self.state_changed(self.check_arr[10], 10))

        # 关键词 填写 触发
        self.keyword = ""
        self.line_edit_keyword.textChanged.connect(self.get_key_word)

        # 选择文件夹 触发
        self.file_road = ""
        self.btn_file_1.clicked.connect(self.get_file_road)

        # 填写文件内容 触发
        self.lineEdit_3.textChanged.connect(self.file_road_write)

        self.content_list =[]
        self.file_list=[]
        # 搜索文件/文件夹 触发, 返回content和file_road
        self.pushButton.clicked.connect(self.search_working)

        # 自定义信号触发函数
        self.sendmsg.connect(self.showTable)

        # 自定义信号触发函数，无文件类型被选中时触发
        self.no_checked_notice.connect(self.show_no_checked_notice)

    def show_no_checked_notice(self, notice):
        QMessageBox.about(self.centralwidget, "警告", notice)



    def showTable(self, file_list, content_list):
        _translate = QtCore.QCoreApplication.translate
        row_num = len(file_list)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(row_num)

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "content"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "address"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for i in range(row_num):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 0, item)
            item.setText(_translate("MainWindow", content_list[i]))
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 1, item)
            item.setText(_translate("MainWindow", file_list[i]))



        # item = self.tableWidget.item(0, 0)
        # item.setText(_translate("MainWindow", "file1"))
        #self.tableWidget.horizontalHeader().setStretchLastSection(True)

        #self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setColumnWidth(0, 800)
        self.tableWidget.setColumnWidth(1, 600)


    def search_working(self, keyword):
        self.file_list = []
        self.content_list = []
        url = self.lineEdit_3.text()
        url = url.replace('/', '\\') + '\\'
        print(url)
        filelist = get_filelist(url, [])

        pattern = self.keyword
        print(len(filelist))

        # self.check_arr = [self.checkBox, self.check_m, self.check_txt, self.check_py, self.check_csv,
        #                   self.check_pptx, self.check_docx, self.check_cpp_c, self.check_xlsx,
        #                   self.check_file_name, self.check_file_content, None]
        # self.state_arr = [False, False, False, False, False, False, False, False, False, False, False]

        file_type_list = ['.v/.sv', '.m', '.txt', '.py', '.csv', '.pptx', '.docx', '.c/.cpp', '.xlsx/.xls']
        check_type_list = ['file_name', 'file_content']
        file_type_num = []
        check_type_num = []

        # 判断是否勾选 文件类型
        for i in range(9):
            if (self.state_arr[i]) & (i <= 8) :
                print(self.state_arr[i], i)
                file_type_num.append(i)
        print(file_type_num)
        if file_type_num == []:
            print('file_type')
            self.no_checked_notice.emit('文件类型未选中')
            return 0

        file_name_arr = [[], [], [], [], [], [], [], [], []]

        # 待搜索的文件后缀
        file_type_search = set()

        for i in range(9):
            if(self.state_arr[i]):
                file_type_sub = file_type_list[i].split('/')
                for ft in file_type_sub:
                    file_type_search.add(ft)
        print(file_type_search)

        content = ''
        for ft in file_type_search:
            print(ft)
            for e in filelist:
                print(type(e),e)

                if e.endswith(ft):
                    if (ft=='.v')|(ft=='.sv')|(ft=='.c')|(ft=='.cpp')|(ft=='.m')|(ft=='.txt')|(ft=='.py'):
                        print('ifv')
                        content = readTxt(e)
                        print('readtxt')
                    elif (ft=='.pptx'):
                        content = readPptx(e)
                    elif (ft=='.docx'):
                        content = readDocx(e)
                    elif (ft=='.xls')|(ft=='.xlsx'):
                        content = readExcel(e)
                    elif (ft=='.csv'):
                        content = readCsv(e)
                    else:
                        content = ''
                else:
                    content = ''
                print('match')
                match = search(pattern, content, IGNORECASE)
                if match != None:
                    start = match.start()
                    end = match.end()
                    print(e)
                    start = 0 if start < 20 else start - 20
                    end = len(e) if (end + 20 < len(e)) else end + 20
                    print(content[start:end])
                    self.file_list.append(e)
                    self.content_list.append(content[start:end])
        self.sendmsg.emit(self.file_list, self.content_list)
        # for e in filelist:
        #     content = readTxt(e)
        #     match = re.search(pattern, content, re.IGNORECASE)
        #     if match != None:
        #         start = match.start()
        #         end = match.end()
        #         print(e)
        #         start = 0 if start < 25 else start - 25
        #         end = len(e) if (end + 25 < len(e)) else end + 25
        #         print(content[start:end])
        #         self.file_list.append(e)
        #         self.content_list.append(content[start:end])
        # self.sendmsg.emit(self.file_list, self.content_list)

        # length_file = len(self.file_list)
        # for k in range(length_file):
        #     print(self.file_list[k])
        # for j in range(length_file):
        #     print(self.content_list[k])
        # print(length_file)




    def file_road_write(self, text):
        self.file_road = text
        print(text)

    def get_key_word(self, text):
        self.keyword = text
        print(text)

    def get_file_road(self):
        str = QFileDialog.getExistingDirectory(self.horizontalLayoutWidget_3, "选择文件夹", "/")
        self.lineEdit_3.setText(str)
        print(str)
        # 输出文件路径及文件名
    #     list = traverse(str);
    #     for i in list:
    #         print(i)
    #
    # def traverse(self,f):
    #     # list存文件名
    #     list = []
    #     fs = os.listdir(f)
    #     for f1 in fs:
    #         tmp_path = os.path.join(f, f1)
    #         if not os.path.isdir(tmp_path):
    #             list.append(tmp_path)
    #     return list


    def state_changed(self, check_box, num):
        for i in range(11):
            self.state_arr[i] = self.check_arr[i].isChecked()
        print(self.state_arr)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.check_py.setText(_translate("MainWindow", ".py"))
        self.checkBox.setText(_translate("MainWindow", ".v"))
        self.check_txt.setText(_translate("MainWindow", ".txt"))
        self.check_docx.setText(_translate("MainWindow", ".docx"))
        self.check_pptx.setText(_translate("MainWindow", ".pptx"))
        self.check_m.setText(_translate("MainWindow", ".m"))
        self.check_csv.setText(_translate("MainWindow", ".csv"))
        self.check_cpp_c.setText(_translate("MainWindow", ".c/cpp"))
        self.check_xlsx.setText(_translate("MainWindow", ".xls/x"))
        self.check_file_name.setText(_translate("MainWindow", "查找文件名"))
        self.check_file_content.setText(_translate("MainWindow", "查找文件内容"))
        self.label.setText(_translate("MainWindow", "关键词："))
        self.comboBox.setItemText(0, _translate("MainWindow", "打开"))
        self.comboBox.setItemText(1, _translate("MainWindow", "帮助"))
        self.comboBox.setItemText(2, _translate("MainWindow", "软件信息"))
        self.btn_file_1.setText(_translate("MainWindow", "选择文件夹"))
        self.pushButton.setText(_translate("MainWindow", "搜索"))
