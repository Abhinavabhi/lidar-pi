import serial
import RPi.GPIO as GPIO
import time
import numpy as np
GPIO.cleanup()
mean1=0
mean2=0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
msum=np.ones(180,dtype=float)
dist=np.zeros(181,dtype=float)
pos=np.zeros(181,dtype=int)
arduino=serial.Serial('/dev/ttyUSB0',9600)
arduino.setDTR(False)
time.sleep(2)
arduino.setDTR(True)
with arduino:
    while True:
        values=arduino.readline().split('p')
        if(len(values)==2):
            h=int(values[1])
            if(h==0):
                while True:
                    values=arduino.readline().split('p')
                    dist[int(values[1])]=int(values[0])
                    h=int(values[1])
                    
                    if(h==180):
                        
                        mean1=np.mean(dist[0:90])
                        mean2=np.mean(dist[91:180])
                        mean=(mean1+mean2)/2
                        if(((mean1+mean2)/2)>=250):
                            print('straight')
                        ##print mean
                        for x in range(0,142):
                            for y in range(0,39):
                                msum[x]=msum[x]*dist[x+y]
                        val=np.argmax(msum)+20
                        
                        print 'index=',val
                        print 'mean1=',mean1
                        print 'mean2=',mean2
                        if(val>90):
                            print 'right'
                        if(val<=90 and mean2>=mean1):
                            print 'right'
                            GPIO.output(11,True)
                            GPIO.output(10,True)
                        if(val<=90 and mean1>=mean2):
                            
                            print 'left'
                        
                            GPIO.output(10,True)
                            GPIO.output(11,True)
                        
                        #print val
                        msum=np.ones(180,dtype=float)
                   
                       
                        
                      

              
                

       
                
      
                
                    
                
        
