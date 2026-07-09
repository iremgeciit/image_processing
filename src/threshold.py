import cv2
import matplotlib.pyplot as plt

# ==========================
# Resmi Oku
# ==========================

image = cv2.imread("../images/original5.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ==========================
# Threshold İşlemleri
# ==========================

# Binary
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Binary Inverse
_, binary_inv = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Adaptive Mean
adaptive = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    15,
    5
)

# Otsu
otsu_value, otsu = cv2.threshold(
    gray,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

print("Otsu Threshold Değeri:", otsu_value)

# ==========================
# Sonuçları Kaydet
# ==========================

cv2.imwrite("../outputs/binary.jpg", binary)
cv2.imwrite("../outputs/binary_inverse.jpg", binary_inv)
cv2.imwrite("../outputs/adaptive.jpg", adaptive)
cv2.imwrite("../outputs/otsu.jpg", otsu)

# ==========================
# Karşılaştırma
# ==========================

plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
plt.imshow(gray, cmap="gray")
plt.title("Original (Gray)")
plt.axis("off")

plt.subplot(2,3,2)
plt.imshow(binary, cmap="gray")
plt.title("Binary")
plt.axis("off")

plt.subplot(2,3,3)
plt.imshow(binary_inv, cmap="gray")
plt.title("Binary Inverse")
plt.axis("off")

plt.subplot(2,3,5)
plt.imshow(adaptive, cmap="gray")
plt.title("Adaptive Mean")
plt.axis("off")

plt.subplot(2,3,6)
plt.imshow(otsu, cmap="gray")
plt.title("Otsu")
plt.axis("off")

plt.tight_layout()
plt.show()