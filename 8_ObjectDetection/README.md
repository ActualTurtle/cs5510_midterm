# 8. (20 points) Object Detection (Please put the classified images as part of your submission)

to install dependencies
```
pip install -r requirements.txt
```


### (a) (5 points) Classify the 100 images in the Store category from https://web.mit.edu/torralba/www/indoor.html using any image classification algorithm (not YOLO). ultralytics/yolo5

See [```part_a.py```](part_a.py)

See [```part_a_classifications```](part_a_classifications)

Withing ```part_a.py``` we load a Roboflow 2.0 model that has been trained to classify indoor scenes. We use said model to classify the images stored within ```img/grocerystore```. The images with classifications, as well as the raw data can be found in ```part_a_classifications```. 

### (b) (5 points) Do the same with comparing 2 YOLO versions:

See [```part_b.py```](part_b.py)

See [```part_b_detections```](part_b_detections)

Within ```part_b.py``` we run both Yolov5s and Yolov8n on the same images as part a. The processed images with bounding boxes can be found within ```part_b_detections/yolo*/iimg```.

### (c) (10 points) Deploy a YOLO model on a Raspberry Pi. What is the effective per- formance you get on the same datasets? Build a chart of performance showing the speed (FPS) and CPU usage between your pi and the standard use computer you are using (hopefully not a pi). Note: Please add the specs of the comparison device.

See [```part_c.py```](part_c.py)

See [```part_c_plot.py```](part_c_plot.py)

```part_c.py``` used to generate data for the plots. ```part_c_plot.py``` plots the data.
