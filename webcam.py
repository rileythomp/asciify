import cv2 as cv
from imgtoascii import ImgToAscii
import os

# run watch -n 0.1 cat asciiart.txt in a separate terminal to see output

FrameName = 'frame.jpg'

cam = cv.VideoCapture(0)
print('press q to stop webcam')
while (True):
    retval, frame = cam.read()
    if retval:
        cv.imshow('Ascii Art', frame)
        cv.imwrite(FrameName, frame)
        asciiart = ImgToAscii(FrameName)
        file = open('asciiart.txt', 'w')
        file.write(asciiart)
        file.close()
        os.remove(FrameName)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print('error recording webcam frame')
        break

cam.release()
cv.destroyAllWindows()
