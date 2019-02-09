"""
ECE196 Face Recognition Project
Author: W Chen

Use this as a template to:
1. load weights for vgg16
2. load images
3. finetune network
4. save weights
"""

import cv2
from keras.models import Model
import keras.applications.vgg16
from keras import optimizers
from keras.layers import Dropout, Flatten, Dense
from keras.utils.np_utils import to_categorical
import numpy as np
import glob
import os
import random

IMG_H, IMG_W, NUM_CHANNELS = 224, 224, 3
MEAN_PIXEL = np.array([104., 117., 123.]).reshape((1, 1, 3))
TRAIN_DIR = '../data/training'  # TODO
VAL_DIR = '../data/validation'  # TODO
NUM_EPOCHS = 1  # TODO
BATCH_SIZE = 16
NUM_CLASSES = 19  # TODO


def load_model():
    # TODO: use VGG16 to load lower layers of vgg16 network and declare it as base_model
    # TODO: use 'imagenet' for weights, include_top=False, (IMG_H, IMG_W, NUM_CHANNELS) for input_shap

	
	keras.applications.vgg16.VGG16(include_top=False, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=19)
	print('Model weights loaded.')
	base_out = base_model.output
    # TODO: add a flatten layer, a dense layer with 256 units, a dropout layer with 0.5 rate,
    # TODO: and another dense layer for output. The final layer should have the same number of units as classes
    	model = Model(inputs=base_model.input, outputs=predictions)	
	model.add(Flatten())
	model.add(Dense(256,activation = 'relu'))
	model.add(Dropout(0.5))
	model.add(Dense(19, activation = 'softmax'))
	print 'Build model'

	model.summary()

    # TODO: compile the model, use SGD(lr=1e-4,momentum=0.9) for optimizer, 'categorical_crossentropy' for loss,
    # TODO: and ['accuracy'] for metrics
	sgd = optimizers.SGD(lr = 1e-4, momentum=0.9)
	model.compile(loss = 'categorical crossentropy', optimizer = sgd, metrics = 'accuracy')
	print 'Compile model'
	return model


def load_data(src_path):
    # under train/val/test dirs, each class is a folder with numerical numbers
    # X: number_images * height * width * channels
    # Y: number_images * 1
    class_path_list = sorted(glob.glob(os.path.join(src_path, '*')))
    image_path_list = []
    for class_path in class_path_list:
        image_path_list += sorted(glob.glob(os.path.join(class_path, '*jpg')))
    random.shuffle(image_path_list)
    num_images = len(image_path_list)
    print '-- This set has {} images.'.format(num_images)
    X = np.zeros((num_images, IMG_H, IMG_W, NUM_CHANNELS))
    Y = np.zeros((num_images, 1))
    # read images and labels
    for i in range(num_images):
        image_path = image_path_list[i]
        label = int(image_path.split('/')[-2])
        image = cv2.imread(image_path, 1)
        image = cv2.resize(image, (IMG_H, IMG_W)) - MEAN_PIXEL
        X[i, :, :, :] = image
        Y[i, :] = label
    Y = to_categorical(Y, NUM_CLASSES)
    return X, Y


def main():
    # make model
    model = load_model()
    print 'VGG16 created\n'

    # read train and validation data and train the model for n epochs
    print 'Load train data:'
    X_train, Y_train = load_data(TRAIN_DIR)
    print 'Load val data:'
    X_val, Y_val = load_data(VAL_DIR)
    # TODO: Train model
    model.fit()
    # TODO: Save model weight
    model.save()
    print 'model weights saved.'
    return


if __name__ == '__main__':
    main()
