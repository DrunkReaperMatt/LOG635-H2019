#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#@Author: Ameni MEZNI, ameni.mezni.1@etsmtl.net
#Date: 22/08/2018
#In this tutorial, we will explore features extraction for images using pixel values

# pip install -U scikit-learn scipy matplotlib
# pip install opencv-python

# In[16]:


#import necessery packages
import cv2
import squares as square
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#from cv2 import imread, imwrite, imshow, waitKey
from sklearn.preprocessing import MinMaxScaler


# In[18]:


#An image has several colors and many pixels.
#To visualize how this image is stored, think of every pixel as a cell in matrix.
#Now this cell contains three different intensity information, catering to the color Red, Green and Blue.
#So a RGB image becomes a 3-D matrix. Each number is the intensity of Red, Blue and Green colors.

#Handling the third dimension of images sometimes can be complex and redundant.
#In feature extraction, it becomes much simpler if we compress the image to a 2-D matrix.
#This is done by Gray-scaling or Binarizing.
#Gray scaling is richer than Binarizing as it shows the image as a combination of different intensities of Gray.
#Whereas binarzing simply builds a matrix full of 0s and 1s.
#Here is how you convert a RGB image to Gray scale:


#import the image and transform it to grayscale
greyscale_image= cv2.imread('../Images/Losanges/Losanges_4_F/8-losange4.jpg',cv2.IMREAD_GRAYSCALE)

#Show the grey_scaled image
# cv2.imshow('Initial image',greyscale_image)

#Save the grey_scaled image
# cv2.imwrite('../Images/Losanges/Losanges_4_F/8-losange4.jpg', greyscale_image)

#Creates a trackbar and attaches it to the specified window.
#cv2.waitKey()

print("Grey scaled image shape", greyscale_image.shape)
print("greyscale_image",greyscale_image)
print("type(greyscale_image)",type(greyscale_image))


# In[19]:


sc = MinMaxScaler(feature_range = (0, 1))
greyscale_image_normalized = sc.fit_transform(greyscale_image)
print("greyscale_image_normalized",greyscale_image_normalized)
print("greyscale_image_normalized.shape", greyscale_image_normalized.shape)

squares = square.find_squares(greyscale_image)
cv2.drawContours( greyscale_image, squares, -1, (0, 255, 0), 3)
cv2.imshow('squares', greyscale_image)
# img[y1:y2, x1:x2]
cropped_img = greyscale_image[squares[0][0][1]:squares[0][2][1], squares[0][1][0]:squares[0][3][0]]
cv2.imshow('cropped squares', cropped_img)

# plt.imshow(img)
# plt.show()

cv2.waitKey(0)