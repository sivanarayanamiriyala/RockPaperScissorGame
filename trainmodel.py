from keras.applications import *
from keras.optimizers import *
from keras.utils import *
from keras.layers import *
from keras.models import *
import tensorflow as tf
import cv2
import numpy as np
import os


game={
"rock":0,
"paper":1,
"scissor":2,
"none":3

}


def mapper(val):
    return game[val]


model=Sequential([MobileNet(input_shape=(224, 224, 3), include_top=False),
	Dropout(0.5),
        Conv2D(len(game),(1, 1), padding='valid'),
        Activation('relu'),
        GlobalAveragePooling2D(),
        Activation('softmax')
    ])


imagedata=[]
pathdata=[]
for folder in os.listdir("Images"):
	path=os.path.join("Images",folder)
	if not os.path.isdir(path):
		continue

	for image in os.listdir(path):
		image = cv2.imread(os.path.join(path, image))
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		image = cv2.resize(image,(224, 224))
		imagedata.append(image)
		pathdata.append(folder)

pathdata=list(map(mapper,pathdata))
pathdata = to_categorical(pathdata,len(game))
model.compile(
    optimizer=Adam(lr=0.0001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(np.array(imagedata), np.array(pathdata), epochs=10)
model.save("rock-paper-scissors-model.h5")



