import sys
from os import remove
import wget
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from message import Message
import mainForm

import json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True
#http://kappa.cs.petrsu.ru/~dimitrov/cross2020/test.json
class MainScreen(QtWidgets.QMainWindow, mainForm.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.download_clicked)
        self.pushButton_2.clicked.connect(self.save_clicked)

    def download_clicked(self):
        url = self.lineEdit.text()
        try:
            wget.download(url, "tmp.txtasdasdasd")
        except:
            self.textEdit.setText("Ошибка получения файла")
        try:
            f = open("tmp.txtasdasdasd", 'r')
            self.textEdit.setText(f.read())
            f.close()
            remove("tmp.txtasdasdasd")
        except:
            self.textEdit.setText("Ошибка чтения файла")

    def save_clicked(self):
        self.mes = Message()
        fileName, _ = QFileDialog.getSaveFileName(self, "Сохранить файл",  "",
                                                  "All Files (*);;Json files (*.json)")
        if fileName:
            if validateJSON(self.textEdit.toPlainText()):
                f = open(fileName, 'w')
                f.write(self.textEdit.toPlainText())
                self.mes.label.setText("Файл сохранён")
                self.mes.show()
            else:
                self.mes.label.setText("Файл не соответствует формату JSON")
                self.mes.show()
        



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainScreen()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
