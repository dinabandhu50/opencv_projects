import cv2
import numpy as np
import matplotlib.pyplot as plt

# %%
img = cv2.imread('./data/image_3.jpg', 0)
print(img.shape)
# %%


def bgr2rgb(img):
    """
    The cv2 reads image in BGR format while plt showes image in RGB format.
    To overcome this follow:
    b,g,r = cv2.split(img)
    img = cv2.merge([r,g,b])
    """
    if len(img.shape) == 3 and img.shape[2] == 3:
        b, g, r = cv2.split(img)
        out = cv2.merge([r, g, b])
    else:
        out = img
    return out


# %% Histogram eqalization
hist, bins = np.histogram(img.flatten(), 256, (0, 256))
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/hist.cumsum().max()
# Histogram Equalization
equ = cv2.equalizeHist(img)
hist_equ, bins_equ = np.histogram(equ.flatten(), 256, (0, 256))
# Contrast Limited Adaptive Histogram Equalization
clahe = cv2.createCLAHE(clipLimit=20.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)
hist_cl1, bins_cl1 = np.histogram(cl1.flatten(), 256, (0, 256))
# Horizontal stack of images
res = np.hstack((img, equ, cl1))

plt.figure(1)
plt.imshow(bgr2rgb(res), cmap='gray')
# %%
plt.figure(2)
plt.plot(hist, color='b', label="hist")
plt.plot(hist_equ, color='g', label="hist equalized")
plt.plot(hist_cl1, color='r', label="hist CLAHE")
plt.plot(cdf_normalized, 'y', label='CDF normalized')
plt.legend()
plt.show()
