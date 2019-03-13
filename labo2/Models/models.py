from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier


def SVM():
    clf = SVC(kernel='linear')
    return clf


def KNN():
    clf = KNeighborsClassifier(n_neighbors=5, algorithm='auto', weights='distance')
    return clf
