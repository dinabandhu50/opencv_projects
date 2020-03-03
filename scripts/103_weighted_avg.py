import cv2
import matplotlib.pyplot as plt


img1 = cv2.imread('../data/image_1.jpg')
img2 = cv2.imread('../data/image_2.jpg')
# need to do resize

res = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

plt.figure()
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.show()
