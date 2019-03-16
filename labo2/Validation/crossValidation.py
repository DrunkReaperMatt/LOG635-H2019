from sklearn.model_selection import cross_val_score


class CrossValidation(object):
	def AccuracyScore(self, clf, X, Y, cv=10):
		score = cross_val_score(clf,X,Y, cv=cv)
		return score.mean()