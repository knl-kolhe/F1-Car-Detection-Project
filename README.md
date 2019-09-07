# F1-Car-Detection-Project

## Technologies Used:
YOLO, darknet on Windows: https://github.com/AlexeyAB/darknet
Tensorflow
Python, Numpy
HTML
PHP
MySQL

## The Project:
This project aims to implement some of the technologies in the field of image processing to automatically bring live updates in the field of Car Racing, similar to cricbuzz to fans. There will be a low power device deployed on the race track which will capture the images of cars crossing the finish line and process the image. The device will correctly identify the object (the car) and detect the position of the Number on the car. That number will be recognised by a different model. It will then return the car number and the time the car crossed the finish line to a central server. The central server will display these values to everyone accessing it over the internet. The device deployed at the track needs to be connected to the server by only a low bandwidth connection as it is not streaming all the images to the central server, rather just sending inferences over the connection. 
The future applications of such a project can be at busy intersections and commuters can access real time data of their route over the internet. It can also help automatically identify rule breakers. 

## Keywords:
Machine Learning, Edge Computing, Image Processing, Object Detection, Text recognition.

## Models and Weights:
https://drive.google.com/open?id=1NAcTBC5KFNOIMBlMqn7PUmO6i4hn_q0u
Go to this drive and download all the files. Place them in a folder custom-2 in the repository. (You can change the name, I had used the named custom-2 for YOLO model as it was custom model number 2.
