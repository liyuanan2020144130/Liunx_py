from socket import *
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox

def function():
	
  IP = ''
  PORT = 50000
  BUFLEN = 512

  listenSocket = socket(AF_INET,SOCK_STREAM)
  listenSocket.bind((IP,PORT))

  listenSocket.listen(8)
  QMessageBox.about(window,'服务器',f'服务器启动成功，在{PORT}端口等待客户端连接...')

  dataSocket,addr =listenSocket.accept()
  QMessageBox.about(window,'接受一个客户端连接:',addr)

  while True:
	  receved = dataSocket.recv(BUFLEN)

	  if not receved:
		  break

	  info = receved.decode()
	  print(f'收到对方的消息：{info}')

	  dataSocket.send(f'服务端接收到了信息:{info}'.encode())

  listenSocket.close()
  dataSocket.close()


app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('server')

#textEdit = QPlainTextEdit(window)
#textEdit.setPlaceholderText("输入IP号")
#textEdit.move(10, 25)
#textEdit.resize(300, 350)

button = QPushButton('启动', window)
button.move(180, 80)

window.show()

button.clicked.connect(function)
app.exec_()

