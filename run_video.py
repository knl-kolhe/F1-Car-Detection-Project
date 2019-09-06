# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 01:36:25 2018

@author: Kunal
"""

import cv2
from darkflow.net.build import TFNet
import numpy as np
import time

from keras.models import load_model    
model=load_model('custom-2/svhn-multi-digit-24-09-F1-ds.h5')

option = {
    'model': 'custom-2/yolo-obj.cfg',
    'load': 'custom-2/yolo-obj_2200.weights',
    'threshold': 0.30,
    'gpu': 1.0
}

tfnet = TFNet(option)

capture = cv2.VideoCapture('test.mp4')
colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

while (capture.isOpened()):
    stime = time.time()
    ret, frame = capture.read()
    if ret:
        results = tfnet.return_predict(frame)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            img=frame[tl[1]:br[1],tl[0]:br[0]]
            img=cv2.resize(img,(64,64))
            img=img[np.newaxis,...]
            res=model.predict(img)
            label = str(np.argmax(res[0]))+","+str(np.argmax(res[1]))
            frame = cv2.rectangle(frame, tl, br, color, 7)
            frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow('frame', frame)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        capture.release()
        cv2.destroyAllWindows()
        break