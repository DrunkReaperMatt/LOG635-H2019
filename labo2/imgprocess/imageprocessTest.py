from labo2.imgprocess.imageprocess import process_image
import cv2

# Test code for image processing function
cropped_img = process_image('../Images/Cercles/Cercles_3_F/30-cercle3.jpg')
cv2.imshow('cropped image', cropped_img)
cv2.waitKey(0)