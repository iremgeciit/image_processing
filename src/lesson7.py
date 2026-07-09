import cv2
import matplotlib.pyplot as plt

image = cv2.imread("../images/original.jpg", 0)

plt.figure(figsize=(8,5))

plt.hist(image.ravel(),
         bins=256,
         range=[0,256],
         color="black")

plt.title("Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")

plt.grid()

plt.show()