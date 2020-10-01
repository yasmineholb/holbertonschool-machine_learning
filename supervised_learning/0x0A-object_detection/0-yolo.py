#!/usr/bin/env python3
""" Yolo class """
import tensorflow.keras as K


class Yolo():
    """ class that uses the Yolo v3 algorithm to perform object detection """
    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        """ class constructor """
        self.model = K.models.load_model(filepath=model_path)
        with open(classes_path, 'r') as fl:
            self.class_names = [line.split("\n")[0] for line in fl.readlines()]
        self.class_t = class_t
        self.nms_t = nms_t
        self.anchors = anchors
