from Models.models import SVM, KNN
from Validation.validation import run_valiadtion
from ImageProcessing.datasetloading import load_ensemble


def run_program():
    image_dataset = load_ensemble("EnsembleB/")

    svm = SVM()
    knn = KNN()

    run_valiadtion(image_dataset, svm, "SVM")
    run_valiadtion(image_dataset, knn, "K-NN")


if __name__ == '__main__':
    run_program()
