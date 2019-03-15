import numpy as np
import cv2 
from sklearn.preprocessing import MinMaxScaler
import glob 
import warnings
import sys
import random
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_fscore_support

warnings.simplefilter('ignore')
np.set_printoptions(threshold=sys.maxsize)

# For a reason we dont know , it is impossible to import the module ImageProcessing.datasetloading


def forward(a,w):
    x0=[]
    for i in a:
        i=np.insert(i,0,1)
        x0.append(i.tolist())
    
    return np.dot(x0,w)
    
def sigmoid(z):
    return 1/(1+np.exp(-z))

def inverseSigmoid(a):
    return 1/(1+np.exp(-z)) * (1-1/(1+np.exp(-z)))

def removeBiais(w):
    return np.delete(w,0,1)

def addBiais(a):
    x0=[]
    for i in a:
        i=np.insert(i,0,1)
        x0.append(i.tolist())
        
    return x0


def randomizeW(x,y):
    return np.random.uniform(low=0, high=1, size=(x,y))
    
def indexHighest(row):
    index = 0;
    for i in range(len(row)):
        if(row[i] > row[index]):
            index = i
        
    return index

def convertDataToNumber(array):
    
    temp = []
    for x in range(0,len(array)):
        index = 0;
        for i in range(len(array[x])):
            if(array[x][i] > array[x][index]):
                index = i

        if(index == 0):
            temp.append('1')
        elif(index == 1):
            temp.append('2')
        elif(index == 2):
            temp.append('3')
        elif(index == 3):
            temp.append('4')
        elif(index == 4):
            temp.append('5')
        elif(index == 5):
            temp.append('6')
        elif(index == 6):
            temp.append('7')
        elif(index == 7):
            temp.append('8')
            
    return temp


#valeur des résultats Y selon la classe
X = []
Y = []

imfilename = ['./EnsembleB/Cercles_2_F/*',
             './EnsembleB/Cercles_5_F/*',
             './EnsembleB/Hexagones_2_F/*',
             './EnsembleB/Hexagones_5_F/*',
             './EnsembleB/Losanges_2_F/*',
             './EnsembleB/Losanges_5_F/*',
             './EnsembleB/Triangles_2_F/*',
             './EnsembleB/Triangles_5_F/*']

yValue = [[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],
          [0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1]]


sc = MinMaxScaler(feature_range = (0, 1))

for i in range(0, len(imfilename)):
    for filename in glob.glob(imfilename[i]): 
        img = cv2.imread(filename,0)
        img = cv2.resize(img,(14,32))
        img = sc.fit_transform(img)
        X.append(np.ravel(img).tolist())
        Y.append(yValue[i])

#275x448
height, width = np.shape(X)

c = list(zip(X, Y))

#randomize X and Y equally to shuffle the dataset but keeping X-Y indexes this is done to avoid having all the data sorted by type
random.shuffle(c)

X, Y = zip(*c)


kfolds = []
yfolds = []

#number of folds //hyperparameter
k=5


#insert all dataset into K folds array which has a size of 5 hyperparam
for i in range(0,5):
    kfolds.append(X[int(height/k*i):int(height/k*(i+1))])
    yfolds.append(Y[int(height/k*i):int(height/k*(i+1))])


#first param = line, second = row, # all weight are initially randomize between 0 and 1

alpha = 0.20
lamda = [0.2,0.4,0.6,0.8,1]
epochs = 100

#this is done to calculate the mean accuracy of the 5 accuracies obtains with the 5 folds


