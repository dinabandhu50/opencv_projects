import cv2
import matplotlib.pyplot as plt

# read image
img = cv2.imread('../data/image_5.jpg', 1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(
    img,
    'OpenCV - Dinabandhu',
    (50, 600),
    font,
    2,
    (255, 255, 255),
    5
)

# # display image using cv2
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# display image using plt
plt.figure()
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
