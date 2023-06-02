# 树莓派通过socket发送数据程序
import socket
import serial
import time
ser0 = serial.Serial("/dev/ttyUSB0", 115200,timeout = 20)
i=0
print("客户端开启")
# 套接字接口
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置ip和端口
host = '192.168.10.204'
port = 2222

try:
    mySocket.connect((host, port))  ##连接到服务器
    print("连接到服务器")
except:  ##连接不成功，运行最初的ip
    print('连接不成功')

while True:
    start = time.clock()
    # 发送消息
    msg = ser0.readline(25)
    #msg = input("客户端发送:")
    # 编码发送
    #mySocket.send(msg.encode("utf-8"))
    mySocket.send(msg)
    print(msg)
    print("发送完成%d"%i)
    i=i+1
    end = time.clock()
    print(end - start)
    if msg == "close":
        mySocket.close()
        print("程序结束\n")
        exit()
print("程序结束\n")