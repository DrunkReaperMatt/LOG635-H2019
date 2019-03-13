from sklearn import metrics
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import time


def run_valiadtion(dataset, clf, model='NONE'):
    dataset_size = dataset.target_size
    time_train_arr = []
    time_pred_arr = []
    pred_arr = []
    scalability_arr = [1,
        0.8,
        0.6,
        0.4,
        0.2]

    # Run svm validation for each scalable dataset
    for size in scalability_arr:
        X, Y = shuffle(dataset.data, dataset.target, random_state=42)
        print(len(X))
        X_mod = X[:int(len(X)*size)]
        Y_mod = Y[:int(len(Y)*size)]


        print("\nTest de scalabilité à " + str(size * 100) + " %")
        X_train, X_test, y_train, y_test = train_test_split(X_mod, Y_mod)

        #svc = svm.SVC(dataset_size, 'linear')



        # Train machine
        init_train_time = time.time()
        clf.fit(X_train, y_train)
        end_train_time = time.time()
        time_train_arr.append(end_train_time - init_train_time)

        # Obtain predictions
        init_pred_time = time.time()
        pred_arr.append(clf.score(X_test, y_test))
        y_pred = clf.predict(X_test)
        end_pred_time = time.time()
        time_pred_arr.append(end_pred_time - init_pred_time)

        print("Matrice de classification - \n{}".format(
            metrics.classification_report(y_test, y_pred)
        ))

        print("Matrice de confusion - \n{}".format(
            metrics.confusion_matrix(y_test, y_pred)
        ))

    plt.title("Graphe du temps d'apprentissage pour {}".format(model))
    plt.plot(scalability_arr, time_train_arr)
    plt.show()

    plt.title("Graphe du temps de prédictions pour {}".format(model))
    plt.plot(scalability_arr, time_pred_arr)
    plt.show()
