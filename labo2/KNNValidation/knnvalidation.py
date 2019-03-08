from ImageProcessing.datasetloading import load_ensemble
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import metrics


dataset = load_ensemble("../EnsembleB/")

X_train, X_true, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=.1, random_state=109)


clf = KNeighborsClassifier(n_neighbors=5, algorithm='auto', weights='distance')
clf.fit(X_train, y_train)


y_pred = clf.predict(X_true)
target_names = dataset.target_names
print("Classification report for - \n{}:\n{}\n".format(
    clf, metrics.classification_report(y_test, y_pred, target_names=target_names)
))


cm = metrics.confusion_matrix(y_test, y_pred)
print(cm)