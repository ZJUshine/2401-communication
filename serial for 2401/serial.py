#  -*- coding: utf-8 -*
# 用来检验串口发送的数据是否正确并且写入文件
import serial
import time
import os
import binascii
import crcmod.predefined

class CRCGenerator(object):
    def __init__(self):
        self.module = 'crc-8-maxim'
        
    def create(self,input):
       crc8 = crcmod.predefined.Crc(self.module)
       hexData = input
       hexData =binascii.unhexlify(hexData)
       crc8.update(hexData)
       #result = hex(crc8.crcValue)
       #return result
       return crc8.crcValue

if __name__=="__main__":
    crc =CRCGenerator()
    ok = 0
    
    while ok == 0:
        try:
            ser = serial.Serial("/dev/ttyUSB0", 115200,timeout = 20)
            ok = 1
        except:
            pass
    num=0
    ser.write(b'0')
    while True:
        test = ser.read(1)
        print(test)
        if test==b'\xff':
            test = ser.read(1)
            if test==b'\x02':
                break
    char = ser.read(23)
    start = time.clock()
    while True:
        
        char= ser.read(25)
        print(char)
        #for i in range (24):
        char1=char[:24]
        char2=char1.hex()
        crcbit8=crc.create(char2)
        print(crcbit8)
        print(char[-1])
        #print(type(char[-1]))
        #print(type(crcbit8))
        f = open('test.txt', 'a')
        for i in range (25):
            f.write(str(char[i]))
        #f.write(str(char))
        f.write("\n")
        if char[-1]==crcbit8:
            print("accurate crc!")
            #f.write("accurate crc!\n")
        else:
            print("error!")
            #f.write("error!\n")
        char3 = char[0]
        #print(str(char3))
        if char3==255:
            num=num+1
            print('number=%d'% num)
            f.write('number=%d\n'% num)
        else:
            print("title error!")
            #f.write("title error!\n")
        f.close()
        end = time.clock()
        print("final is in ", end - start)
        start = time.clock()

            
        
    


