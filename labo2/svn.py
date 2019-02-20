from sklearn.svm import SVC
from crossValidation import CrossValidation as cv

class SVM():
	def print_agent():
		print('svm')

	def exec(x, y, trainX, C=1e-3, gamma=1e-3, kernel='rbf',):
		clf = SVC(C=C, kernel=kernel)
		clf.fit(x,y)
		result = clf.predict(trainX)

		score = cv().AccuracyScore(knn, x, y)
		print(score)

		return result