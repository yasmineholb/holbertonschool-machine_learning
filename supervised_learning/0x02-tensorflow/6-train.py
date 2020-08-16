#!/usr/bin/env python3
""" train function """
import tensorflow as tf


def train(X_train, Y_train, X_valid, Y_valid, layer_sizes, activations, alpha, iterations, save_path="/tmp/model.ckpt"):
    """ train function """
    calculate_accuracy = __import__('3-calculate_accuracy').calculate_accuracy
    calculate_loss = __import__('4-calculate_loss').calculate_loss
    create_placeholders = __import__('0-create_placeholders').create_placeholders
    create_train_op = __import__('5-create_train_op').create_train_op
    forward_prop = __import__('2-forward_prop').forward_prop
    add_to_collection()
    X_train, Y_train = create_placeholders(nx, classes)
    p = forward_prop(x, layer_sizes, activations)
    for i in range(0, iterations+1, 100):
        print("After {} iterations:".format{i})
        print("\tTraining Cost: {cost}".format{})   """create_layer(prev, n, activation)"""
        print("\tTraining Accuracy: {accuracy}".format(calculate_accuracy(y, y_pred)))
        print("\tValidation Cost: {cost}".format{})  
        print("\tValidation Accuracy: {accuracy}".format{}) """calculate_loss(y, y_pred)"""
        print(create_train_op(loss, alpha)
        
        
