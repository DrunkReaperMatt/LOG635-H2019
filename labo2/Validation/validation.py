from sklearn import metrics


def run_valiadtion(y_pred, y_test, clf, target_names):
    print("Classification report for - \n{}:\n{}\n".format(
        clf, metrics.classification_report(y_test, y_pred, target_names=target_names)
    ))

    cm = metrics.confusion_matrix(y_test, y_pred)
    print(cm)
