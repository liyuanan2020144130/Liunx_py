from socket import *
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox

def function():
   IP = '127.0.0.1'
   SERVER_PORT = 50000
   BUFLEN = 1024

   dataSocket = socket(AF_INET, SOCK_STREAM)

   dataSocket.connect((IP, SERVER_PORT))

   while True:
       toSend = input('>>>')
       if toSend == 'exit':
           break
       dataSocket.send(toSend.encode())

       receved = dataSocket.recv(BUFLEN)
       if not receved:
           break
       print(receved.decode())

   dataSocket.close()

app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('client')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("输入所要发送内容")
textEdit.move(10, 25)
textEdit.resize(300, 350)

button = QPushButton('发送', window)
button.move(380, 80)

window.show()

button.clicked.connect(function)

app.exec_()
