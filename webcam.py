import cv2 as cv
from imgtoascii import ImgToAscii
import os

FrameName = 'frame.jpg'

# run watch -n 0.1 cat asciiart.txt in a separate terminal to see output
def strToFile(str: str, filename: str):
    file = open(filename, 'w')
    file.write(str)
    file.close()

def outputAsciiArt(art: str, filename: str):
    print(art)
    strToFile(art, filename)



cam = cv.VideoCapture(0)
print('press q to stop webcam')
while (True):
    retval, frame = cam.read()
    if retval:
        cv.imshow('Ascii Art', frame)
        cv.imwrite(FrameName, frame)
        asciiart = ImgToAscii(FrameName)
        outputAsciiArt(asciiart, 'asciiart.txt')
        os.remove(FrameName)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print('error recording webcam frame')
        break

cam.release()
cv.destroyAllWindows()
