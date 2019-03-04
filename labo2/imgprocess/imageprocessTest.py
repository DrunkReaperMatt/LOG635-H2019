from labo2.imgprocess.imageprocess import process_image
import cv2

# Test code for image processing function
cropped_img = process_image('../Images/Losanges/Losanges_4_F/8-losange4.jpg')
cv2.imshow('cropped image', cropped_img)
cv2.waitKey(0)