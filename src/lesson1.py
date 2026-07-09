import cv2
image = cv2.imread("../images/original.jpg")

print(type(image))
print(image.shape)

print(image[0, 0])
print(image[100, 100])



for i in range(300,400):
    for j in range(150,250):
        image[i,j]=[0,0,255]


cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

