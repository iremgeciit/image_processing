import cv2
import matplotlib.pyplot as plt

# Resmi oku
image = cv2.imread("../images/original8.jpg")

# Matplotlib için RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold
_, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

# Konturları Bul
contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Çizmek için kopya al
result = image_rgb.copy()

# Konturları çiz
cv2.drawContours(
    result,
    contours,
    -1,
    (255,0,0),
    2
)

print("Bulunan Kontur Sayısı:", len(contours))

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(image_rgb)
plt.title("Original")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(gray,cmap="gray")
plt.title("Gray")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(thresh,cmap="gray")
plt.title("Threshold")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(result)
plt.title("Contours")
plt.axis("off")

plt.tight_layout()
plt.show()