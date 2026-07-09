import cv2
import matplotlib.pyplot as plt

# Resmi gri olarak oku
image = cv2.imread("../images/original3.jpg", 0)

# Histogramı çiz
plt.hist(image.ravel(), bins=256, range=[0,256])

# Başlık
plt.title("Image Histogram")

# X ekseni
plt.xlabel("Pixel Intensity")

# Y ekseni
plt.ylabel("Number of Pixels")

# Grafiği göster
plt.show()