import sys
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
win = uic.loadUi("mahasiswa.ui")

win.show()
sys.exit(app.exec())