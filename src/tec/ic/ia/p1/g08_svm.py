import numpy
import pandas
from tec.ic.ia.p1 import g08_data
from tec.ic.ia.pc1 import g08
from sklearn.svm import LinearSVC
from sklearn.svm import SVC

def non_shuffling_train_test_split(X, y, test_size=0.2):
    i = int((1 - test_size) * X.shape[0]) + 1
    X_train, X_test = numpy.split(X, [i])
    y_train, y_test = numpy.split(y, [i])
    return X_train, X_test, y_train, y_test




def execute_model(dataset, test_percentage):
	[X1, Y1],[X2, Y2],[X3, Y3] = g08_data.shaped_data2(dataset)


	x_train, x_test, y_train, y_test = non_shuffling_train_test_split(X1, Y1, test_percentage/100)


	model = LinearSVC()
	model.fit(x_train, y_train.ravel())


	#Calculate Test Prediction


	predictions = model.predict(x_train)
	first = [g08.PARTIDOS[int(predictions[i])] for i in range(len(predictions))]

	predictions = model.predict(x_test)
	first += [g08.PARTIDOS[int(predictions[i])] for i in range(len(predictions))]

	first_acc_train = model.score(x_train,y_train.ravel())
	first_acc = model.score(x_test,y_test.ravel())





	x_train, x_test, y_train, y_test = non_shuffling_train_test_split(X2, Y2, test_percentage/100)




	model = LinearSVC()
	model.fit(x_train, y_train.ravel())


	#Calculate Test Prediction


	predictions = model.predict(x_train)

	second = [g08.PARTIDOS2[int(predictions[i])] for i in range(len(predictions))]

	predictions = model.predict(x_test)
	second += [g08.PARTIDOS2[int(predictions[i])] for i in range(len(predictions))]

	second_acc_train = model.score(x_train,y_train.ravel())
	second_acc = model.score(x_test,y_test.ravel())




	x_train, x_test, y_train, y_test = non_shuffling_train_test_split(X3, Y3, test_percentage/100)

	model = LinearSVC()
	model.fit(x_train, y_train.ravel())


	#Calculate Test Prediction


	predictions = model.predict(x_train)
	third = [g08.PARTIDOS2[int(predictions[i])] for i in range(len(predictions))]

	predictions = model.predict(x_test)
	third += [g08.PARTIDOS2[int(predictions[i])] for i in range(len(predictions))]

	third_acc_train = model.score(x_train,y_train.ravel())
	third_acc = model.score(x_test,y_test.ravel())


	#print(first)
	print(first_acc)
	print()
	#print(second)
	print(second_acc)
	print()
	#print(third)
	print(third_acc)

	finalDict = {
	        'res_1':        first,
	        'res_2':        second,
	        'res_3':        third,
	        'err_train':    (first_acc+second_acc+third_acc)/3,
	        'err_test':     (first_acc_train+second_acc_train+third_acc_train)/3,
	        'train_set':    [True]*len(X1)+[False]*len(Y1)
	    }
	return finalDict


execute_model(g08.generar_muestra_pais(10000,1),20)