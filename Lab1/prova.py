import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

img_path = "C:/SCAV/video-coding-materials/Lab1/blau.png"
img = cv2.imread(img_path)

plt.figure(figsaize=(12, 5))

plt.imshow(img)
plt.title("Original Image (RGB)")
plt.axis("off")

plt.show()

