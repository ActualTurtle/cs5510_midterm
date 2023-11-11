import cv2

'''
Used only for generation of images for perfomance check
'''


# Open the video file
video_capture = cv2.VideoCapture("../VideoFER/content/random_faces.mp4")

# Initialize a frame counter
frame_count = 0

# Read and save frames as JPEG images
while True:
    success, frame = video_capture.read()
    
    if not success:
        break
    
    # Save the frame as a JPG image
    image_filename = f"frame_{frame_count:04d}.jpg"
    cv2.imwrite(f"frames/{image_filename}", frame)
    
    frame_count += 1

# Release the video capture object
video_capture.release()
