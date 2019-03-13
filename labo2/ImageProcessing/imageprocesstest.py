from labo2.ImageProcessing.imageprocess import process_image
import cv2 as cv

'''
Test code for image processing function
'''


cropped_img = process_image('../Images/Triangles/Triangles_3_F/7-triangle3.png')
cv.imshow('cropped image', cropped_img)
cv.waitKey(0)
