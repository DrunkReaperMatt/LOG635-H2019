from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix


class SVM(object):
	def exec(self, x, y, target_names):
		param_grid = [
			{'C': [1, 0.1, 0.01, 0.001], 'kernel': ['linear']},
			{'C': [1, 0.1, 0.01, 0.001], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']}
		]
		svc = SVC()
		clf = GridSearchCV(svc, param_grid, cv=5)
		clf.fit(x, y)

		y_pred = clf.predict(x)
		print("Classification report for - \n{}:\n{}\n".format(
			clf, classification_report(y, y_pred, target_names=target_names)
		))

		cm = confusion_matrix(y, y_pred)
		print(cm)
