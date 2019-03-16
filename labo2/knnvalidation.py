from labo2.Models.models import KNN
from labo2.Validation.validation import run_validation
from labo2.ImageProcessing.datasetloading import load_ensemble


def run_program():
    image_dataset = load_ensemble("EnsembleB/")

    knn = KNN()

    run_validation(image_dataset, knn, "K-NN")


if __name__ == '__main__':
    run_program()
