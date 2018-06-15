import numpy
import pandas
from tec.ic.ia.p1 import g08_data
from tec.ic.ia.pc1 import g08
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from sklearn.model_selection import train_test_split
from keras.utils import np_utils
import tensorflow as tf

# fix random seed for reproducibility



def regression(dataset, percentage, l1=False, l2=False):


	seed = 7
	numpy.random.seed(seed)



	learning_rate = 0.001
	num_epochs = 1500
	display_step = 300
	# load dataset

	[X1, Y1],[X2, Y2],[X3, Y3] = g08_data.shaped_data_regression(dataset)



	x_train, x_test, y_train, y_test = train_test_split(X1, Y1, test_size = percentage/100, random_state=0)

	num_features = x_train.shape[1]

	learning_rate = 0.01
	training_epochs = 1000

	tf.reset_default_graph()

	# for visualize purpose in tensorboard we use tf.name_scope
	with tf.name_scope("Declaring_placeholder"):    
	    # X is placeholdre for iris features. We will feed data later on
	    X = tf.placeholder(tf.float32, [None, len(x_train[0])] )
	    # y is placeholder for iris labels. We will feed data later on
	    y = tf.placeholder(tf.float32, [None, len(y_train[0])] )
	    
	with tf.name_scope("Declaring_variables"):
	    # W is our weights. This will update during training time
	    W = tf.Variable(tf.zeros([len(x_train[0]), len(y_train[0])]))
	    # b is our bias. This will also update during training time
	    b = tf.Variable(tf.zeros( [len(y_train[0])] ))


	Z = tf.add(tf.matmul(X, W), b)
	prediction = tf.nn.softmax(Z)

	# Calculate the cost
	cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits = Z, labels = y))

	# Use Adam as optimization method
	optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

	init = tf.global_variables_initializer()

	cost_history = numpy.empty(shape=[1],dtype=float)

	with tf.Session() as sess:
	    sess.run(init)
	    
	    for epoch in range(training_epochs):
	        _, c  = sess.run([optimizer, cost], feed_dict={X: x_train, y: y_train})
	        #print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c), \ "W=", sess.run(W), "b=", sess.run(b))
	        cost_history = numpy.append(cost_history, c)
	        
	        
	    # Calculate the correct predictions
	    correct_prediction = tf.to_float(tf.greater(prediction, 0.5))

	    # Calculate accuracy on the test set
	    accuracy = tf.reduce_mean(tf.to_float(tf.equal(y, correct_prediction)))


	    prediction=tf.argmax(Z,1)
	    pred = prediction.eval(feed_dict={X: x_train}, session=sess)
	    first = [g08.PARTIDOS[int(pred[i])] for i in range(len(pred))]


	    pred = prediction.eval(feed_dict={X: x_test}, session=sess)


	    y_classes = [numpy.argmax(y, axis=None, out=None) for y in y_test]

	    success = 0
	    for i in range(len(pred)):
	        if pred[i] == y_classes[i]:
	            success+=1
	    first_acc = (110*success/len(pred))
	    first += [g08.PARTIDOS[int(pred[i])] for i in range(len(pred))]
	    first_acc_train = accuracy.eval({X: x_train, y: y_train})








	x_train, x_test, y_train, y_test = train_test_split(X2, Y2, test_size = 0.1, random_state=0)

	num_features = x_train.shape[1]

	learning_rate = 0.01
	training_epochs = 1000

	tf.reset_default_graph()




	# for visualize purpose in tensorboard we use tf.name_scope
	with tf.name_scope("Declaring_placeholder"):    
	    # X is placeholdre for iris features. We will feed data later on
	    X = tf.placeholder(tf.float32, [None, len(x_train[0])] )
	    # y is placeholder for iris labels. We will feed data later on
	    y = tf.placeholder(tf.float32, [None, len(y_train[0])] )
	    
	with tf.name_scope("Declaring_variables"):
	    # W is our weights. This will update during training time
	    W = tf.Variable(tf.zeros([len(x_train[0]), len(y_train[0])]))
	    # b is our bias. This will also update during training time
	    b = tf.Variable(tf.zeros( [len(y_train[0])] ))


	Z = tf.add(tf.matmul(X, W), b)
	prediction = tf.nn.softmax(Z)

	# Calculate the cost
	cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits = Z, labels = y))

	# Use Adam as optimization method
	optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

	init = tf.global_variables_initializer()

	cost_history = numpy.empty(shape=[1],dtype=float)

	with tf.Session() as sess:
	    sess.run(init)
	    
	    for epoch in range(training_epochs):
	        _, c  = sess.run([optimizer, cost], feed_dict={X: x_train, y: y_train})
	        #print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c), \ "W=", sess.run(W), "b=", sess.run(b))
	        cost_history = numpy.append(cost_history, c)
	        
	        
	    # Calculate the correct predictions
	    correct_prediction = tf.to_float(tf.greater(prediction, 0.5))

	    # Calculate accuracy on the test set
	    accuracy = tf.reduce_mean(tf.to_float(tf.equal(y, correct_prediction)))


	    prediction=tf.argmax(Z,1)
	    pred = prediction.eval(feed_dict={X: x_train}, session=sess)
	    second = [g08.PARTIDOS2[int(pred[i])] for i in range(len(pred))]


	    pred = prediction.eval(feed_dict={X: x_test}, session=sess)


	    y_classes = [numpy.argmax(y, axis=None, out=None) for y in y_test]

	    success = 0
	    for i in range(len(pred)):
	        if pred[i] == y_classes[i]:
	            success+=1
	    second_acc = (110*success/len(pred))
	    second += [g08.PARTIDOS2[int(pred[i])] for i in range(len(pred))]

	    second_acc_train = accuracy.eval({X: x_train, y: y_train})




	x_train, x_test, y_train, y_test = train_test_split(X3, Y3, test_size = 0.1, random_state=0)

	num_features = x_train.shape[1]

	learning_rate = 0.01
	training_epochs = 1000

	tf.reset_default_graph()




	# for visualize purpose in tensorboard we use tf.name_scope
	with tf.name_scope("Declaring_placeholder"):    
	    # X is placeholdre for iris features. We will feed data later on
	    X = tf.placeholder(tf.float32, [None, len(x_train[0])] )
	    # y is placeholder for iris labels. We will feed data later on
	    y = tf.placeholder(tf.float32, [None, len(y_train[0])] )
	    
	with tf.name_scope("Declaring_variables"):
	    # W is our weights. This will update during training time
	    W = tf.Variable(tf.zeros([len(x_train[0]), len(y_train[0])]))
	    # b is our bias. This will also update during training time
	    b = tf.Variable(tf.zeros( [len(y_train[0])] ))


	Z = tf.add(tf.matmul(X, W), b)
	prediction = tf.nn.softmax(Z)

	# Calculate the cost
	cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits = Z, labels = y))

	# Use Adam as optimization method
	optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

	init = tf.global_variables_initializer()

	cost_history = numpy.empty(shape=[1],dtype=float)

	with tf.Session() as sess:
	    sess.run(init)
	    
	    for epoch in range(training_epochs):
	        _, c  = sess.run([optimizer, cost], feed_dict={X: x_train, y: y_train})
	        #print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c), \ "W=", sess.run(W), "b=", sess.run(b))
	        cost_history = numpy.append(cost_history, c)
	        
	        
	    # Calculate the correct predictions
	    correct_prediction = tf.to_float(tf.greater(prediction, 0.5))

	    # Calculate accuracy on the test set
	    accuracy = tf.reduce_mean(tf.to_float(tf.equal(y, correct_prediction)))


	    prediction=tf.argmax(Z,1)
	    pred = prediction.eval(feed_dict={X: x_train}, session=sess)
	    third = [g08.PARTIDOS2[int(pred[i])] for i in range(len(pred))]


	    pred = prediction.eval(feed_dict={X: x_test}, session=sess)


	    y_classes = [numpy.argmax(y, axis=None, out=None) for y in y_test]

	    success = 0
	    for i in range(len(pred)):
	        if pred[i] == y_classes[i]:
	            success+=1
	    third_acc = (110*success/len(pred))
	    third += [g08.PARTIDOS2[int(pred[i])] for i in range(len(pred))]
	    third_acc_train = accuracy.eval({X: x_train, y: y_train})

	finalDict = {
			'train_set':        [],
            'res_1':        first,
            'res_2':        second,
            'res_3':        third,
            'err_train':    (first_acc+second_acc+third_acc)/3,
            'err_test':     (first_acc_train+second_acc_train+third_acc_train)/3,
            'train_set':    [True]*len(X1)+[False]*len(Y1)
        }
	return finalDict



if __name__ == '__main__':
	regression()