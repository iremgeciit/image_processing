import cv2
import matplotlib.pyplot as plt

# Resmi oku
image = cv2.imread("../images/original6.jpg")

# Gri tona çevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sobel
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Laplacian
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

# Canny
canny = cv2.Canny(gray, 100, 200)

plt.figure(figsize=(15,8))

# Original
plt.subplot(2,3,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

# Gray
plt.subplot(2,3,2)
plt.imshow(gray, cmap="gray")
plt.title("Gray")
plt.axis("off")

# Sobel X
plt.subplot(2,3,3)
plt.imshow(sobel_x, cmap="gray")
plt.title("Sobel X")
plt.axis("off")

# Sobel Y
plt.subplot(2,3,4)
plt.imshow(sobel_y, cmap="gray")
plt.title("Sobel Y")
plt.axis("off")

# Laplacian
plt.subplot(2,3,5)
plt.imshow(laplacian, cmap="gray")
plt.title("Laplacian")
plt.axis("off")

# Canny
plt.subplot(2,3,6)
plt.imshow(canny, cmap="gray")
plt.title("Canny")
plt.axis("off")

plt.tight_layout()
plt.show()