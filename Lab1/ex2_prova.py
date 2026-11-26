import cv2
import numpy as np
import matplotlib.pyplot as plt
from first_seminar import ColorTranslator

# To prove visually if the conversion is done correctly.

# Read the original image
img_path = "C:/SCAV/video-coding-materials/Lab1/images/blau.png"       # The original image is a 5x5 blue (0, 0, 255) image
img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# When plotting the image we have realize that the image is not blue, but red. So checking on internet 
# (https://www.geeksforgeeks.org/python/reading-image-opencv-using-python/) we have found that opencv reads the images in BGR, 
# different from matplot that reads it in RGB. So we have apply this conversion.

height, width, channels = img.shape

img_yuv = np.zeros((height, width, channels), dtype=np.uint8)

# Iterate for every pixel and convert from RGB to YUV
for i in range(height):
    for j in range(width):

        r, g, b = img[i, j]

        y, u, v = ColorTranslator().rgb_to_yuv_limited(r, g, b)

        img_yuv[i, j] = (y, u, v)


plt.imshow(img)
plt.title("Original Image (RGB)")
plt.show()

plt.imshow(img_yuv)
plt.title("Converted Image (YUV)")
plt.show()


# We dont know if the image is correct, so we convert it back to RGB and check if it is the same as the original image
img_rgb = np.zeros((height, width, channels), dtype=np.uint8)

# Iterate for every pixel and convert from YUV to RGB
for i in range(height):
    for j in range(width):

        y, u, v = img_yuv[i, j]

        r, g, b = ColorTranslator().yuv_to_rgb_limited(int(y), int(u), int(v))

        img_rgb[i, j] = (r, g, b)


plt.imshow(img_rgb)
plt.title("Reconverted Image (RGB)")
plt.show()


# I do not know why the YUV image is not blue :(

