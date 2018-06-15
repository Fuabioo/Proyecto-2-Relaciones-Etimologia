import collections
import itertools
import math
import random
import numpy
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split

import numpy
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from sklearn.preprocessing import StandardScaler,MinMaxScaler

from tec.ic.ia.p1 import g08_data
from tec.ic.ia.pc1 import g08



"""
def getParsedData(n):
    data1round, data2round, data2round1 = g08_data.shaped_data_kdtrees(n)
    return data1round, data2round, data2round1
"""
"""
def genDataSet(n, m):
    dataSet = []
    dataSet = [list(random.randint(0,1) for x in range(m)) for y in range(n)]
    for i in dataSet:
        if i[3]%2 == 0:
            i[-1] = 'PAC'
        else:
            i[-1] = 'RN'


    return dataSet
"""

# Formats the dataset to be used on each round 
def shape_data(dataset):
    X = dataset[:,1:-3].astype(float)
    X0 = dataset[:,0]
    X32 = dataset[:,-2]
    X31 = dataset[:,-3]
    Y = dataset[:,-1]
    # encode class values as integers
    encoderY = LabelEncoder()
    encoderY.fit(Y)
    encoded_Y = encoderY.transform(Y)
    # encode class values as integers
    encoderX0 = LabelEncoder()
    encoderX0.fit(X0)
    X0 = encoderX0.transform(X0)
    # encode class values as integers
    encoderX32 = LabelEncoder()
    encoderX32.fit(X32)
    X32 = encoderX32.transform(X32)
    encoderX31 = LabelEncoder()
    encoderX31.fit(X31)
    X31 = encoderX31.transform(X31)
    scaler = MinMaxScaler()
    scaler.fit(X)
    X = scaler.transform(X)
    X = numpy.concatenate((X0.reshape((-1, 1)), X), axis=1)
    X = numpy.concatenate((X, X31.reshape((-1, 1))), axis=1)
    X_second = X
    X = numpy.concatenate((X, X32.reshape((-1, 1))), axis=1)
    X_first = X
    Y = numpy.array([g08.PARTIDOS.index(Y[i]) for i in range(len(Y))])
    X = numpy.concatenate((X, Y.reshape((-1, 1))), axis=1)
    X_second = numpy.concatenate((X_second, Y.reshape((-1, 1))), axis=1)
    return X_first,X_second,X



def square_distance(a, b):
    square = 0
    a = a[0:-1]
    b = b[0:-1]
    for elemX, elemY in zip(a, b):
        dist = elemX - elemY
        square += dist * dist
    return square

Node = collections.namedtuple("Node", 'point axis label left right')

class KDTree(object):
    #Modificaciones:
    # Datos de entrada, adaptados a los datos de prueba generados en el PC1
    # Cálculo del SqrtError, adaptado para ignorar el voto, tomando en cuenta sólo los indicadores
    # Forma general, procesamiento correcto de los datos de entrada en el nuevo formato
    # Procesamiento de listas con vecinos cercanos
    # Valor de retorno


    def __init__(self, k, objects=[]):

        def build_tree(objects, axis=0):

            if not objects:
                return None
            objects.sort(key=lambda element: element[axis])
            median_idx = len(objects) // 2
            median_point= objects[median_idx][0:-1]
            median_label = objects[median_idx][-1]
            next_axis = (axis + 1) % k
            return Node(median_point, axis, median_label,
                        build_tree(objects[:median_idx], next_axis),
                        build_tree(objects[median_idx + 1:], next_axis))

        self.root = build_tree(list(objects))

    def knn(self, destination, k):
        bestOccurrences = []
        bestSDs = []
        best = [None, None, float('inf')]
        # state of search: best point found, its label,
        # lowest squared distance

        def recursive_search(here):

            if here is None:
                return
            point, axis, label, left, right = here

            here_sd = square_distance(point, destination)

            best[:] = point, label, here_sd
            bestOccurrences.append(best[1])
            bestSDs.append(here_sd)

            if len(bestSDs) > k:
                idx = bestSDs.index(max(bestSDs))
                bestOccurrences.pop(idx)
                bestSDs.pop(idx)


            diff = destination[axis] - point[axis]
            close, away = (left, right) if diff <= 0 else (right, left)

            recursive_search(close)
            if diff ** 2 < min(bestSDs):
                recursive_search(away)

        recursive_search(self.root)
        return bestOccurrences, bestSDs

