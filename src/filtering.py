import cv2
import matplotlib.pyplot as plt

# ============================
# Resmi Oku
# ============================

image = cv2.imread("../images/original4.jpg")

# OpenCV BGR okur.
# Matplotlib ise RGB ister.
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# ============================
# Filtreler
# ============================

mean = cv2.blur(image, (7, 7))

gaussian = cv2.GaussianBlur(image, (7, 7), 0)

median = cv2.medianBlur(image, 7)

bilateral = cv2.bilateralFilter(image, 9, 75, 75)

# Matplotlib için RGB'ye çevir

mean = cv2.cvtColor(mean, cv2.COLOR_BGR2RGB)
gaussian = cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB)
median = cv2.cvtColor(median, cv2.COLOR_BGR2RGB)
bilateral = cv2.cvtColor(bilateral, cv2.COLOR_BGR2RGB)

# ============================
# Sonuçları Kaydet
# ============================

cv2.imwrite("../outputs/mean.jpg",
            cv2.blur(image, (7, 7)))

cv2.imwrite("../outputs/gaussian.jpg",
            cv2.GaussianBlur(image, (7, 7), 0))

cv2.imwrite("../outputs/median.jpg",
            cv2.medianBlur(image, 7))

cv2.imwrite("../outputs/bilateral.jpg",
            cv2.bilateralFilter(image, 9, 75, 75))

# ============================
# Karşılaştırma
# ============================

plt.figure(figsize=(14,8))

plt.subplot(2,3,1)
plt.imshow(image_rgb)
plt.title("Original")
plt.axis("off")

plt.subplot(2,3,2)
plt.imshow(mean)
plt.title("Mean Filter")
plt.axis("off")

plt.subplot(2,3,3)
plt.imshow(gaussian)
plt.title("Gaussian Filter")
plt.axis("off")

plt.subplot(2,3,4)
plt.imshow(median)
plt.title("Median Filter")
plt.axis("off")

plt.subplot(2,3,5)
plt.imshow(bilateral)
plt.title("Bilateral Filter")
plt.axis("off")

plt.tight_layout()
plt.savefig("../outputs/original4.jpg", dpi=300, bbox_inches="tight")
plt.show()