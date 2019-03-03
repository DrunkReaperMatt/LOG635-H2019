#!/usr/bin/env python
# coding: utf-8

'''
Program allowing the conversion of an image to Grey color and crop out the desired region.

Inspired from:
Programme Python basique pour extraction de primitives
Ameni MEZNI, ameni.mezni.1@etsmtl.net
Date: 22/08/2018

Necessary command(s):
pip install opencv-python
'''


# import necessary packages
import cv2
import squares as square


# function that reads an image and returns its grayscale cropped square region
def process_image(image_path):
    # import the image and transform it to grayscale
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # find all contours of the square region
    contours = square.find_squares(gray_image)
    cv2.drawContours(gray_image, contours, -1, (0, 255, 0), 3)
    # crop the grayscale image with the contours
    cropped_image = gray_image[contours[0][0][1]:contours[0][2][1], contours[0][1][0]:contours[0][3][0]]

    return cropped_image
