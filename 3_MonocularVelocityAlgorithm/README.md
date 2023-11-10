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


# 3b.