from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Label1", self)
        self.label.move(200, 0)
        self.button = QPushButton("Button1", self)
        self.setGeometry(0, 0, 400, 400)
        self.setWindowTitle("Belajar PyQt5")
app = QApplication([])
window = MyWindow()
window.show()
app.exec_()