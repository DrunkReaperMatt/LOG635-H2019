import numpy as np
from crossValidation import CrossValidation as cv
import cv2
from sklearn.preprocessing import MinMaxScaler
import glob
import warnings
import sys
import random
from sklearn.metrics import classification_report, confusion_matrix

from labo2.ImageProcessing.datasetloading import load_ensemble


def do_foward_propagation(z, w):
    x0 = []
    x1 = z
    for i in z:
        i = np.insert(i, 0, 1)
        x0.append(i.tolist())

    return np.dot(x0, w)


def do_back_propagation(z, w):
    pass


def calculate_sigmoid(z):
    return 1 / (1 + np.exp(-z))


def calculate_derivative_sigmoid(z):
    return 1 / (1 + np.exp(-z)) * (1 - 1 / (1 + np.exp(-z)))


def remove_biais(w):
    return np.delete(w, 0, 1)


def add_biais(a):
    x0 = []
    for i in a:
        i = np.insert(i, 0, 1)
        x0.append(i.tolist())

    return x0


if __name__ == "__main__":

    image_dataset = load_ensemble("../EnsembleB/")
    dataset_size = image_dataset.target_size

    time_train_arr = []
    time_pred_arr = []
    pred_arr = []
    scalability_arr = [dataset_size,
                       dataset_size * 0.8,
                       dataset_size * 0.6,
                       dataset_size * 0.4,
                       dataset_size * 0.2]

    print(image_dataset)
    print(dataset_size)
