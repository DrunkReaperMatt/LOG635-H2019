from labo2.svmvalidation.svmvalidation import load_ensemble

image_dataset = load_ensemble("../EnsembleB/")

X_train, X_test, y_train, y_test = train_test_split(
    image_dataset.data, image_dataset.target, test_size=0.3,random_state=109)