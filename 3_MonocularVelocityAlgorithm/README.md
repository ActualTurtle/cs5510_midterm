# 3a. Implement the monocular velocity detection algorithm
## Capture and process data

Run 

``` /capture_process_data/record_image_clips.py --r```

then run with the file updated with the file path to the image clips

the below script takes the image clips and every 20th image it find the bb_box of where the object is in the image. It also saves annotation json of the bb_box for every 20th image. It also generates a text file that has a path to an image without a bb_box and then the second image path that has a bb_box of the object and the path to the annotation file for that image. ie: "/path/to/image1.jpg /path/to/image2.jpg /path/to/annotation.json" then it goes to the next line and that line is the next two images and annotation file to try and predict the velocity of the object.

Also need to download the yolov3.weights 
https://pjreddie.com/media/files/yolov3.weights

``` /capture_process_data/find_bb_box.py```


Run 

With the file update with proper paths

``` test_crop_velocity.py ``` 

#### Ran into issues trying to run

# 3b. Implement the Monocular Odometry algorithm

There are multiple ways to run the monocular odometry algorithm.
* live camera feed
* image clips

## Install dependencies
``` pip install -r requirements.txt ```

## Live camera feed
To run
``` visual_odemetry_live_camera_feed.py ```

When you first run the script it will look for a calibration file in the directory if it doesn't find the calibration file it will start running a calibration script. The calibration script will keep scanning for images with a 9 x 6 chessboard pattern. 

Once it has calibrated it will start running the visual odemetry from the live camera feed for a set amount of images. 

## Image clips
To run
``` visualodemetry_from_image_directory.py ```

When you first run the script it will look for a calibration file in the directory for the camera calibraion file of the captured images. 
It will then find all the image in the the /video/video directory with the images labeled as 1.png, 2.png, 3.png, etc.

Then it will save a map and a image of the map and the video of the images. 

