import cv2
import matplotlib.pyplot as plt

img = cv2.imread('document.jpg', 0)
plt.imshow(img, cmap="gray")
plt.show()