import cv2
img = cv2.imread("lesson 11/example_edge.jpg")
if img is None:
    print("image is not found!")
else:
    while True:
        print("\nChoose a filter: ")
        print("1 - red tint")
        print("2 - blue tint")
        print("3 - green tint")
        print("4 - increase red")
        print("5 - decrease blue")
        print("0 - exit")
        
        choice = input("enter your choice :") #string datatype
        new_img = img.copy() #make copy
        if choice == "1":
            new_img[:,:,0]=0 #remove blue
            new_img[:,:,1]=0 #remove green



        elif choice == "2":
            new_img[:,:,1]=0 #remove green
            new_img[:,:,2]=0 #remove red

        
        elif choice == "3":
            new_img[:,:,0]=0 #remove blue
            new_img[:,:,2]=0 #remove red
        
        elif choice == "4":
            new_img[:,:,2]= cv2.add(new_img[:,:,2],50)
        
        elif choice == "5":
            new_img[:,:,0]= cv2.subtract(new_img[:,:,0],50)
        
        elif choice == "0":
            print("excitiing...")
            break
           

        else:
            print(" iinvalid choice! try again")
            continue
        cv2.imshow("fiiltered image",new_img)
        cv2.waitKey(0)
    cv2.destroyAllWindows()




            