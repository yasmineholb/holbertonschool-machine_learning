#!/usr/bin/env python3
""" train function """
import tensorflow as tf

def evaluate(X, Y, save_path):
	""" evaluate function"""
	with tf.Session() as sess:
		#saver=tf.train.import_meta_graph(save_path+'.meta') 
		saver.restore(sess, save_path)
		sess.run(tf.global_variables_initializer())
		sess.run(tf.local_variables_initializer())
        	X_saved = tf.get_collection('X')
        	y_saved = tf.get_collection('y')
		train_op_saved = tf.get_collection('train_op')
        	accuracy_saved = tf.get_collection('accuracy')
        	loss_saved = tf.get_collection('loss')
        	y_pred_saved = tf.get_collection('y_pred')
		X = X_saved[0]
		y = y_saved[0]
		loss = loss_saved[0]
		accuracy = accuracy_saved[0]
		train_op = train_op_saved[0]
		y_pred = y_pred_saved[0]
       		y_pred, accuracy, loss = session.run((y_pred, accuracy, loss),
					 feed_dict={X: X, y: Y })
    return(y_pred, accuracy, loss)

        
