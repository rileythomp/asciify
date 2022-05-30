from PIL import Image
import math

Chars = '.\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
CharsLen = len(Chars)


def brightnessToChar(brightness: float) -> str:
    scaled_brightness = brightness/256
    char_index = math.floor(scaled_brightness * CharsLen)
    if char_index >= CharsLen:
        print('char index out of bounds')
        print(scaled_brightness, char_index, CharsLen)
        return ''
    char = Chars[char_index]
    return char

def getAsciiDimensions(imgPath: str):
    img = Image.open(imgPath)
    img_width = 100
    width_percent = (img_width/float(img.size[0]))
    img_height = int((float(img.size[1])*float(width_percent)))
    img = img.resize((img_width,img_height), Image.Resampling.LANCZOS)
    width, height = img.size
    return img, width, height

def ImgToAscii(imgPath) -> str:
    img, width, height = getAsciiDimensions(imgPath)
    art = ''
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            # luminosity
            brightness =  0.2126*r + 0.7152*g + 0.0722*b
            # brightness = (r+g+b)/3
            # lightness
            # brightness = (max(r, g, b)+min(r, g, b)) / 2
            # luminosity perceived 1
            # brightness = 0.299*r + 0.587*g + 0.114*b
            # luminosity perceived 2
            # brightness = math.sqrt( 0.299*r*r + 0.587*g*g + 0.114*b*b )
            char = brightnessToChar(brightness)
            art += char*2
        art += '\n';
    return art