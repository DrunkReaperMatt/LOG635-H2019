from sklearn.neighbors import KNeighborsClassifier
from labo2.Validation.crossValidation import CrossValidation as cv

class KNN(object):
	def print_agent(self):
		print('knn')

	def exec(self, x, y, trainX, n=5, weights = 'uniform'):
		knn = KNeighborsClassifier(n_neighbors = n, algorithm ='auto', weights=weights)
		knn.fit(x,y)
		result = knn.predict(trainX)

		score = cv().AccuracyScore(knn, x, y)
		print(score)

		return result
