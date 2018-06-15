from tec.ic.ia.pc1 import g08
import numpy
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from sklearn.preprocessing import StandardScaler,MinMaxScaler

def shaped_data(dataset):
    dataset = numpy.array(dataset)


    X = dataset[:,1:-2].astype(float)
    X0 = dataset[:,0]
    X32 = dataset[:,-2]
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

    X = numpy.concatenate((X0.reshape((-1, 1)), X), axis=1)
    X = numpy.concatenate((X, X32.reshape((-1, 1))), axis=1)

    # convert integers to dummy variables (i.e. one hot encoded)
    dummy_y = np_utils.to_categorical(encoded_Y)






    return X,dummy_y


def shaped_data2(dataset):
    dataset = numpy.array(dataset)


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





    X = numpy.concatenate((X0.reshape((-1, 1)), X), axis=1)


    encoderX31 = LabelEncoder()
    encoderX31.fit(X31)
    X31 = encoderX31.transform(X31)


    #X = numpy.concatenate((X, X31.reshape((-1, 1))), axis=1)

    X_second = X


    dummy_y2 = np_utils.to_categorical(X32)
    X = numpy.concatenate((X, X32.reshape((-1, 1))), axis=1)

    # convert integers to dummy variables (i.e. one hot encoded)
    dummy_y = np_utils.to_categorical(encoded_Y)

    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)

    scaler.fit(X_second)
    X_second = scaler.transform(X_second)
    
    return [X_second,X32],[X_second,encoded_Y],[X,encoded_Y]


def shaped_data_regression(dataset):
    dataset = numpy.array(dataset)


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





    X = numpy.concatenate((X0.reshape((-1, 1)), X), axis=1)


    encoderX31 = LabelEncoder()
    encoderX31.fit(X31)
    X31 = encoderX31.transform(X31)


    #X = numpy.concatenate((X, X31.reshape((-1, 1))), axis=1)

    X_second = X


    dummy_y2 = np_utils.to_categorical(X32)
    X = numpy.concatenate((X, X32.reshape((-1, 1))), axis=1)

    # convert integers to dummy variables (i.e. one hot encoded)
    dummy_y = np_utils.to_categorical(encoded_Y)

    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)

    scaler.fit(X_second)
    X_second = scaler.transform(X_second)
    
    return [X_second,dummy_y2],[X_second,dummy_y],[X,dummy_y]





def shaped_data_no_bin(dataset):
    dataset = numpy.array(dataset)


    X = dataset[:,1:-2].astype(float)
    X0 = dataset[:,0]
    X32 = dataset[:,-2]
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

    X = numpy.concatenate((X0.reshape((-1, 1)), X), axis=1)
    X = numpy.concatenate((X, X32.reshape((-1, 1))), axis=1)

    Y = numpy.array([g08.PARTIDOS.index(Y[i]) for i in range(len(Y))])

    X = numpy.concatenate((X, Y.reshape((-1, 1))), axis=1)

    return X




def shaped_data_no_bin2(dataset):
    dataset = numpy.array(dataset)

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



    X = numpy.concatenate((X0.reshape((-1, 1)), X), axis=1)
    X = numpy.concatenate((X, X31.reshape((-1, 1))), axis=1)

    X_second = X
    
    X = numpy.concatenate((X, X32.reshape((-1, 1))), axis=1)

    X_first = X
    
    
    


    
    Y = numpy.array([g08.PARTIDOS.index(Y[i]) for i in range(len(Y))])

    X = numpy.concatenate((X, Y.reshape((-1, 1))), axis=1)


    X_second = numpy.concatenate((X_second, Y.reshape((-1, 1))), axis=1)
    
    return X_first,X_second,X




def shaped_data_kdtrees(dataset):
    dataset = numpy.array(dataset)

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


    scaler = MinMaxzScaler()
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
