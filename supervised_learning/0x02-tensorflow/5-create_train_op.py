#!/usr/bin/env python3
""" create function """
import tensorflow as tf


def create_train_op(loss, alpha):
    """ create train op """
    my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=alpha)
    """my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(
    my_optimizer, loss)
    linear_regressor = tf.estimator.LinearRegressor(
        feature_columns = None,
        optimizer=my_optimizer)
    return my_optimizer"""
    train_op = my_optimizer.minimize(loss)
    return(train_op)
