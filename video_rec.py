# make sure the time on all the machines match
# make sure you run the code on all the machines when the number of seconds shown is less than 10
# run the code once to get detail on the current machine time

# this will make sure you have 40 seconds to runn the code on all machines.
# the video recording starts when the timer reaches 0
# the video is going to be recorded fot just 2 second each at 20 frames per second

# we are recording just 60 videos for the time being

# Letter/word for which the images are being clicked
letter = 'Hello'

# number of frames (change this if you require more time per action)
# make sure the number of frames is same for all the actions then
num_frames = 40


import cv2
import pathlib
import os
import time
import ntplib
from datetime import datetime, timezone


# c = ntplib.NTPClient()
# Provide the respective ntp server ip in below function
# response = c.request('pool.ntp.org', version=3)
# t = datetime.fromtimestamp(response.tx_time, timezone.utc)
t = datetime.now()
print(t.second)


x = pathlib.Path(__file__).parent.resolve()
print(x) 

path = os.path.join(x,'dataset')
print(path) 
if not os.path.isdir(path):
    os.mkdir(path)

letter_path = os.path.join(path,letter)
print(letter_path) 
if not os.path.isdir(letter_path):
    os.mkdir(letter_path)


cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

time.sleep(3)

while True:
    if t.second>49:
        break
    time.sleep(0.2)
    # response = c.request('pool.ntp.org', version=3)
    t = datetime.now()
    print(50-t.second)
    

count = 1
while True:
    img_path = os.path.join(letter_path,str(count))
    out = cv2.VideoWriter(img_path+".avi", cv2.VideoWriter_fourcc(*'MJPG'), num_frames, (frame_width,frame_height))
    
    for i in range(num_frames):
        # read the frames from the camera
        ret,frame = cap.read()
        
        # quit when the 'q' key is presses
        if cv2.waitKey(50) == ord('q'):
            break
        
        # save the video
        out.write(frame)
        
        cv2.putText(frame, 'Video count: '+str(count), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)
        cv2.putText(frame, 'frame count: '+str(i), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)
        
        
        # show the image window
        cv2.imshow('win',frame)
        
    out.release()
    
    # increase the counter
    count = count+1
    if count == 61:
        break



cap.release()
cv2.destroyAllWindows()