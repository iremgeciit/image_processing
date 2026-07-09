import cv2
import matplotlib.pyplot as plt

image = cv2.imread("../images/original9.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

resize = cv2.resize(image,(300,300))

center=(image.shape[1]//2,image.shape[0]//2)

matrix=cv2.getRotationMatrix2D(center,45,1)

rotate=cv2.warpAffine(
    image,
    matrix,
    (image.shape[1],image.shape[0])
)

flip=cv2.flip(image,1)

crop=image[100:500,200:600]

plt.figure(figsize=(15,8))

titles=[
"Original",
"Resize",
"Rotate",
"Flip",
"Crop"
]

images=[
image,
resize,
rotate,
flip,
crop
]

for i in range(len(images)):

    plt.subplot(2,3,i+1)

    plt.imshow(images[i])

    plt.title(titles[i])

    plt.axis("off")

plt.tight_layout()

plt.show()