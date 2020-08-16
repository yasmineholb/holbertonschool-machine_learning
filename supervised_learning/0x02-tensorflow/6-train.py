#!/usr/bin/env python3
""" train function """
import tensorflow as tf


def train(X_train, Y_train, X_valid, Y_valid, layer_sizes, activations,
          alpha, iterations, save_path="/tmp/model.ckpt"):
    """ train function """
    calculate_accuracy = __import__('3-calculate_accuracy').calculate_accuracy
    calculate_loss = __import__('4-calculate_loss').calculate_loss
    create_placeholders = __import__(
        '0-create_placeholders').create_placeholders
    create_train_op = __import__('5-create_train_op').create_train_op
    forward_prop = __import__('2-forward_prop').forward_prop
    """ train function """
    classes = Y_train.shape[1]
    nx = X_train.shape[1]
    X, y = create_placeholders(nx, classes)
    y_pred = forward_prop(X, layer_sizes, activations)
    loss = calculate_loss(y, y_pred)
    accuracy = calculate_accuracy(y, y_pred)
    train_op = create_train_op(loss, alpha)
    init = tf.global_variables_initializer()
    init1 = tf.local_variables_initializer()
    with tf.Session() as sess:
        saver = tf.train.Saver()
        init.run()
        init1.run()
        for i in range(iterations+1):
            loss_train = sess.run(loss, feed_dict={
                X: X_train,
                y: Y_train
            })

            accuracy_train = sess.run(loss, feed_dict={
                X: X_train,
                y: Y_train
            })
            sess.run(train_op, feed_dict={
                X: X_valid,
                y: Y_valid
            })
            loss_valid = sess.run(loss, feed_dict={
                X: X_valid,
                y: Y_valid
            })
            accuracy_valid = sess.run(loss, feed_dict={
                X: X_valid,
                y: Y_valid
            })
            if i % 100 == 0:
                print("After {} iterations:".format(i))
                print("\tTraining Cost: {cost}".format(loss_train))
                print("\tTraining Accuracy: {accuracy}".format(accuracy_train))
                print("\tValidation Cost: {cost}".format(loss_valid))
                print("\tValidation Accuracy: {accuracy}".format(
                    accuracy_valid))
    saver = tf.train.Saver()
    return saver.save(sess, save_path)
