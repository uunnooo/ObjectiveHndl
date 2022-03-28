# PyQtFileDialog.py
import sys

import pandas
import re
import numpy as np
from PyQt5.QtWidgets import *
import pandas as pd
from PyQt5.QtCore import *
import _ParsingPattern_ as Par

class CFileDialogWindow(QWidget) :
    def __init__(self) :
        super().__init__()

        self.label = QLabel("파일 : ", self)
        self.BTInfor = QPushButton("Information 파일 선택", self)
        self.BTInfor.clicked.connect(self.BTInfor_clicked)
        self.BTData = QPushButton("Data 파일 선택", self)
        self.BTData.clicked.connect(self.BTData_clicked)

        self.setupUI()

    def setupUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.label, 0, 0, 1, 5)
        grid.addWidget(self.BTInfor, 1, 0, 1, 1)
        grid.addWidget(self.BTData, 1, 2, 1, 1)

        self.setWindowTitle("Load File")
        self.setGeometry(300, 300, 300, 100)
        self.show()

    def BTInfor_clicked(self):
        tmpData = []
        columList = []
        fname = QFileDialog.getOpenFileName(self, 'Select File', 'D:\\uno\\2021\\핸들링편차파일\\',
                                            'Inforfile(*.txt)')
        rawData = pd.read_csv(fname[0], engine='c', encoding='cp1252', on_bad_lines='skip', header=None,
                        skip_blank_lines=True, keep_default_na=False)
        [tmpData.append(rawData.loc[i].str.split()) for i in range(len(rawData))]

        for name, pattern in Par.InformationTest().__dict__.items() :
            columList.append([name, np.where(rawData[0].str.contains(pattern, flags=re.I))[0]])
        print(columList)



        self.label.setText(fname[0])

    def BTData_clicked(self):
        tmpData = []
        fname = QFileDialog.getOpenFileName(self, 'Select File', 'D:\\uno\\2021\\핸들링편차파일\\',
                                            'Inforfile(*.txt)')
        rawData = pd.read_csv(fname[0], engine='c', encoding='cp1252', on_bad_lines='skip', header=None,
                        skip_blank_lines=True, keep_default_na=False)
        [tmpData.append(rawData.loc[i].str.split()) for i in range(len(rawData))]

        self.label.setText(fname[0])

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = CFileDialogWindow()
    app.exec_()
