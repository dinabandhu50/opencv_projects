import cv2

# Reading image from folder
img = cv2.imread('../data/image_1.jpg')
print(img.shape)

# Writing to local folder
cv2.imwrite('../data/image_1_write.jpg', img)

# Showing on window
cv2.imshow('Figure', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
