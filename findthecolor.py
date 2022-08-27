import cv2 as cv
import numpy as np
from PIL import Image

image = cv.imread("./saladadefruta.png")
average_color_row = np.average(image, axis=0)
average_color = np.average(average_color_row, axis=0)

average_color = np.ndarray.tolist(average_color)
average_color = tuple(average_color)


for i in average_color:
    average_color = tuple(tuple(map(int, average_color)))

im = Image.open('./saladadefruta.png')
width = im.size[0] 
height = im.size[1] 
for i in range(0,width):
    for j in range(0,height):
        data = im.getpixel((i,j))
        if (data[0]==0 and data[1]==0 and data[2]==0):
            im.putpixel((i,j),(average_color))

im.save("new_image_3.png")