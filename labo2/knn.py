from sklearn.neighbors import KNeighborsClassifier
import numpy as np

class KNN():
	def print_agent():
		print('knn')

	def exec(x, y,n=5, weights = 'uniform'):
		knn = NearestNeighbors(n_neighbors = n, algorithm ='auto', weights=weights)
		knn.fit(x,y)
