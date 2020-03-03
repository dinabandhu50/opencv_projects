import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading Image
img = cv2.imread('../data/image_2.jpg', 1)

print(img.shape)

# image displaying
plt.figure()
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

# small image
crop = img[250:550, 500:700]

plt.figure()
plt.imshow(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
plt.show()

# Splitting and Merging image channels
b, g, r = cv2.split(img)
img2 = cv2.merge((r, g, b))
