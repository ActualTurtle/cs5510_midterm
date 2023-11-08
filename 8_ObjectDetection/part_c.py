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

frames = 0
totaltime = 0
cpusnaps = []

for img in images:

    frames += 1
    cpusnaps.append(psutil.cpu_percent())
    data["cpu"]["percents"].append(sum(cpusnaps) / len (cpusnaps))
    starttime = time.time()
    model_v5(img) # run yolov5
    deltatime = time.time() - starttime
    totaltime += deltatime
    data["fps"]["times"].append(frames / totaltime) # currenlt average  frames per second

data["cpu"]["average"] = sum(data["cpu"]["percents"]) / len(data["cpu"]["percents"])
data["fps"]["average"] = sum(data["fps"]["times"]) / len(data["fps"]["times"])

with open(f"part_c_data/{platform.system()}_{int(time.time())}.json", 'w') as json_file:
    json.dump(data, json_file)
