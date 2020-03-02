import numpy as np
import cv2

# Reading image
img = cv2.imread('../data/image_3.jpg', 1)

# Drawing on image
cv2.line(img, (100, 200), (500, 300), (0, 0, 255), 5)
cv2.arrowedLine(img, (10, 500), (500, 10), (0, 255, 0), 5)
cv2.rectangle(img, (200, 450), (400, 550), (255, 0, 0), 5)
cv2.circle(img, (350, 350), 50, (100, 10, 1), 5)

# showing image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
