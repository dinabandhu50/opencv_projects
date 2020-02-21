import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('./data/image_3.jpg')

# hist,bins = np.histogram2d(img)
print(img.shape)
plt.imshow(img)
