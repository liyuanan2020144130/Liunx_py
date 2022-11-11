import socket
import os

def recvfile(conn):	
    filename = 'D:/test.txt'   #文件目录
    print('Receive the file sent by the client %s!'% filename)  #给出接收提示
    conn.send(filename.encode('utf-8'))   
    str1 = conn.recv(1024)  #将接收数据存入str1字符串中
    str2 = str1.decode('utf-8')#显示接收信息
    if str2 == 'no':
	    print('receive the file %s failed!'% filename)
       
    else:
	    conn.send(b'I am ready!')
	    temp = filename.split('/')  #将接收文件进行切片存入temp中
	    myname = 'my_' + temp[len(temp)-1]  #定义新的文件名
	    size = 1024   #指定长度

	    with open (myname,'wb') as f:  #以写打开文件
		    while True:
			    data = conn.recv(size)  
			    f.write(data)
			    if len(data) < size:
			       break
	    print('Then receive fileis %s'% myname)
 #conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建套接字，绑定地址
s.bind(('127.0.0.1',4582))  #指定ip地址和端口号
s.listen(1)   #最多允许1个端口监听
print('Waiting for connecting...')
(conn,addr) = s.accept()  #接收客户机发来的信息
while True:
	#(conn,addr) = s.accept()
	recvfile(conn)  #调用函数