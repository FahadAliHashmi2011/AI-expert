import cv2
import matplotlib.pyplot as plt
def show_image(title, img):
    plt.imshow(img,cmap="gray")
    plt.title(title)
    plt.axis("off")
    plt.show
image  = cv2.imread("lesson 10/example_edge.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
show_image("original image",gray)
print("choose an option :")
print("1 - sobel edge")
print("2 - canny edge")
print("3 - blur image")
print("4 - exit")
while True:
    choice = input(" Enter a number:")
    if choice == "1":
        edges = cv2.Sobel(gray,cv2.CV_64F,1,1,ksize=3)
        show_image("sobel edge",edges)
    elif choice == "2":
        edges= cv2.Canny(gray,100,200)
        show_image("canny edges",edges)
    elif choice == "3":
        blur =cv2.GaussianBlur(gray,(5,5),0)
        show_image("blur image",blur)
    elif choice == "4":
        print("bye!")
        break
    else:
        print(" wrong choice try again")
