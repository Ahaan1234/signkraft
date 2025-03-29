
# make sure the time on all the machines match
# make sure you run the code on all the machines when the number of seconds shown is less than 10
# run the code once to get detail on the current machine time

# this will make sure you have 40 seconds to runn the code on all machines.
# the video recording starts when the timer reaches 0
# the video is going to be recorded fot just 2 second each at 20 frames per second

# we are recording just 60 videos for the time being

# Letter/word for which the images are being clicked
letter = 'test'

# number of frames (change this if you require more time per action)
# make sure the number of frames is same for all the actions then
num_frames = 40


import cv2
import pathlib
import os
import time
import ntplib
from datetime import datetime, timezone
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 50004))
s.listen(3)

conn = [0,0,0]

try:
    for i in range(3):
        conn[i], addr = s.accept()
        data = conn[i].recv(6)

        if data == b'Keyaan':
            print("Connected to Keyaan")
            # conn.sendall(data)

        if data == b'mac110':
            print("Connected to mac110")
            # conn.sendall(data)

        if data == b'Mac100':
            print("Connected to Mac100")
            # conn.sendall(data)
        
    l = conn[0].sendall(b'mac110')
    l = conn[1].sendall(b'Mac100')
    l = conn[2].sendall(b'Keyaan')

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

    time.sleep(1)

    count = 1
    while True:
        l = conn[2].sendall(b'Keyaan')
        l = conn[0].sendall(b'mac110')
        l = conn[1].sendall(b'Mac100')
        print(l)

        time.sleep(0.1)

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
        if count == 31:
            break



except KeyboardInterrupt as k:
    print('closing all connections, keyboard interrupt')
    cap.release()
    cv2.destroyAllWindows()
    conn[0].close()
    conn[1].close()
    conn[2].close()

except AttributeError as a:
    print('closing all connections, attribute error')
    cap.release()
    cv2.destroyAllWindows()
    conn[0].close()
    conn[1].close()
    conn[2].close()

except BrokenPipeError as b:
    print('closing all connections, broken pipe error')
    cap.release()
    cv2.destroyAllWindows()
    conn[0].close()
    conn[1].close()
    conn[2].close()
    
