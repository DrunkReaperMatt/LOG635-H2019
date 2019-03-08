from ImageProcessing.datasetloading import load_ensemble

from sklearn import svm, metrics
from sklearn.model_selection import GridSearchCV, train_test_split


image_dataset = load_ensemble("../EnsembleB/")

X_train, X_true, y_train, y_test = train_test_split(
    image_dataset.data, image_dataset.target, test_size=0.3, random_state=109)

param_grid = [
  {'C': [1, 0.1, 0.01, 0.001], 'kernel': ['linear']},
  {'C': [1, 0.1, 0.01, 0.001], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
 ]
svc = svm.SVC()
clf = GridSearchCV(svc, param_grid)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_true)
target_names = image_dataset.target_names
print("Classification report for - \n{}:\n{}\n".format(
    clf, metrics.classification_report(y_test, y_pred, target_names=target_names)
))

cm = metrics.confusion_matrix(y_test, y_pred)
print(cm)
