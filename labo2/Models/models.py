from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV


def SVM():
    param_grid = [
        {'C': [1, 0.1, 0.01, 0.001], 'kernel': ['linear']},
        {'C': [1, 0.1, 0.01, 0.001], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']}
    ]
    svc = SVC()
    clf = GridSearchCV(svc, param_grid, cv=5)
    return clf


def KNN():
    clf = KNeighborsClassifier(n_neighbors=5, algorithm='auto', weights='distance')
    return clf
