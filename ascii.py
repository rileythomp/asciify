from PIL import Image
import math
import time

chars = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'.'
chars = chars[::-1]

img = Image.open('me.jpeg')
img_width = 100
width_percent = (img_width/float(img.size[0]))
img_height = int((float(img.size[1])*float(width_percent)))
img = img.resize((img_width,img_height), Image.ANTIALIAS)
width, height = img.size

brightness_img = []
art = ''
start_time = time.time()
for y in range(height):
    row = []
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        row.append((r+g+b)/3)
    brightness_img.append(row)

art = ''
for y in range(len(brightness_img)):
    for x in range(len(brightness_img[0])):
        brightness = brightness_img[y][x]
        scaled_brightness = brightness/255
        char_index = math.floor(scaled_brightness * len(chars))
        char = chars[char_index]
        art += char*2
    art += '\n';

print("--- %s seconds ---" % (time.time() - start_time))
print(art)
file = open('out.txt', 'w')
file.write(art)
file.close()