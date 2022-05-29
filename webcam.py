import cv2 as cv
from imgtoascii import ImgToAscii
import os

# run watch -n 0.1 cat asciiart.txt in a separate terminal to see output
def strToFile(str: str, filename: str):
    file = open(filename, 'w')
    file.write(str)
    file.close()

frameName = 'frame.jpg'

cam = cv.VideoCapture(0)
print('press q to stop webcam')
while (True):
    retval, frame = cam.read()
    cv.imshow('Ascii Art', frame)
    cv.imwrite(frameName, frame)
    asciiart = ImgToAscii(frameName)
    print(asciiart)
    strToFile(asciiart, 'asciiart.txt')
    os.remove(frameName)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
