import numpy as np 
from keras_vggface.vggface import VGGFace
from keras.preprocessing import image
from keras_vggface import utils
from keras.models import load_model
from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt
from PIL import Image
from warnings import simplefilter
def predict_face(img):
    simplefilter(action="ignore",category=Warning)
    # getting image from the directory
    target_size=(224, 224)
    model = load_model('model_save_face.h5')
    img=plt.imread(img)
    # detecting face from the image we have uploded for image recogniztion prediction
    detector=MTCNN()
    result_image=detector.detect_faces(img)
    x1,y1,width,height=result_image[0]['box']
    x2,y2=x1+width,y1+height
    face_roi=img[y1:y2,x1:x2]
    image_face = Image.fromarray(face_roi)
    image_face = image_face.resize(target_size)

    x = image.img_to_array(image_face)
    x = np.expand_dims(x, axis=0)
    x = utils.preprocess_input(x, version=2) 
    # predicting the o/p from the model we have created previously
    preds = model.predict(x)
    out_lab = np.argmax(preds[0])
    #getting name from the predicted number 
    name2label = {'hardik':0,'himanshu':1,'mike':2,'anmol':3,'swati':4,'atul':5}
    label2name = {0:'hardik',1:'himanshu',2:'mike',3:'anmol',4:'swati',5:'atul'}

    print ("\n\n\n\t\t PERSON IN THE IMAGE IS  : ",label2name[out_lab])