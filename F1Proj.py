import RPi.GPIO as GPIO
import time
import picamera
import cv2
from darkflow.net.build import TFNet
import numpy as np
from picamera.array import PiRGBArray
from mysql.connector import MySQLConnection, Error
import mysql
from datetime import datetime

#hardware setup
camera=picamera.PiCamera()
camera.resolution=(640,480)
rawCapture=PiRGBArray(camera)
time.sleep(0.1)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
print('Hardware Setup Done')
GPIO.output(3,GPIO.LOW)
time.sleep(1)
GPIO.output(3,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)

#software setup
from keras.models import load_model    
model=load_model('custom-2/svhn-multi-digit-21-03-F1-run1.h5')

option = {
    'model': 'custom-2/yolo-obj.cfg',
    'load': 'custom-2/yolo-obj_2200.weights',
    'threshold': 0.30,
    'gpu': 1.0
}

tfnet = TFNet(option)

colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

mydb=mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="user",
    database="F1Track"
    )

mycursor=mydb.cursor()

print('ready')
GPIO.output(27,GPIO.LOW)
GPIO.output(3,GPIO.LOW)
time.sleep(1)
GPIO.output(3,GPIO.HIGH)
lapstart=datetime.now().strftime('%H:%M:%S')
while True:
    if GPIO.input(5)==GPIO.HIGH:
        i=1
        camera.capture(rawCapture, format="bgr")
        frame=rawCapture.array
        rawCapture.truncate(0)
        GPIO.output(3,GPIO.LOW)
        time.sleep(1)
        GPIO.output(3,GPIO.HIGH)
        #frame=cv2.imread("custom-2/"+str(i)+".jpg")
        frame=cv2.resize(frame,(640,480))
        lapend=datetime.now().strftime('%H:%M:%S')
        print('captured 1 image')
        cv2.imwrite('snapshot1.jpg',frame)
        results = tfnet.return_predict(frame)
        cv2.imwrite('snapshot1.jpg',frame)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            img=frame[tl[1]:br[1],tl[0]:br[0]]
            img=cv2.resize(img,(64,64))
            img=img[np.newaxis,...]
            res=model.predict(img)
            label=""
            if np.argmax(res[0])=='10':
                label=""
            label = label+str(np.argmax(res[1]))
            print(label)
            '''
            frame = cv2.rectangle(frame, tl, br, color, 7)
            frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imwrite('snapshot1_result.jpg',frame)
            cv2.imshow('frame', frame)
            cv2.waitKey(0);
            cv2.destroyAllWindows()
            '''
            sql="Insert Into Race2 (Car_No,lap_start_time,lap_end_time) Values (%s,%s,%s)"
            val = (label,lapstart,lapend)

            mycursor.execute(sql,val)

            mydb.commit()

            print(mycursor.rowcount,"record Inserted")
            GPIO.output(3,GPIO.LOW)
            time.sleep(1)
            GPIO.output(3,GPIO.HIGH)
            i=i+1
        GPIO.output(3,GPIO.LOW)
        time.sleep(1)
        GPIO.output(3,GPIO.HIGH)
    else:
        GPIO.output(27,GPIO.LOW)
        
