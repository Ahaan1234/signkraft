# This code is used to resize high quality video(1080p) into 480p
# make sure all the videos are inside a folder (set the folder name in the "word" variable)
# Make sure to manually create a folder for the output videos (set this new folder name in the "word_new" variable)
# Later manully delete the old video folder and rename the folder

import cv2
import numpy as np
from tqdm import tqdm
import os
import cv2

word = 'woman'
# word_new = 'no_resized'
# word_new = 'thank_you_resized'
word_new = word + '_resized'
# word_new = 'yes_resized'
os.mkdir('data/'+word+'_resized')

data_path = os.path.join('data',word)
print(word)

for i in tqdm(range(1,151)):
    
    vid_path = os.path.join(data_path,str(i)+'.avi')
    video = cv2.VideoCapture(vid_path)

    if (video.isOpened() == False):
        print("Error reading video file: "+str(i))

    frame_width = int(video.get(3))
    frame_height = int(video.get(4))

    new_size = (320,240)

    result = cv2.VideoWriter(os.path.join('data',word_new,str(i)+".avi"), cv2.VideoWriter_fourcc(*'MJPG'), 10, new_size)
        
    while(True):
        ret, frame = video.read()

        if ret == True:
            frame = cv2.resize(frame,new_size)
            result.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        else:
            break


    video.release()
    result.release()