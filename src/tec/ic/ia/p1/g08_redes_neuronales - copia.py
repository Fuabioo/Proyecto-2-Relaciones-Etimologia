import numpy
import pandas
from tec.ic.ia.pc1 import g08

from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import LabelEncoder,StandardScaler
# fix random seed for reproducibility
seed = 5
numpy.random.seed(seed)
# load dataset
dataframe = numpy.array(g08.generar_muestra_pais(10000,0))

X = dataframe[:,1:-2]

scalerX = StandardScaler()
scalerX.fit(X)
X = scalerX.transform(X)
Y = dataframe[:,-1]


# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)



# define baseline model
def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(len(X[0])*8, input_dim=len(X[0]), init='normal', activation='relu'))
	model.add(Dense(len(X[0])*7, init='normal', activation='relu'))
	model.add(Dense(len(X[0])*6, init='normal', activation='relu'))
	model.add(Dense(len(X[0])*5, init='normal', activation='relu'))
	model.add(Dense(len(X[0])*4, init='normal', activation='relu'))
	model.add(Dense(len(X[0])*3, init='normal', activation='relu'))
	model.add(Dense(len(X[0])*2, init='normal', activation='relu'))
	model.add(Dense(len(X[0]), init='normal', activation='relu'))
	model.add(Dense(len(dummy_y[0]), init='normal', activation='softmax'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model



cvscores = []
X_train, X_test, Y_train, Y_test = train_test_split(X, dummy_y, test_size=0.33, random_state=seed)
model = baseline_model()
model.fit(X_train, Y_train, validation_data=(X_test,Y_test), epochs=150, batch_size=100, verbose=2)

'''



estimator = KerasClassifier(build_fn=baseline_model, nb_epoch=1, batch_size=200, verbose=1)
X_train, X_test, Y_train, Y_test = train_test_split(X, dummy_y, test_size=0.33, random_state=seed)
estimator.fit(X_train, Y_train)

'''


predictions = model.predict(X_test)

y_classes = [numpy.argmax(y, axis=None, out=None) for y in Y_test]

predictions = encoder.inverse_transform(predictions)
Y_test = encoder.inverse_transform(y_classes)

print(predictions)
print(Y_test)

success = 0
for i in range(len(predictions)):
	if predictions[i] == Y_test[i]:
		success+=1
print(success/len(predictions))

print("asdasd")

