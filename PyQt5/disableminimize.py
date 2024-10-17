from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QDesktopWidget
from PyQt5 import QtCore

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Label1", self)
        self.label.move(200, 0)
        self.button = QPushButton("Button1", self)
        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle("Belajar PyQt5")
        cwa = self.frameGeometry()  # Cek ukuran main window app kita
        cwc = QDesktopWidget().availableGeometry().center()  # Pada screen saya: (682, 363)
        cwa.moveCenter(cwc)
        self.move(cwa.topLeft())
        self.setFixedSize(500, 500)  # Agar tidak bisa di-resize! Icon maximize juga akan otomatis hilang
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()