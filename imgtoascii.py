from PIL import Image
import math

def ImgToAscii(imgPath) -> str:
    chars = '.\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

    img = Image.open(imgPath)
    img_width = 100
    width_percent = (img_width/float(img.size[0]))
    img_height = int((float(img.size[1])*float(width_percent)))
    img = img.resize((img_width,img_height), Image.Resampling.LANCZOS)
    width, height = img.size

    art = ''
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            brightness = (r+g+b)/3
            scaled_brightness = brightness/256
            char_index = math.floor(scaled_brightness * len(chars))
            if char_index >= len(chars):
                print('char index out of bounds')
                print(scaled_brightness, char_index, len(chars))
                return ''
            char = chars[char_index]
            art += char*2
        art += '\n';

    return art