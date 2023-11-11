import argparse
import cv2
import time
import os
# from cropvelocity import *

cwd = os.getcwd()


def record_images():

    # use opencv to record images to the folder video
    # sleep 5 seconds
    time.sleep(5)

    cap = cv2.VideoCapture(0)
    i = 0
    while i<100:
        ret, frame = cap.read()
        # cv2.imshow('frame', frame)
        # if cv2.waitKey(1) == ord('q'):
        #     break
        cv2.imwrite(cwd+'/my-inteligence-robotics-repo/mono_velocity/my_modified_mono_velocity/video'+'/%d.jpg' % i, frame)
        i += 1
        # sleep 0.1 second
        time.sleep(0.1)
    cap.release()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PyTorch Monocular Depth Estimation')
    parser.add_argument('--r', '--record', action='store_true', help='record the video')


    args = parser.parse_args()
    print(args.r)
    print(args.i)
    if args.r:
        print("There is a 5 second delay before recording starts")
        record_images()