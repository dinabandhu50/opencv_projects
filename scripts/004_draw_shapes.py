import numpy as np
import matplotlib.pyplot as plt
import cv2

# Reading image
img = cv2.imread('../data/image_3.jpg', 1)

print(img.shape)
# Drawing on image
cv2.line(img, (100, 200), (500, 300), (0, 0, 255), 5)
cv2.arrowedLine(img, (10, 500), (500, 10), (0, 255, 0), 5)
cv2.rectangle(img, (200, 450), (400, 550), (255, 0, 0), 5)
cv2.circle(img, (350, 350), 50, (100, 10, 1), 5)
cv2.ellipse(img, (150, 350), (100, 50), 0, 0, 360, 255, -1)

pts = np.array([[10, 15], [150, 200], [500, 111]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255))
# showing image
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.figure()
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
