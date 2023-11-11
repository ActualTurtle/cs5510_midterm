import pathlib
import time
import json
import platform
import psutil
from fer import FER

'''
This script will be used to generate analysis data on different machines
'''
detector = FER()

# Images
img_dir = "frames"
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
    detector.detect_emotions(img) # run FER
    deltatime = time.time() - starttime
    totaltime += deltatime
    data["fps"]["times"].append(frames / totaltime) # current average  frames per second

data["cpu"]["average"] = sum(data["cpu"]["percents"]) / len(data["cpu"]["percents"])
data["fps"]["average"] = sum(data["fps"]["times"]) / len(data["fps"]["times"])

with open(f"data/{platform.system()}_{int(time.time())}.json", 'x') as json_file:
    json.dump(data, json_file)