import os

# GPU USAGE NOTIFICATIONS OFF 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist # db with handwritten number images
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPooling2D

# x_train - training selection images
# y_train - vector of corresponding values for training selection
# x_test - test selection images
# y_test - vector of corresponding values for test selection
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# value normalization
x_train = x_train / 255
x_test = x_test / 255
y_train_cat = keras.utils.to_categorical(y_train, 10)
y_test_cat = keras.utils.to_categorical(y_test, 10)

x_train = np.expand_dims(x_train, axis=3)
x_test = np.expand_dims(x_test, axis=3) 


# BUILDING NN
# ---------- ---------- ---------- #
model = keras.Sequential([
 Conv2D(32, (3,3), padding='same', activation='relu', input_shape=(28, 28,
1)),
 MaxPooling2D((2, 2), strides=2),
 Conv2D(64, (3,3), padding='same', activation='relu'),
 MaxPooling2D((2, 2), strides=2),
 Flatten(),
 Dense(128, activation='relu'),
 Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
             loss='categorical_crossentropy',
             metrics=['accuracy'])

his = model.fit(x_train, y_train_cat, batch_size=32, epochs=5, validation_split=0.2)
# ---------- ---------- ---------- #


# NN TESTING 
# ---------- ---------- ---------- #

model.evaluate(x_test, y_test_cat)
# ---------- ---------- ---------- #

