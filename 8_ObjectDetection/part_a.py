from roboflow import Roboflow
import pathlib
import json

'''
Part A

Using a Roboflow 2.0 classification algorithm https://universe.roboflow.com/popular-benchmarks/mit-indoor-scene-recognition, 
classify first 100 images in 'img/grocerystore', images from https://universe.roboflow.com/popular-benchmarks/mit-indoor-scene-recognition
'''

NUM_IMAGES = 100
rf = Roboflow(api_key="L5rJOX5ls15IZp7PvFtH")
project = rf.workspace().project("mit-indoor-scene-recognition")
model = project.version(5).model


count = 0
data = {}
img_dir = "img/grocerystore"
for image_path in pathlib.Path(img_dir).glob('*.jpg'):
    if (count >= NUM_IMAGES):
        break
    img_name = str(image_path).split("/")[2].split(".")[0]

    pred = model.predict(str(image_path))
    data[img_name] = pred.json()
    pred.save(f"part_a_classifications/img/{img_name}_prediction.jpg")
    count += 1


with open("part_a_classifications/classifications.json", 'w') as json_file:
    json.dump(data, json_file)

print(f"Classified {count} Images")