import cv2
import matplotlib.pyplot as plt

# Resmi oku
image = cv2.imread("../images/original10.jpg")

# RGB'ye çevir
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Gri tona çevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Histogram Equalization
equalized = cv2.equalizeHist(gray)

# Grafik
plt.figure(figsize=(12,8))

# ----------------- Original -----------------
plt.subplot(2,2,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

# ----------------- Equalized -----------------
plt.subplot(2,2,2)
plt.imshow(equalized, cmap="gray")
plt.title("Histogram Equalization")
plt.axis("off")

# ----------------- Histogram -----------------
plt.subplot(2,2,3)
plt.hist(gray.ravel(), bins=256, range=(0,256), color="black")
plt.title("Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Pixel Count")

# ----------------- Equalized Histogram -----------------
plt.subplot(2,2,4)
plt.hist(equalized.ravel(), bins=256, range=(0,256), color="black")
plt.title("Equalized Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Pixel Count")

plt.tight_layout()
plt.savefig("../outputs/original10.jpg", dpi=300, bbox_inches="tight")
plt.show()