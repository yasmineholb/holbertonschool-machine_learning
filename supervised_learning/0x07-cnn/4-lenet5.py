#!/usr/bin/env python3
""" LeNet-5 (Tensorflow) """
import tensorflow as tf


def lenet5(x, y):
    """ Function that builds a modified version
        of the LeNet-5 architecture using tensorflow """
    init = tf.contrib.layers.variance_scaling_initializer()
    conv1 = tf.layers.Conv2D(filters=6, kernel_size=(5, 5),
                             padding='same',
                             activation=tf.nn.relu,
                             kernel_initializer=init)(x)
    pool1 = tf.layers.MaxPooling2D(pool_size=(2, 2),
                                   strides=(2, 2))(conv1)
    conv2 = tf.layers.Conv2D(filters=16, kernel_size=(5, 5),
                             padding='valid',
                             activation=tf.nn.relu,
                             kernel_initializer=init)(pool1)
    pool2 = tf.layers.MaxPooling2D(pool_size=(2, 2),
                                   strides=(2, 2))(conv2)
    flt = tf.layers.Flatten()(pool2)
    n1 = tf.layers.Dense(units=120, activation=tf.nn.relu,
                         kernel_initializer=init)(flt)
    n2 = tf.layers.Dense(units=84, activation=tf.nn.relu,
                         kernel_initializer=init)(n1)
    n3 = tf.layers.Dense(units=10,
                         kernel_initializer=init)(n2)
    softmax = tf.nn.softmax(n3)
    loss = tf.losses.softmax_cross_entropy(y, n3)
    arg1 = tf.math.argmax(y)
    arg2 = tf.math.argmax(n3)
    eq = tf.math.equal(arg1, arg2)
    cast = tf.cast(eq, dtype=tf.float32)
    accuracy = tf.math.reduce_mean(cast)
    opt = tf.train.AdamOptimizer().minimize(loss)
    return (softmax, opt, loss, accuracy)
