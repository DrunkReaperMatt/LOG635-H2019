from labo2.ImageProcessing.datasetloading import load_ensemble

from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import time

# Load dataset from Ensemble B directory
image_dataset = load_ensemble("../EnsembleB/")
dataset_size = image_dataset.target_size

time_train_arr = []
time_pred_arr = []
pred_arr = []
scalability_arr = [dataset_size,
                    dataset_size*0.8,
                    dataset_size*0.6,
                    dataset_size*0.4,
                    dataset_size*0.2]

# Run svm validation for each scalable dataset
for size in scalability_arr:
    X = image_dataset.data
    Y = image_dataset.target

    print("\nTest de scalabilité à " + str(size) + " %")
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=int(size), random_state=42)

    svc = svm.SVC(dataset_size, 'linear')

    # Train machine
    init_train_time = time.time()
    svc.fit(X_train, y_train)
    end_train_time = time.time()
    time_train_arr.append(end_train_time - init_train_time)

    # Obtain predictions
    init_pred_time = time.time()
    pred_arr.append(svc.score(X_test, y_test))
    y_pred = svc.predict(X_test)
    end_pred_time = time.time()
    time_pred_arr.append(end_pred_time - init_pred_time)

    print("Matrice de classification - \n{}".format(
        metrics.classification_report(y_test, y_pred)
    ))

    print("Matrice de confusion - \n{}".format(
        metrics.confusion_matrix(y_test, y_pred)
    ))

plt.title("Graphe du temps d'apprentissage")
plt.plot(scalability_arr, time_train_arr)
plt.show()

plt.title("Graphe du temps de prédictions")
plt.plot(scalability_arr, time_pred_arr)
plt.show()
