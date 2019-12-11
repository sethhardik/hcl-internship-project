import numpy as np
from keras.preprocessing import image
from keras_vggface.vggface import VGGFace
from keras_vggface import utils
import glob 
from sklearn.utils import shuffle
import numpy as np 
from PIL import Image

from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt

def data_prep():
    images  = []
    labels  = []
    target_size=(224, 224)

    name2label = {'hardik':0,'himanshu':1,'mike':2,'anmol':3,'swati':4,'atul':5}
    labe2name = {0:'hardik',1:'himanshu',2:'mike',3:'anmol',4:'swati',5:'atul'}

    for sub_folder in glob.glob('data_face\\*') :
        name = sub_folder.split('\\')[-1]
        for file in glob.glob(sub_folder + '\\*'):
            img=plt.imread(file)
            # detectiong face from the the train dataset we have and creating our own dataset only of faces 
            detector=MTCNN()
            result_image=detector.detect_faces(img)
            x1,y1,width,height=result_image[0]['box']
            x2,y2=x1+width,y1+height
            face_roi=img[y1:y2,x1:x2]
            image_face = Image.fromarray(face_roi)
            image_face = image_face.resize(target_size)
		#image_face = np.asarray(image_face)
            x = image.img_to_array(image_face)
            images.append(x)
            labels.append(name2label[name])
            print (x.shape , name2label[name])

		
        images = np.array(images)
        labels = np.array(labels)
        # applying neccesary image_pre-processing on the images we have 
        x = utils.preprocess_input(images, version=2) 
        print (images.shape)
        print (labels.shape)

    images , labels = shuffle(images , labels)
    #saving the faces and the labels in the face_data file so that we can use it on our trained model
    np.savez('face_data', x=images, y=labels)





