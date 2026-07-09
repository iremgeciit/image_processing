import cv2
import matplotlib.pyplot as plt

# Resmi gri olarak oku
image = cv2.imread("../images/original3.jpg",0)

# Histogram Equalization uygula
equalized = cv2.equalizeHist(image)

# Kaydet
cv2.imwrite("../outputs/equalized.jpg", equalized)

# Yan yana göster
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.imshow(image, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(equalized, cmap="gray")
plt.title("Equalized")
plt.axis("off")

plt.show()

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(image,cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(equalized,cmap="gray")
plt.title("Equalized")
plt.axis("off")

plt.subplot(2,2,3)
plt.hist(image.ravel(),256,[0,256])
plt.title("Original Histogram")

plt.subplot(2,2,4)
plt.hist(equalized.ravel(),256,[0,256])
plt.title("Equalized Histogram")

plt.tight_layout()

plt.show()