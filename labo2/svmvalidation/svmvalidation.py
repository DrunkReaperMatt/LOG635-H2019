from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from labo2.imgprocess.imageprocess import process_image
from sklearn import svm, metrics, datasets
from sklearn.utils import Bunch
from sklearn.model_selection import GridSearchCV, train_test_split

def load_ensemble(ensemble_path) :
    image_dir = Path(ensemble_path)
    folders = [directory for directory in image_dir.iterdir() if directory.is_dir()]
    categories = [folder.name for folder in folders]

    images = []
    flat_data = []
    target = []

    for i, direc in enumerate(folders):
        for file in direc.iterdir():
            img = process_image(str(file))
            flat_data.append(img.flatten())
            images.append(img)
            target.append(i)
    flat_data = np.array(flat_data)
    target = np.array(target)
    images = np.array(images)

    return Bunch(data=flat_data,
                 target=target,
                 target_names=categories,
                 images=images)



image_dataset = load_ensemble("../EnsembleB/")

X_train, X_test, y_train, y_test = train_test_split(
    image_dataset.data, image_dataset.target, test_size=0.3,random_state=109)

param_grid = [
  {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
  {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
 ]
svc = svm.SVC()
clf = GridSearchCV(svc, param_grid)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("Classification report for - \n{}:\n{}\n".format(
    clf, metrics.classification_report(y_test, y_pred)))