import numpy
import pandas
from tec.ic.ia.p1 import g08_data
from tec.ic.ia.pc1 import g08

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import StratifiedKFold


'''
def baseline_model2(y_len,x_len):
    # create model
    model = Sequential()
    model.add(Dense(x_len*4, input_dim=x_len, activation='relu'))
    model.add(Dense(x_len*3, activation='relu'))
    model.add(Dense(x_len*2, activation='relu'))
    model.add(Dense(x_len,   activation='relu'))
    model.add(Dense(y_len , activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
'''
def baseline_model(y_len, x_len, hidden_layer_amount, hidden_unit_amount, activation_fun):

    model = Sequential()
    model.add(Dense(66, input_dim=x_len, activation=activation_fun))
    while hidden_layer_amount > 0:
	    model.add(Dense(hidden_unit_amount, activation=activation_fun))
	    hidden_layer_amount -= 1
    model.add(Dense(y_len, activation='softmax'))
    # Compile model
    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy'])
    return model

def non_shuffling_train_test_split(X, y, test_size=0.2):
    i = int((1 - test_size) * X.shape[0]) + 1
    X_train, X_test = numpy.split(X, [i])
    y_train, y_test = numpy.split(y, [i])
    return X_train, X_test, y_train, y_test

def execute_model(hidden_layer_amount, hidden_unit_amount, activation_fun, dataset, test_percentage):



    # fix random seed for reproducibility
    seed = 7
    numpy.random.seed(seed)

    #################
    # First Round
    #################

    [X1, Y1],[X2, Y2],[X3, Y3] = g08_data.shaped_data2(dataset)
    X_train, X_test, Y_train, Y_test = non_shuffling_train_test_split(X1, Y1, test_percentage/100)



    cvmodels = []
    cvscores = []
    n_split = max(Y_test)//2
    if n_split < 2: n_split = 2
    kfold = StratifiedKFold(n_splits=n_split, shuffle=True, random_state=seed)
    for train, test in kfold.split(X_train, Y_train):


        dummy_y = np_utils.to_categorical(Y_train)

        estimator = baseline_model(len(dummy_y[0]), len(X_train[0]), hidden_layer_amount, hidden_unit_amount, activation_fun)

        estimator.fit(X_train[train], dummy_y[train], epochs=100, batch_size=100, verbose=0)

        scores = estimator.evaluate(X_train[test], dummy_y[test], verbose=0)

        cvscores.append(scores[1] * 100)
        cvmodels.append(estimator)

    first_acc_train = max(cvscores)
    estimator = cvmodels[cvscores.index(max(cvscores))]



    predictions = estimator.predict_classes(X_train)

    success = 0
    for i in range(len(predictions)):
        if predictions[i] == Y_train[i]:
            success+=1
    first = [g08.PARTIDOS[int(predictions[i])] for i in range(len(predictions))]



    predictions = estimator.predict_classes(X_test)

    success = 0
    for i in range(len(predictions)):
        if predictions[i] == Y_test[i]:
            success+=1
    
    train_first = [g08.PARTIDOS[int(predictions[i])] for i in range(len(predictions))]
    first_acc = (110*success/len(predictions))
    first += train_first


 


    #################
    # Second Round
    #################

    X_train, X_test, Y_train, Y_test = non_shuffling_train_test_split(X2, Y2, test_percentage/100)

    cvmodels = []
    cvscores = []
    kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
    for train, test in kfold.split(X_train, Y_train):


        dummy_y = np_utils.to_categorical(Y_train)

        estimator = baseline_model(len(dummy_y[0]),len(X_train[0]), hidden_layer_amount, hidden_unit_amount, activation_fun)

        estimator.fit(X_train[train], dummy_y[train], epochs=100, batch_size=100, verbose=0)

        scores = estimator.evaluate(X_train[test], dummy_y[test], verbose=0)

        cvscores.append(scores[1] * 100)
        cvmodels.append(estimator)

    second_acc_train = max(cvscores)
    estimator = cvmodels[cvscores.index(max(cvscores))]



    predictions = estimator.predict_classes(X_train)

    success = 0
    for i in range(len(predictions)):
        if predictions[i] == Y_train[i]:
            success+=1
    second = [g08.PARTIDOS2[int(predictions[i])] for i in range(len(predictions))]


    predictions = estimator.predict_classes(X_test)


    success = 0
    for i in range(len(predictions)):
        if predictions[i] == Y_test[i]:
            success+=1
    
    train_second = [g08.PARTIDOS2[int(predictions[i])] for i in range(len(predictions))]
    second_acc = (110*success/len(predictions))
    second += train_second




    #################
    # ThirdRound
    #################

    X_train, X_test, Y_train, Y_test = non_shuffling_train_test_split(X3, Y3, test_percentage/100)

    cvmodels = []
    cvscores = []
    kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
    for train, test in kfold.split(X_train, Y_train):


        dummy_y = np_utils.to_categorical(Y_train)

        estimator = baseline_model(len(dummy_y[0]),len(X_train[0]), hidden_layer_amount, hidden_unit_amount, activation_fun)

        estimator.fit(X_train[train], dummy_y[train], epochs=100, batch_size=100, verbose=0)

        scores = estimator.evaluate(X_train[test], dummy_y[test], verbose=0)

        cvscores.append(scores[1] * 100)
        cvmodels.append(estimator)


    third_acc_train = max(cvscores)
    estimator = cvmodels[cvscores.index(max(cvscores))]

    predictions = estimator.predict_classes(X_train)

    success = 0
    for i in range(len(predictions)):
        if predictions[i] == Y_train[i]:
            success+=1
    third = [g08.PARTIDOS2[int(predictions[i])] for i in range(len(predictions))]

    print(predictions)
    print(third)

    predictions = estimator.predict_classes(X_test)




    success = 0
    for i in range(len(predictions)):
        if predictions[i] == Y_test[i]:
            success+=1
    
    train_third = [g08.PARTIDOS2[int(predictions[i])] for i in range(len(predictions))]
    third_acc = (110*success/len(predictions))
    third += train_third


 

    finalDict = {
            'res_1':        first,
            'res_2':        second,
            'res_3':        third,
            'err_train':    (first_acc+second_acc+third_acc)/3,
            'err_test':     (first_acc_train+second_acc_train+third_acc_train)/3,
            'train_set':    [True]*len(X1)+[False]*len(Y1)
        }
    return finalDict



if __name__ == '__main__':
    # execute_model(4, 'relu')
    execute_model(5, 60, 'relu')
