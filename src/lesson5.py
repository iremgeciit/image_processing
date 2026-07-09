import cv2

# Resmi oku
image = cv2.imread("../images/original2.jpg")

# Gri tona dönüştür
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Boyutları yazdır
print("Renkli Görüntü:", image.shape)
print("Gri Görüntü:", gray.shape)

# Ekranda göster
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)

# Kaydet
cv2.imwrite("../outputs/grayscale.jpg", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()