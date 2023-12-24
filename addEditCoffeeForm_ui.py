from PyQt5 import QtCore, QtGui, QtWidgets


class SecondFormUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(601, 193)
        self.deleteGroupBox = QtWidgets.QGroupBox(Form)
        self.deleteGroupBox.setGeometry(QtCore.QRect(0, 0, 601, 41))
        self.deleteGroupBox.setTitle("")
        self.deleteGroupBox.setObjectName("deleteGroupBox")
        self.label = QtWidgets.QLabel(self.deleteGroupBox)
        self.label.setGeometry(QtCore.QRect(8, 7, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.deleteButton = QtWidgets.QPushButton(self.deleteGroupBox)
        self.deleteButton.setGeometry(QtCore.QRect(472, 5, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.idEdit = QtWidgets.QLineEdit(self.deleteGroupBox)
        self.idEdit.setGeometry(QtCore.QRect(40, 9, 421, 21))
        self.idEdit.setObjectName("idEdit")
        self.addRowGroupBox = QtWidgets.QGroupBox(Form)
        self.addRowGroupBox.setGeometry(QtCore.QRect(0, 40, 601, 171))
        self.addRowGroupBox.setTitle("")
        self.addRowGroupBox.setObjectName("addRowGroupBox")
        self.saveButton = QtWidgets.QPushButton(self.addRowGroupBox)
        self.saveButton.setGeometry(QtCore.QRect(472, 3, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.titleEdit = QtWidgets.QLineEdit(self.addRowGroupBox)
        self.titleEdit.setGeometry(QtCore.QRect(120, 5, 341, 21))
        self.titleEdit.setObjectName("titleEdit")
        self.roastingEdit = QtWidgets.QLineEdit(self.addRowGroupBox)
        self.roastingEdit.setGeometry(QtCore.QRect(130, 30, 331, 21))
        self.roastingEdit.setObjectName("roastingEdit")
        self.typeEdit = QtWidgets.QLineEdit(self.addRowGroupBox)
        self.typeEdit.setGeometry(QtCore.QRect(140, 55, 321, 21))
        self.typeEdit.setObjectName("typeEdit")
        self.weightEdit = QtWidgets.QLineEdit(self.addRowGroupBox)
        self.weightEdit.setGeometry(QtCore.QRect(110, 130, 351, 21))
        self.weightEdit.setObjectName("weightEdit")
        self.costEdit = QtWidgets.QLineEdit(self.addRowGroupBox)
        self.costEdit.setGeometry(QtCore.QRect(60, 105, 401, 21))
        self.costEdit.setObjectName("costEdit")
        self.tasteEdit = QtWidgets.QLineEdit(self.addRowGroupBox)
        self.tasteEdit.setGeometry(QtCore.QRect(120, 80, 341, 21))
        self.tasteEdit.setObjectName("tasteEdit")
        self.label_2 = QtWidgets.QLabel(self.addRowGroupBox)
        self.label_2.setGeometry(QtCore.QRect(8, 3, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.addRowGroupBox)
        self.label_3.setGeometry(QtCore.QRect(8, 28, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.addRowGroupBox)
        self.label_4.setGeometry(QtCore.QRect(8, 53, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.addRowGroupBox)
        self.label_5.setGeometry(QtCore.QRect(8, 78, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.addRowGroupBox)
        self.label_6.setGeometry(QtCore.QRect(8, 103, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.addRowGroupBox)
        self.label_7.setGeometry(QtCore.QRect(8, 128, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.editButton = QtWidgets.QPushButton(self.addRowGroupBox)
        self.editButton.setGeometry(QtCore.QRect(472, 36, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editButton.setFont(font)
        self.editButton.setObjectName("editButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Редактирование БД"))
        self.label.setText(_translate("Form", "ID = "))
        self.deleteButton.setText(_translate("Form", "Удалить запись"))
        self.saveButton.setText(_translate("Form", "Сохранить запись"))
        self.label_2.setText(_translate("Form", "Название сорта = "))
        self.label_3.setText(_translate("Form", "Степень обжарки = "))
        self.label_4.setText(_translate("Form", "Молотый/в зернах = "))
        self.label_5.setText(_translate("Form", "Описание вкуса = "))
        self.label_6.setText(_translate("Form", "Цена ="))
        self.label_7.setText(_translate("Form", "Вес упаковки ="))
        self.editButton.setText(_translate("Form", "Изменить запись"))
