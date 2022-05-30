from imgtoascii import ImgToAscii

frameName = input("Image path: ")
asciiart = ImgToAscii(frameName, True)
file = open('asciiart.txt', 'w')
file.write(asciiart)
file.close()
