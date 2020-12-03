import cv2

img = cv2.imread("lena.jpg",-1) #flag: 1-color image;0-gray image;-1-image as such including alpha channel
# print(img) #pixels of the image

cv2.imshow('image',img) #flash the image
k = cv2.waitKey(0)&0xFF #cv2.waitKey(0) to wait for a key event
                        # 5000: 5 seconds, 0:forever stays
                        # 0xFF: if using 64 system machine

if k == 27: #escape key
    cv2.destroyAllWindows() #close the windows
elif k == ord('s'): #if s is pressed
    cv2.imwrite('lena_copy.png',img)