from datetime import datetime, timezone
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
def function():

    t = textEdit.toPlainText()

    ts_epoch=int(t)

    ts = datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%d %H:%M:%S')

    QMessageBox.about(window,'转换后为',ts)
    	
app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('纪元转化')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("输入所需秒数")
textEdit.move(10, 25)
textEdit.resize(300, 350)

button = QPushButton('转换', window)
button.move(380, 80)

window.show()

button.clicked.connect(function)

app.exec_()

