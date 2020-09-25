#!/usr/bin/env python3
"""Civar10v2.ipynb"""
import tensorflow.keras as K
import tensorflow as tf


def preprocess_data(X, Y):
    """ Function that pre-processes the data for your model """
    X1 = K.applications.resnet50.preprocess_input(X)
    Y1 = K.utils.to_categorical(Y, 10)
    return X1, Y1


if __name__ == "__main__":
    """ main program """
    (x_train, y_train), (x_test, y_test) = K.datasets.cifar10.load_data()
    x_train, y_train = preprocess_data(x_train, y_train)
    x_test, y_test = preprocess_data(x_test, y_test)
    inp = K.Input(shape=(32, 32, 3))
    res = K.applications.ResNet50(include_top=False,
                                  weights="imagenet",
                                  input_tensor=inp)
    for layer in res.layers[:-30]:
        layer.trainable = False
    model = K.models.Sequential()
    model.add(K.layers.Lambda(lambda image: tf.image.resize(image,
                                                            (224, 224))))
    model.add(res)
    model.add(K.layers.Flatten())
    model.add(K.layers.BatchNormalization())
    model.add(K.layers.Dense(256, activation='relu'))
    model.add(K.layers.Dropout(0.5))
    model.add(K.layers.BatchNormalization())
    model.add(K.layers.Dense(128, activation='relu'))
    model.add(K.layers.Dropout(0.5))
    model.add(K.layers.BatchNormalization())
    model.add(K.layers.Dense(64, activation='relu'))
    model.add(K.layers.Dropout(0.5))
    model.add(K.layers.BatchNormalization())
    model.add(K.layers.Dense(10, activation='softmax'))

    check = K.callbacks.ModelCheckpoint(filepath="cifar10.h5",
                                        monitor="val_acc",
                                        mode="max",
                                        save_best_only=True)
    model.compile(loss='categorical_crossentropy',
                  optimizer=K.optimizers.RMSprop(lr=2e-5),
                  metrics=['accuracy'])
    hist = model.fit(x_train, y_train, batch_size=32, epochs=10, verbose=1,
                     validation_data=(x_test, y_test), callbacks=[check])
    model.summary()
    model.save('cifar10.h5')
