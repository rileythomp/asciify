import cv2 as cv
from imgtoascii import ImgToAscii
import os

frameName = 'frame.jpg'

cam = cv.VideoCapture(0)
print('press q to stop webcam')
while (True):
    retval, frame = cam.read()
    cv.imshow('Ascii Art', frame)
    cv.imwrite(frameName, frame)
    asciiart = ImgToAscii(frameName)
    file = open('asciiart.txt', 'w')
    file.write(asciiart)
    file.close()
    os.remove(frameName)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
