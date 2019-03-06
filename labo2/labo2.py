from knn import KNN
from svn import SVM
from imgprocess.imageprocess import process_image
from sklearn.preprocessing import LabelEncoder
import numpy as np
import cv2
import os


def run_program():
    setup_datasets()
    return


def setup_datasets():
    lbl = LabelEncoder()

    imgdir = 'Images/Losanges/Losanges_4_F'
    cercles = []
    for file in os.listdir(imgdir):
        print(os.path.join(imgdir, file))
        img = process_image(os.path.join(imgdir, file))
        img = np.array(img)
        cercles.append(img)


    cercles = np.array(cercles)
    print(cercles.size)
    return


def shrink_array(array, percentage):
    size = array.size * percentage
    temparr = np.array(array)
    np.random.shuffle(temparr)
    resize = temparr[:size]

    return resize


def test_prints():
    KNN.print_agent()
    SVM.print_agent()


if __name__ == '__main__':
    run_program()
