from PyQt5 import QtWidgets , uic
application=QtWidgets.QApplication([])
dialog=uic.loadUi("test.ui")

def Change():
    dialog.label.setText("Hello World!.....")
dialog.pushButton.clicked.connect(Change)
dialog.show()
application.exec()
