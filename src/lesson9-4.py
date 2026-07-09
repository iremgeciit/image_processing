import cv2
import matplotlib.pyplot as plt

# Resmi oku
image = cv2.imread("../images/original.jpg")

# Bilateral Filter uygula
bilateral = cv2.bilateralFilter(image, 9, 75, 75)

# Kaydet
cv2.imwrite("../outputs/bilateral.jpg", bilateral)

# Karşılaştır
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(bilateral, cv2.COLOR_BGR2RGB))
plt.title("Bilateral Filter")
plt.axis("off")

plt.tight_layout()
plt.show()