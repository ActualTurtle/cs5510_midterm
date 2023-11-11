import torch
import pathlib
import time
from ultralytics import YOLO
from PIL import Image

'''
Part B

Using Yolov5s via torchhub and yolov8n via ultralytics. Passing the same 100 images through both models and comparing the 
differences in accuracy and speed

images save in "part_b_detections/yolo{version_num}/img"

Based on a previous run
YOLO v5 time for classify 100 images: 35.92656707763672 seconds
YOLO v8 time for classify 100 images: 22.250749111175537 seconds


'''

# Model
model_v5 = torch.hub.load("ultralytics/yolov5", "yolov5s")
model_v8 = YOLO("yolov8n.pt")

# Images
img_dir = "img/grocerystore"
images = [str(img_path) for img_path in pathlib.Path(img_dir).glob('*.jpg')]

# Inference
starttime = time.time()
results_v5 = model_v5(images)
time_v5 = time.time() - starttime

starttime = time.time()
results_v8 = model_v8(images)
time_v8 = time.time() - starttime

# Results
results_v5.save(save_dir=f"part_b_detections/yolo5/img") # Save yolov5 images

for i in range(len(results_v8)): # Save yolov8 images
    im_array = results_v8[i].plot() 
    im = Image.fromarray(im_array[..., ::-1])  
    im.save(f"part_b_detections/yolo8/img/{str(images[i]).split('/')[2].split('.')[0]}.jpg", )  # save image

print()
print(f"YOLO v5 time for classify 100 images: {time_v5} seconds")
print(f"YOLO v8 time for classify 100 images: {time_v8} seconds")
