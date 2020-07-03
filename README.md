# Sem-3-Project
Self Driving Car Virtual Simulation on gta_5

The Project basically aims to provide a stimulation of driverless car in virtual environment i.e. in the game GTA5. The car will run on its own, will detect the obstacles coming in its way( trees, lampposts, people etc) and will save itself from colliding with them.


The Self Driving Car GTA5 module is been divided into 3 parts: 
1. Object Detection Module 
2. Model Training Module 
3. Lane detection Module 
 So, in first we implemented Object Detection Module using model version ssd_mobilenet_v1_coco_2017_11_17.
In second we implemented Model Training Module using model version alexnetv2-10-epochs-300K-data.model After 6-8 hours of training the model the car was finally able to run smoothly.
In third we implemented Lane Detection Module. The frames are first captured by OpenCV and then are took it into the gray scale mode so as to detect the left and right lanes of the driver. 

