import json
import cv2
import numpy as np

import os
cwd = os.getcwd()

# Load YOLOv3 weights and configuration
net = cv2.dnn.readNet(cwd+"/my-inteligence-robotics-repo/mono_velocity/my_modified_mono_velocity/yolov3.weights", cwd+"/my-inteligence-robotics-repo/mono_velocity/my_modified_mono_velocity/yolov3.cfg")

# Load COCO names
with open(cwd+"/my-inteligence-robotics-repo/mono_velocity/my_modified_mono_velocity/coco.names", "r") as f:
    classes = f.read().strip().split("\n")

tracklet_info = []
images_paths_annotations = ''
i = 0

twentieth_last_previous_path = None

fileNames =  os.listdir(cwd+'/my-inteligence-robotics-repo/mono_velocity/my_modified_mono_velocity/video')
fileNames.sort()

print("fileNames",fileNames)

for filename in fileNames:
    frame = cv2.imread(os.path.join(cwd+'/my-inteligence-robotics-repo/mono_velocity/my_modified_mono_velocity/video', filename))

    print("filename",filename)

    # print("right here",(i % 20))


    if frame is None:
        break

    if i == 0:
        twentieth_last_previous_path = filename


    # every 20 frames add the frame to the twentieth_last_previous_frame
    if i % 20 == 0 and i != 0:
        print('i: ', i)
    # Get the video frame dimensions
        (H, W) = frame.shape[:2]

        # Preprocess the frame and perform YOLOv3 object detection
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)
        layer_names = net.getUnconnectedOutLayersNames()
        detections = net.forward(layer_names)

        # Initialize lists to store detected cars' bounding boxes
        boxesInImage = []
        boxes = []
        confidences = []
        class_ids = []

        for detection in detections:
            for obj in detection:
                scores = obj[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.5 and classes[class_id] == "person":
                    # Calculate bounding box coordinates
                    center_x = int(obj[0] * W)
                    center_y = int(obj[1] * H)
                    width = int(obj[2] * W)
                    height = int(obj[3] * H)
                    x = int(center_x - width / 2)
                    y = int(center_y - height / 2)

                    boxesInImage.append({'bbox':{'left':x, 'top':y,'right':width, 'bottom':height}})
                    boxes.append([x, y, width, height])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Apply non-maximum suppression to remove duplicate detections
        # indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        # if len(indexes) > 0:
        #     for i in indexes.flatten():
        #         x, y, w, h = boxes[i]
        #         tracklet_info.append([x, y, x + w, y + h])

        #         # Draw bounding box and label
        #         # color = (0, 255, 0)  # Green color for cars
                # cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                # text = f"Car: {confidences[i]:.2f}"
                # cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # cv2.imshow("Car Detection", frame)
        # save the annotation to json file
        with open(cwd+'/my-inteligence-robotics-repo/mono_velocity/my_modified_mono_velocity/video/'+str(i)+'-annotation.json', 'w') as outfile:
            json.dump(boxesInImage, outfile)

        images_paths_annotations += '"'+ cwd+'/my-inteligence-robotics-repo/mono_velocity/my_modified_mono_velocity/video/'+twentieth_last_previous_path+'"'+' '+'"'+cwd+'/my-inteligence-robotics-repo/mono_velocity/my_modified_mono_velocity/video/'+filename +'"'+' '+'"'+cwd+'/my-inteligence-robotics-repo/mono_velocity/my_modified_mono_velocity/video/'+str(i)+'-annotation.json'+'"'+ '\n'
        twentieth_last_previous_path = filename


    i += 1

    # if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
    #     break

# Release the video capture and close all OpenCV windows
cv2.destroyAllWindows()

print("images_paths_annotations", images_paths_annotations)

#save the images_paths_annotations to a file
with open(cwd+'/my-inteligence-robotics-repo/mono_velocity/my_modified_mono_velocity/video/images_paths_annotations.txt', 'w') as outfile:
    outfile.write(images_paths_annotations)

# Save the tracklet information (bounding boxes) to a file or use it as needed
# You can save tracklet_info as a CSV file, JSON, or any other format you prefer
