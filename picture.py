from imgtoascii import ImgPathToAscii

frameName = input("Image path: ")
asciiart = ImgPathToAscii(frameName, True)
file = open('asciiart.txt', 'w')
file.write(asciiart)
file.close()
