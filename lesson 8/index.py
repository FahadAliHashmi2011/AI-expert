import cv2
import numpy as np
import matplotlib.pyplot as plt
image =cv2.imread("lesson 8/example.jpg")
image_rgb =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB image")
plt.show()
gray_image= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.title("Grayscale image")
plt.imshow(gray_image,cmap="gray")
plt.show()
cropped_image = image[100:300 ,200:400]
cropped_rgb = cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("cropped region")
plt.show()
(h,w) = image.shape[0:2]
center = (w//2 ,h//2)
m = cv2.getRotationMatrix2D(center,45,1.0)
rotated = cv2.warpAffine(image, m,(w,h))
rotated_rgb = cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("rotatated image")
plt.show()
brightness_matrix =np.ones(image.shape,dtype="uint8")*50
brighter = cv2.add(image,brightness_matrix)
brighter_rgb = cv2.cvtColor(brighter,cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("brighter image")
plt.show()
