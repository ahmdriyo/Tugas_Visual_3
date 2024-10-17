from PyQt5.QtWidgets import QApplication, QPushButton,QLabel,QMainWindow, QWidget

class MyWIndow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.label = QLabel(self)
    self.label.setText("Label")
    self.label.move(10,10)
    self.button = QPushButton(self)
    self.button.setText("Button")
    
    
    
app = QApplication([])
window = MyWIndow()
window.show()
app.exec_()