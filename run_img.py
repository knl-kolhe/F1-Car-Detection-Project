# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 01:59:13 2018

@author: Kunal
"""

import cv2
from darkflow.net.build import TFNet
import numpy as np


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
frame=cv2.imread("custom-2/snapshot.jpg",1)
frame=cv2.resize(frame,(640,480))
#frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

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
    frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            
cv2.imshow('frame', frame)
cv2.waitKey(0);
cv2.destroyAllWindows()

from keras import backend as K
K.clear_session()
