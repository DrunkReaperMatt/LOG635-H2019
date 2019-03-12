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
import cv2 as cv
from labo2.ImageProcessing.squares import find_squares


# function that reads an image and returns its grayscale cropped square region
def process_image(image_path):
    # import the image and transform it to grayscale
    gray_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

    # find all squares in image
    print(image_path + '......Loaded!')
    squares = find_squares(gray_image)
    cv.drawContours(gray_image, squares, -1, (0, 255, 0), 3)

    # if no square was found, simply use the original image
    cropped_image = gray_image
    if len(squares) != 0:
        # crop the grayscale image with the contours
        cropped_image = gray_image[squares[0][0][1]:squares[0][2][1], squares[0][1][0]:squares[0][3][0]]

    # resize image to make it smaller
    resized_image = cv.resize(cropped_image, (32, 14))

    return resized_image
