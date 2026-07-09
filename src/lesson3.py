import cv2

image = cv2.imread("../images/original.jpg")

blue, green, red = cv2.split(image)

blue[:] = 0

new_image = cv2.merge((blue, green, red))

cv2.imshow("Original", image)
cv2.imshow("Without Blue", new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()