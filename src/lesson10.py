import cv2
import matplotlib.pyplot as plt

image = cv2.imread("../images/original.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)

plt.figure(figsize=(12,4))

plt.subplot(1,4,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(1,4,2)
plt.imshow(h, cmap="hsv")
plt.title("Hue")
plt.axis("off")

plt.subplot(1,4,3)
plt.imshow(s, cmap="gray")
plt.title("Saturation")
plt.axis("off")

plt.subplot(1,4,4)
plt.imshow(v, cmap="gray")
plt.title("Value")
plt.axis("off")

plt.tight_layout()
plt.show()