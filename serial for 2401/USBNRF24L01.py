#  -*- coding: utf-8 -*
# 可以实现树莓派从串口读取机器人数据后通过串口上的USBNRF24L01模块发送数据
import serial
import time
# ser0 = serial.Serial("/dev/ttyUSB0", 115200,timeout = 1)
ser0 = serial.Serial("/dev/ttyUSB1", 115200,timeout = 1)
i=0
# while True:
#     test = ser1.read(1)
#     print(test)
#     if test==b'\xff':
#         test = ser1.read(1)
#         if test==b'\x02':
#             break
# char = ser1.read(23)
while True:
#     char=ser1.read_all()
    char =ser0.read(25)
#     print(char)
#     ser0.write(char)
    #ser0.write(b'h')
#     char="1234567890123456789012345"
#     i=i+1
    #print(i)
#     if i % 100 == 0:

#         end = time.time()
#         print("100 pac : ",end - start)
#         i = 0
#         start = time.time()
    print(char)
    time.sleep(0.1)
    