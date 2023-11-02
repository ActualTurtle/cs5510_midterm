import matplotlib.pyplot as plt
import pathlib
import json

'''
Using json data generated from part_c.py, stored in "/part_c_data" plots, plots perfomance 
'''


data_dir = "part_c_data"

stats = {"cpu": {}, "fps": {}}

for data_path in pathlib.Path(data_dir).glob('*.json'):
    
    with open(data_path) as json_file:
        data = json.load(json_file)

        stats["cpu"][data_path] = data["cpu"]["percents"]
        stats["fps"][data_path] = data["fps"]["times"]


for cpu_stats_source in stats["cpu"]:
    plt.plot(stats["cpu"][cpu_stats_source], label=f"{cpu_stats_source}")

plt.xlabel("Image/Frames")
plt.ylabel("CPU Usage %")
plt.title("CPU performance")
plt.legend()
plt.show()


for fps_stats_source in stats["fps"]:
    plt.plot(stats["fps"][fps_stats_source], label=f"{fps_stats_source}")
  
plt.xlabel("Image/Frame")
plt.ylabel("Seconds")
plt.title("FPS/time performance")
plt.legend()
plt.show()