import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input, decode_predictions, VGG16
import cv2
import argparse
model = VGG16()

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required = True, help = "Path to the image")

args = vars(parser.parse_args())
image = load_img(args["image"], target_size=(224, 224))

image = img_to_array(image)
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

image = preprocess_input(image)

yhat = model.predict(image)

label = decode_predictions(yhat)
# retrieve the most likely result, e.g. highest probability
label = label[0][0]
# print the classification
print(" The object is :",label[1])