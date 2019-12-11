#--------------------------library used---------------------------------------------------
import numpy as np 
from keras.utils import np_utils
from sklearn.utils import shuffle
import cv2
import os
import glob
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from keras.models import Model
from keras.layers import Dense,Flatten
def model_train():
#------------------------data loading and preprocessing------------------------------------
	no_classes=9
	epochs=40
	X,y=[],[]
	train_data_dir="C:\\Users\\hseth\\Desktop\\HCL_project_1\\data\\"

	train_data=[train_data_dir+i for i in os.listdir(train_data_dir)]
	for img in train_data:
		im=image.load_img(img,target_size=(224,224))
		image_array=image.img_to_array(im)
		X.append(image_array)
	for i in train_data:
		if "telephone" in i:
			y.append(0)
		elif "mug" in i:
			y.append(1)
		elif "dog" in i:
			y.append(2)
		elif "cat" in i:
			y.append(3)
		elif "pen" in i:
			y.append(4)
		elif "bottle" in i:
			y.append(5)
		elif "watch" in i:
			y.append(6)
		elif "headphone" in i:
			y.append(7)
		elif "book" in i:
			y.append(8)
#------------------------------------------data-------------------------------------
	X=np.array(X)
	y=np.array(y)
	X,y=shuffle(X,y)
#--------------------------------splitting of data----------------------------------
	Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2,random_state=0)
#--------------------------------normalizing the images------------------------------
	Xtrain=Xtrain/255
	Xtest=Xtest/255
	print("[INFO] shape of training data:",Xtrain.shape,"\n[INFO] shape of testing data:",Xtest.shape)

#-------------------------------data loaded---------------------------------------------
	cv2.imshow("random Image",Xtrain[56])
	print("image is of class:",ytrain[56])
	cv2.waitKey(0)
	cv2.destroyAllWindows()
#--------------------------------making o/p categorical---------------------------------
	ytrain=np_utils.to_categorical(ytrain,no_classes)
	ytest=np_utils.to_categorical(ytest,no_classes)
#------------------------------------data augmentation------------------------------------
	datagen = image.ImageDataGenerator(featurewise_center=True,featurewise_std_normalization=True,rotation_range=20,width_shift_range=0.2,height_shift_range=0.2,horizontal_flip=True)
	datagen.fit(Xtrain)

#-------------------------------deep learning model-------------------------------------
	model=VGG16(weights="imagenet",include_top=False,input_shape=(224,224,3))

	x= model.output
	x= Flatten()(x)
	x= Dense(512,activation='relu')(x)
	x= Dense(215,activation='relu')(x)
	pred=Dense(no_classes,activation="softmax")(x)

#creating the final model
	model=Model(inputs=model.input,outputs=pred)
# setting no. of untrained layers in our final model
	for layer in model.layers[:-3]:
		layer.trainable = False
#-----------------------------------COMPILING THE MODEL-----------------------------------    
	model.compile(loss="categorical_crossentropy",optimizer="Adadelta",metrics=['accuracy'])
#-----------------------------------FITTING THE MODEL-------------------------------------
	lit_data=datagen.flow(Xtrain, ytrain, batch_size=1)
	model.fit_generator(lit_data,steps_per_epoch=len(X)/12,epochs=epochs,verbose=1,validation_data=(Xtest,ytest))

#-----------------------------------SAVING MODEL------------------------------------------------
	print("[INFO] Model Saved at Location:C:\\Users\\hseth\\Desktop\\HCL_project_1\\ as model_object_detect.h5")
	model.save("C:\\Users\\hseth\\Desktop\\HCL_project_1\\model_object_detect.h5")