for g in range(0,len(lamda)):
    W1 = randomizeW(25,width+1)
    W2 = randomizeW(8,26)
    
    meanAccuracy = 0
    meanRecall = 0
    meanFMesure = 0
    for z in range(0,k):
        X_training = []
        Y_training = []

        # the last dataset is for testing
        X_test  = []
        Y_test = []

        # this if separates the 5 folds differenty into test and training sets
        if z == 0:
            X_training = np.concatenate((kfolds[1], kfolds[2], kfolds[3],kfolds[4]), axis=0)
            Y_training = np.concatenate((yfolds[1], yfolds[2], yfolds[3],yfolds[4]), axis=0)

            X_test = kfolds[0]
            Y_test = yfolds[0]
        elif z == 1:
            X_training = np.concatenate((kfolds[0], kfolds[2], kfolds[3],kfolds[4]), axis=0)
            Y_training = np.concatenate((yfolds[0], yfolds[2], yfolds[3],yfolds[4]), axis=0)

            X_test = kfolds[1]
            Y_test = yfolds[1]

        elif z == 2:
            X_training = np.concatenate((kfolds[0], kfolds[1], kfolds[3],kfolds[4]), axis=0)
            Y_training = np.concatenate((yfolds[0], yfolds[1], yfolds[3],yfolds[4]), axis=0)

            X_test = kfolds[2]
            Y_test = yfolds[2]

        elif z == 3:
            X_training = np.concatenate((kfolds[0], kfolds[1], kfolds[2],kfolds[4]), axis=0)
            Y_training = np.concatenate((yfolds[0], yfolds[1], yfolds[2],yfolds[4]), axis=0)

            X_test = kfolds[3]
            Y_test = yfolds[3]

        elif z == 4:
            X_training = np.concatenate((kfolds[0], kfolds[1], kfolds[2],kfolds[3]), axis=0)
            Y_training = np.concatenate((yfolds[0], yfolds[1], yfolds[2],yfolds[3]), axis=0)

            X_test = kfolds[4]
            Y_test = yfolds[4]


        height, width = np.shape(X_training)
        m=height
        #loop 100 times to update W1 and W2, 100 is a hyperparameter
        for i in range (0,epochs):

            z2 = forward(X_training,W1.transpose())
            a2 = sigmoid(z2)
            z3 = forward(a2,W2.transpose())
            a3 = sigmoid(z3)
            
            delta3=a3-np.array(Y_training)
            W2_sansbiais = removeBiais(W2)
            delta2 = np.dot(delta3,W2_sansbiais) * inverseSigmoid(z2)

            BigD2 = np.dot(delta3.transpose(),addBiais(a2))
            BigD1 = np.dot(delta2.transpose(),addBiais(X_training))

            regularisation1 = lamda[g]/2*m * (np.sum(W1*W1.copy()))
            regularisation2 = lamda[g]/2*m * (np.sum(W2*W2.copy()))
            BigD2 = BigD2+regularisation2
            BigD1 = BigD1+regularisation1

            W1 = W1 - alpha*1/m*BigD1
            W2 = W2 - alpha*1/m*BigD2


        #once weight has been updated , try it with test data
        z2 = forward(X_test,W1.transpose())
        a2 = sigmoid(z2)
        z3 = forward(a2,W2.transpose())
        a3 = sigmoid(z3)

        #predicted array contains data with value converted in 0 or 1 to compare it with actual data
        predicted = []
        for p in range (0,len(a3)):
            index = indexHighest(a3[p])
            predicted.append(yValue[index])

        #compare predicted and actual
        average_precision = precision_recall_fscore_support(np.array(Y_test),np.array(predicted), average='weighted')
        recall = average_precision[0]
        accuracy = average_precision[1]
        fmesure = average_precision[2]
        meanAccuracy += accuracy
        meanRecall += recall
        meanFMesure += fmesure
                
    confusionX = convertDataToNumber(np.array(predicted))
    confusionY = convertDataToNumber(np.array(Y_test))

    print(confusion_matrix(confusionY, confusionX, labels=['1','2','3','4','5','6','7','8']))
    
    print('Mean accuracy')
    print(meanAccuracy/k)
    print('Mean recall')
    print(meanRecall/k)
    print('Mean fmesure')
    print(meanFMesure/k)
