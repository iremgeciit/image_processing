import cv2
image = cv2.imread("../images/original.jpg")

blue, green, red = cv2.split(image)

cv2.imshow("Blue Channel", blue)
cv2.imshow("Green Channel", green)
cv2.imshow("Red Channel", red)

cv2.imwrite("../outputs/blue_channel.jpg", blue)
cv2.imwrite("../outputs/green_channel.jpg", green)
cv2.imwrite("../outputs/red_channel.jpg", red)