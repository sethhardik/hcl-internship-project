
from keras.models import load_model
from os import system
def model_pred(image):
	model = load_model("/home/hardik/Desktop/HCL_project_1/model_object_detect.h5")
	yhat = model.predict(image)
	system("clear")
	print("[info] predicted probabilities are:",yhat)
	for i in range(9):
		if yhat[0][i]>=0.5:
			yhat[0][i]=1
		elif yhat[0][i]<0.5:
			yhat[0][i]=0
	for i in range(9):
		if yhat[0][i]==1:
			loc=i
	if loc == 0:
		class_name="Telephone"
	elif loc == 1:
		class_name="Mug"
	elif loc == 2:
		class_name="Dog"
	elif loc == 3:
		class_name="Cat"
	elif loc == 4:
		class_name="Pen"
	elif loc == 5:
		class_name="Bottle"
	elif loc == 6:
		class_name="Watch"
	elif loc == 7:
		class_name="Headphone"
	elif loc == 8:
		class_name="Book"
	return class_name