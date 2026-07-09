import cv2
import matplotlib.pyplot as plt

# Resmi oku
image = cv2.imread("../images/original.jpg")

# Blur uygula
blur = cv2.blur(image, (7,7))

# Kaydet
cv2.imwrite("../outputs/mean_blur.jpg", blur)

# Göster
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB))
plt.title("Mean Filter")
plt.axis("off")

plt.show()