# Generates the tree and calculates the precision and the predictions 
def calculateTreeData(dataSet, testSet, maxLeafSize, k):
    
    
    predictionList = []
    isTraining = []
    tree = 0
    print("Generating tree")
    tree = KDTree(maxLeafSize, dataSet)
    

    print("Processing")

    accuracy = 0
    for testPerson in testSet:
        # For each person make the search of the N nearest neighbors
        bestOccurrences, bestSDs = tree.knn(testPerson, k)
        predict =  max(set(bestOccurrences), key = bestOccurrences.count)
        predictionList.append(predict)
        isTraining.append('True')
        if predict == testPerson[-1]:

            accuracy += 1

    accuracy = accuracy / len(testSet)
    print("Total accuracy: ", accuracy)
    return tree, accuracy, predictionList, isTraining


# Calculates the tree data for each round
def kdknn(allSets, maxLeafSize = 10, k = 3):
    
    #
    if not allSets:
        return

    set1 = allSets[0][0]
    tSet1 = allSets[0][1]
    set2 = allSets[1][0]
    tSet2 = allSets[1][1]
    set3 = allSets[2][0]
    tSet3 = allSets[2][1]

    destinationSet = tSet3

    #Ronda 1
    print("Creating tree round 1")
    tree1, accuracy1, predictions1, isTraining = calculateTreeData(set1, tSet1, maxLeafSize, k)

    #Ronda 2 sin ronda 1
    print("Creating tree round 2 without round 1")
    tree2, accuracy2, predictions2, _ = calculateTreeData(set2, tSet2, maxLeafSize, k)

    #Ronda 2 con ronda 1
    print("Creating tree round 2 with round 1")
    tree3, accuracy3, predictions3, _ = calculateTreeData(set3, tSet3, maxLeafSize, k)


    return destinationSet, [tree1, tree2, tree3] , [predictions1, predictions2, predictions3], [accuracy1, accuracy2, accuracy3], isTraining

# Defines train/validate parts of the dataset for cross validation
def processSplittedData(splitted, index):
    # Lists with the datasets splitted
    datasetPerRound = []

    trainWith = splitted.copy()
    testWith = trainWith.pop(index)
    trainWith = list(itertools.chain.from_iterable(trainWith))

    datasetPerRound.append(trainWith)
    datasetPerRound.append(testWith)

    return datasetPerRound


# Switches 2 columns of a given dataset
def switchColumns(dataSet, x, y):
    for i in range(len(dataSet)):
        dataSet[i][x], dataSet[i][y] = dataSet[i][y], dataSet[i][x] 
    return dataSet



# Divides the dataset in training and test based on the percentage
def divide_dataset(dataSet, percent):
    return dataSet[0: int(((len(dataSet)*(1-percent))))] , dataSet[int(((len(dataSet)*(1-percent)))):]


