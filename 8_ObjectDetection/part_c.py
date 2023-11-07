import pathlib
import time
import json
import platform
import psutil
import torch

'''
This script will be used to generate analysis data on different machines
'''
model_v5 = torch.hub.load("ultralytics/yolov5", "yolov5s")

# Images
img_dir = "img/grocerystore"
images = [str(img_path) for img_path in pathlib.Path(img_dir).glob('*.jpg')]

data = {}
data["cpu"] = {}
data["cpu"]["percents"] = []
data["fps"] = {}
data["fps"]["times"] = []

for img in images:

    data["cpu"]["percents"].append(psutil.cpu_percent())
    starttime = time.time()
    model_v5(img)
    data["fps"]["times"].append(time.time() - starttime)

data["cpu"]["average"] = sum(data["cpu"]["percents"]) / len(data["cpu"]["percents"])
data["fps"]["average"] = sum(data["fps"]["times"]) / len(data["fps"]["times"])

with open(f"part_c_data/{platform.system()}_{int(time.time())}.json", 'w') as json_file:
    json.dump(data, json_file)
