from PIL import Image
import math

chars = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'.'
chars = chars[::-1]

img = Image.open('me.jpeg')
img_width = 100
width_percent = (img_width/float(img.size[0]))
img_height = int((float(img.size[1])*float(width_percent)))
img = img.resize((img_width,img_height), Image.Resampling.LANCZOS)
width, height = img.size

art = ''
for y in range(height):
    row = []
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        brightness = (r+g+b)/3
        scaled_brightness = brightness/255
        char_index = math.floor(scaled_brightness * len(chars))
        char = chars[char_index]
        art += char*2
    art += '\n';

print(art)
file = open('out.txt', 'w')
file.write(art)
file.close()