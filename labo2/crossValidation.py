from sklearn.model_selection import cross_val_score


class CrossValidation(object):
    def AccuracyScore(self, clf, X, Y, cv=5):
        score = cross_val_score(clf,X,Y, cv=cv)
        return score.mean()