# Makes the cross validation training and calls the final tests
def cross_validate(dataset = [], parts = 2, percent = 20, k=3):
    percent = percent/100 if percent>1 else percent
    # Get full datasets 1, 2, 3 (The same dataset expressed in different ways)

    trainDataset, testDataset = divide_dataset(dataset, percent)

    data1, data2, data3 = shape_data(trainDataset)
    isTraining = []
    trees1 = []
    trees2 = []
    trees3 = []
    predictions1 = []
    predictions2 = []
    predictions3 = []
    accuracies1 = []
    accuracies2 = []
    accuracies3 = []

    data3 = switchColumns(data3.copy(), 7, len(data3[0])-2)

    # Format data for cross validation
    parts = int(len(data1)//parts)


    # Cross validate data 1
    data1split = [data1[i:i+parts] for i  in range(0, len(data1), parts)]
    data2split = [data2[i:i+parts] for i  in range(0, len(data2), parts)]
    data3split = [data3[i:i+parts] for i  in range(0, len(data3), parts)]
    #list(itertools.chain.from_iterable(lists))
    
    for i in range(len(data3split)):
        
        allDatasets = []
        

        print("TESTING WITH: ", i)

        

        # Round 1
        datasetPerRound = processSplittedData(data1split, i)
        allDatasets.append(datasetPerRound)

        # Round 2 without
        datasetPerRound = processSplittedData(data2split, i)
        allDatasets.append(datasetPerRound)

        # Round 2 with
        datasetPerRound = processSplittedData(data3split, i)
        allDatasets.append(datasetPerRound)
        
        _, trees , predictions, accuracies, training = kdknn(allSets = allDatasets, k=k)
        isTraining+=training
        trees1.append(trees[0])
        trees2.append(trees[1])
        trees3.append(trees[2])
        predictions1 += predictions[0]
        predictions2 += predictions[1]
        predictions3 += predictions[2]
        accuracies1.append(accuracies[0])
        accuracies2.append(accuracies[1])
        accuracies3.append(accuracies[2])


    length = len(dataset) - len(isTraining)
    for i in range(length):
        isTraining.append('False')

    finalSet1, finalSet2, finalSet3 = shape_data(testDataset) #CHANGE
    print("-------------------\n finalsetlen", len(finalSet1))

    bestTree1, bestTree2, bestTree3 = getBestTrees(trees1, trees2, trees3, accuracies1, accuracies2, accuracies3)
    

    # Prepare output
    finalDict = finalTests([bestTree1, bestTree2, bestTree3], [finalSet1, finalSet2, finalSet3])
    finalDict['err_train'] = sum([  sum(accuracies1)/float(len(accuracies1)) , sum(accuracies2)/float(len(accuracies2)) , sum(accuracies3)/float(len(accuracies3)) ]) / 3
    
    finalDict['train_set'] = isTraining
    finalDict['res_1'] = [g08.PARTIDOS[int(predict)] for predict in predictions1] + finalDict['res_1']
    finalDict['res_2'] = [g08.PARTIDOS[int(predict)] for predict in predictions2] + finalDict['res_2']
    finalDict['res_3'] = [g08.PARTIDOS[int(predict)] for predict in predictions3] + finalDict['res_3']
    return finalDict

# Makes the final test with the untouched dataset
def finalTests(bestTrees, dataSets, k=3):
    dataSetIndex = 0

    finalDict = {
        'res_1':        [],
        'res_2':        [],
        'res_3':        [],
        'err_train':    0.0,
        'err_test':     0.0,
        'train_set':    []
    }


    totalaccuracy=0
    for dataSet in dataSets:

        resString = 'res_'+str(dataSetIndex+1)

        tree = bestTrees[dataSetIndex]
        print("Processing tests")
        accuracy = 0
        for testPerson in dataSet:
            bestOccurrences, bestSDs = tree.knn(testPerson, k)
            predict =  max(set(bestOccurrences), key = bestOccurrences.count)
            if predict == testPerson[-1]:
                accuracy += 1
            finalDict[resString].append(g08.PARTIDOS[int(predict)])


        accuracy = accuracy / len(dataSet)
        totalaccuracy += accuracy
        dataSetIndex += 1
        print("Error ",dataSetIndex,": ", 1-accuracy)
    
    finalDict['err_test']= totalaccuracy/3

    return finalDict

# Returns the best trees for each round based on the precision they had
def getBestTrees(trees1, trees2, trees3, accuracies1, accuracies2, accuracies3):
    print("Best accuracy 1", max(accuracies1))
    ind1 = accuracies1.index(max(accuracies1))
    print("Best accuracy 2", max(accuracies2))
    ind2 = accuracies2.index(max(accuracies2))
    print("Best accuracy 3", max(accuracies3))
    ind3 = accuracies3.index(max(accuracies3))


    return trees1[ind1], trees2[ind2], trees3[ind3]

if __name__ == '__main__':
    cross_validate(dataset = numpy.array(g08.generar_muestra_pais(1003,1)))