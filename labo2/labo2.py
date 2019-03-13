from Models.models import SVM, KNN
from Validation.validation import run_valiadtion
from ImageProcessing.datasetloading import load_ensemble
from sklearn.model_selection import train_test_split


def run_program():
    image_dataset = load_ensemble("EnsembleB/")
    x_train, x_true, y_train, y_test = train_test_split(
        image_dataset.data, image_dataset.target, test_size=0.3, random_state=109)
    target_names = image_dataset.target_names

    svm = SVM()
    knn = KNN()

    svm.fit(x_train, y_train)
    y_pred1 = svm.predict(x_true)

    knn.fit(x_train, y_train)
    y_pred2 = knn.predict(x_true)

    run_valiadtion(y_pred1, y_test, svm, target_names)
    run_valiadtion(y_pred2, y_test, knn, target_names)


if __name__ == '__main__':
    run_program()
