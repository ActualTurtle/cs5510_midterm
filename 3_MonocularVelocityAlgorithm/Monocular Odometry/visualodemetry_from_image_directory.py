import cv2
import numpy as np
from calibration import Calibration
from monovideoodometery_modified import MonoVideoOdometery
import os

cwd = os.getcwd()


try:
    config = np.load(cwd+'/calibration_params.npz')
    print('calibration file found')
    # read in the calibration file
    mtx = config['mtx']
    dist = config['dist']
    rvecs = config['rvecs']
    tvecs = config['tvecs']

except:
    print('calibration file not found')
    # Calibration().calibrate_camera()
    # config = np.load(cwd+'/calibration_params.npz')
    # print('calibration file found')
    # # read in the calibration file
    # mtx = config['mtx']
    # dist = config['dist']
    # rvecs = config['rvecs']
    # tvecs = config['tvecs']



lk_params = dict( winSize  = (21,21),
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 30, 0.01))


i = 1

visualOdemetry = MonoVideoOdometery(pose=None,cameraMatrix=mtx, distortionCoefficients=dist)

# get the first image from folder video/video/frame1.png
frame = cv2.imread(cwd+'/video/video/1.png')
visualOdemetry.old_frame = frame

traj = np.zeros(shape=(600, 800, 3))

every = 100
frames = []
record_map = True
# while(capture.isOpened()):
while(i < 4999):
    filepath = cwd+'/video/video/' + str(i+1) + '.png'
    frame = cv2.imread(filepath)
     # save frame to folder called video
    frames.append(frame)

    visualOdemetry.process_frame(frame,i)
    mono_coord = visualOdemetry.get_mono_coordinates()
    # print mono_coord everym 100 frames
    if i % every == 0:
        print(mono_coord)

    draw_x, draw_y, draw_z = [int(round(x)) for x in mono_coord]
    traj = cv2.circle(traj, (draw_x + 40, draw_z + 10), 1, list((0, 255, 0)), 4)
    cv2.putText(traj, 'Estimated Odometry Position:', (30, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255), 1)
    cv2.putText(traj, 'Green', (270, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 255, 0), 1)

    i +=1
cv2.imwrite('map2.png', traj)

height, width = frames[0].shape[:2]
print("height")
print(height)
print("width")
print(width)

video = cv2.VideoWriter('video-multiple-loops.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, (width,height))
for i in range(len(frames)):
    video.write(frames[i])

cv2.destroyAllWindows()
video.release()