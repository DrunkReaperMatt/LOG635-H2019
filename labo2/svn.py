from sklearn.svm import SVC
import numpy as np

class SVM():
	def print_agent():
		print('svm')

	def exec(x, y, C=1, kernel='rbf',):
		clf = SVC(C=C, kernel=kernel)
		clf.fit(x,y)
