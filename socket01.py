import socket
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
def fun01():
   t = textEdit.toPlainText()
   mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   mysocket.connect((t,80))
   cmd='GET http://t/romeo.txt HTTP/1.0\r\n\r\n'.encode()
   mysocket.send(cmd)
   while(1):
     data=mysocket.recv(512)
     if(len(data)<1):
        break
     QMessageBox.about(window,'数据：',data.decode()+" ")
   mysocket.close()


app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('socket')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("输入IP地址")
textEdit.move(10, 25)
textEdit.resize(480, 150)

button = QPushButton('确定', window)
button.move(190, 220)

window.show()

button.clicked.connect(fun01)

app.exec_()
