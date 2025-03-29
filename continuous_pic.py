# press the 'q' key to close the appplication
import cv2
import pathlib
import os
import time



# Letter for which the images are being clicked
letter = 'A'


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


time.sleep(3)

count = 1
while True:
    # read the frames from the camera
    ret,frame = cap.read()
    
    # quit when the 'q' key is presses
    if cv2.waitKey(50) == ord('q'):
        break
    
    # show the image window
    cv2.imshow('win',frame)
    
    img_path = os.path.join(letter_path,str(count))
    
    # save the image
    cv2.imwrite(img_path+".jpg",frame)
    
    # increase the counter
    count = count+1
    if count == 1001:
        break
    
cv2.destroyAllWindows()
    