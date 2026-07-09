import cv2
import numpy as np
import matplotlib.pyplot as plt

# Resmi oku
image = cv2.imread("../images/original7.jpg")

# Gri tona çevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold
_, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

# Kernel
kernel = np.ones((5,5), np.uint8)

# Morphology işlemleri
erosion = cv2.erode(thresh, kernel, iterations=1)
dilation = cv2.dilate(thresh, kernel, iterations=1)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

plt.figure(figsize=(15,8))

# Original
plt.subplot(2,3,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

# Threshold
plt.subplot(2,3,2)
plt.imshow(thresh, cmap="gray")
plt.title("Threshold")
plt.axis("off")

# Erosion
plt.subplot(2,3,3)
plt.imshow(erosion, cmap="gray")
plt.title("Erosion")
plt.axis("off")

# Dilation
plt.subplot(2,3,4)
plt.imshow(dilation, cmap="gray")
plt.title("Dilation")
plt.axis("off")

# Opening
plt.subplot(2,3,5)
plt.imshow(opening, cmap="gray")
plt.title("Opening")
plt.axis("off")

# Closing
plt.subplot(2,3,6)
plt.imshow(closing, cmap="gray")
plt.title("Closing")
plt.axis("off")

plt.tight_layout()
plt.show()