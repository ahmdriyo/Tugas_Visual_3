from PyQt5.QtWidgets import QApplication, QPushButton,QLabel,QMainWindow

app = QApplication([])
window = QMainWindow()

# ini label
# label = QLabel(window)
label = QLabel("label", window)
# label.setText("Label")
label.move(200, 20)
button = QPushButton("Ini Button", window)
button.move(10, 20)

window.show()
app.exec_()