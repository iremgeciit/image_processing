import cv2
import matplotlib.pyplot as plt

# Resmi oku
image = cv2.imread("../images/original.jpg")

# Gaussian Blur
gaussian = cv2.GaussianBlur(image, (7,7), 0)

# Kaydet
cv2.imwrite("../outputs/gaussian.jpg", gaussian)

# Karşılaştır
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB))
plt.title("Gaussian Filter")
plt.axis("off")


plt.tight_layout()
plt.show()