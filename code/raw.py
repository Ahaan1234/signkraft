import numpy as np
import os
import cv2
import pandas as pd

data_location = 'data'                  # this is the location of the folder for the data
numpy_file_loc = "numpy_saved_data"     # This is the location to the numpy saved files


# x = np.array([100,20,30])
# print(x.argmax())



# import numpy as np

# arr = np.array([41, 42, 43, 44])

# filter_arr = arr > 42

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)


# cap = cv2.VideoCapture(0)

    
# width = cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
# height = cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)


# while True:
#     ret, frame = cap.read()
#     if not ret: break # break if no next frame
    
#     print(frame.shape)
    
#     cv2.imshow("win",frame) # show frame
    
#     if cv2.waitKey(1) & 0xFF == ord('q'): # on press of q break
#         break
        
# # release and destroy windows
# cap.release()
# cv2.destroyAllWindows()
