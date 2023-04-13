import spidev
import numpy as np
import matplotlib.pyplot as plt
import time
    
def ReadChannel(channel): 
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3)<<8)+adc[2]
    return data

enter = input("Enter y : ")
counter=0
while enter == "y":
    counter+=1
    print("Round : ",counter)
    spi = spidev.SpiDev()
    spi.open(0,0)
    spi.max_speed_hz = 550000
    channel = 0
    dbf = open('Data.txt', 'a')
    print('start')
    for i in range(12000):
        if i == 4000:
            print('Active')
        level = ReadChannel(channel)
        volt = level*5/1023
        dbf.write(str(volt)+',')
    spi.close()
    dbf.write('\n')
    dbf.close()
    print('complete')
    print("*********************")
    enter = input("Enter y: ")
