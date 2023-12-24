import sqlite3
import sys

from functools import partial

from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtWidgets import QMainWindow

from addEditCoffeeForm_ui import SecondFormUi
from main_ui import FirstFormUi

# Коды операций
ADD = 0
DELETE = 1
CHANGE = 2


class FirstForm(QMainWindow, FirstFormUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.load_table()
        self.addButton.clicked.connect(partial(self.open_second_form, ADD))
        self.changeButton.clicked.connect(
            partial(self.open_second_form, CHANGE)
        )
        self.deleteButton.clicked.connect(
            partial(self.open_second_form, DELETE)
        )

    def load_table(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('data/coffee.sqlite')
        self.db.open()

        model = QSqlTableModel(self, self.db)
        model.setTable('Coffee')
        model.select()

        self.tableView.setModel(model)

    def open_second_form(self, mode):
        self.second_form = SecondForm(self, mode)
        self.second_form.show()


class SecondForm(QWidget, SecondFormUi):
    def __init__(self, first_form, mode):
        super().__init__()
        self.setupUi(self)
        self.first_form = first_form
        self.con = sqlite3.connect("data/coffee.sqlite")
        self.initUI(mode)

    def initUI(self, mode):
        # Видоизменяем 2-ю форму в зависимости от выбранной кнопки
        if mode == DELETE:
            self.addRowGroupBox.setVisible(False)
            self.addRowGroupBox.findChildren(QPushButton)[1].setVisible(False)
            self.deleteGroupBox.findChildren(QPushButton)[0].clicked.connect(
                self.delete_row
            )
            self.setFixedSize(600, 40)
        elif mode == ADD:
            self.deleteGroupBox.setVisible(False)
            self.addRowGroupBox.move(0, 0)
            self.addRowGroupBox.findChildren(QPushButton)[1].setVisible(False)
            self.addRowGroupBox.findChildren(QPushButton)[0].clicked.connect(
                self.add_row
            )
            self.setFixedSize(600, 170)
        elif mode == CHANGE:
            self.deleteGroupBox.findChildren(QPushButton)[0].setVisible(False)
            self.addRowGroupBox.findChildren(QPushButton)[0].setVisible(False)
            self.addRowGroupBox.findChildren(QPushButton)[1].clicked.connect(
                self.change_row
            )

    def delete_row(self):
        # Удаляем строку по ID
        cur = self.con.cursor()
        cur.execute("""DELETE from Coffee WHERE ID = ?""", (
            self.deleteGroupBox.findChildren(QLineEdit)[0].text(),
        ))
        self.con.commit()

        self.first_form.load_table()

        self.close()

    def change_row(self):
        # Заменяем строку по выбранному ID
        cur = self.con.cursor()
        cur.execute("""UPDATE Coffee 
                        SET 'название сорта' = ?, 
                            'степень обжарки' = ?, 
                            'молотый/в зернах' = ?, 
                            'описание вкуса' = ?, 
                            'цена' = ?, 
                            'вес упаковки' = ?
                        WHERE ID = ?""", (
            self.addRowGroupBox.findChildren(QLineEdit)[0].text(),
            self.addRowGroupBox.findChildren(QLineEdit)[1].text(),
            self.addRowGroupBox.findChildren(QLineEdit)[2].text(),
            self.addRowGroupBox.findChildren(QLineEdit)[5].text(),
            self.addRowGroupBox.findChildren(QLineEdit)[4].text(),
            self.addRowGroupBox.findChildren(QLineEdit)[3].text(),
            self.deleteGroupBox.findChildren(QLineEdit)[0].text()
        ))
        self.con.commit()
        cur.close()

        self.first_form.load_table()

        self.close()

    def add_row(self):
        # Тут получаем самый большой индекс и прибавляем единичку,
        # иначе берем 1 как начальный индекс
        cur = self.con.cursor()
        id_collection = list(map(
            lambda x: x[0],
            cur.execute("""SELECT ID FROM Coffee""").fetchall()
        ))
        cur_id = 1 if not id_collection else max(id_collection) + 1

        cur.execute("""INSERT INTO Coffee(
                'ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                'описание вкуса', 'цена', 'вес упаковки'
            ) VALUES(?, ?, ?, ?, ?, ?, ?)""", (
            cur_id,
            self.addRowGroupBox.findChildren(QLineEdit)[0].text(),
            self.addRowGroupBox.findChildren(QLineEdit)[1].text(),
            self.addRowGroupBox.findChildren(QLineEdit)[2].text(),
            self.addRowGroupBox.findChildren(QLineEdit)[5].text(),
            self.addRowGroupBox.findChildren(QLineEdit)[4].text(),
            self.addRowGroupBox.findChildren(QLineEdit)[3].text()
        ))
        self.con.commit()
        cur.close()

        self.first_form.load_table()

        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())
