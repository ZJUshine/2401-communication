# 实现8位CRC校验
import os
import binascii
import crcmod.predefined

class CRCGenerator(object):
    def __init__(self):
        self.module = 'crc-8-maxim'
        
    def create(self,input):
       crc8 = crcmod.predefined.Crc(self.module)
       hexData = input
       print(hexData)
       hexData =binascii.unhexlify(hexData)
       crc8.update(hexData)
       result = hex(crc8.crcValue)
       print(result)
       return result

if __name__=="__main__":
    crc =CRCGenerator()
    crc.create('FF012345678901234567891234')
