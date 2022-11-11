import socket
import os

def sendfile(s):
    str1 = s.recv(1024)  
    filename = str1.decode('utf-8')
    print(' Send file to server:',filename)
    if os.path.exists(filename):   #判断文件是否存在
        print('I have %s, begin to send!' % filename)
        s.send(b'yes')
        s.recv(1024)  #指定接收数据长的
        size = 1024
        with open(filename,'rb') as f:  #以读的方式打开文件
           while True:
              data = f.read(size)  #读取数据赋值给data
              s.send(data)   #发送数据给服务器
              if len(data) < size:  #比较data的长度
                  break
        print('%s is Sending succeeded!' % filename)
    else:
       print('Sorry, I have no %s' % filename)
       s.send(b'no')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #创建套接字，绑定地址
s.connect(('127.0.0.1',4582))   #指定ip地址和端口号
#filename = 'D:/test.txt'
while 1:
	
    sendfile(s)  #调用函数