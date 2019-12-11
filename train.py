import numpy as np 
from sklearn.model_selection import train_test_split
from keras_vggface.vggface import VGGFace
from keras.engine import  Model
from keras.layers import Input
import numpy as np
import keras  
from keras.layers import Dense
def train():
    # extracting file saved by data_prep.py
    data = np.load('face_data.npz')
    x , y  =  data['x'], data['y']
    #categorical conversion of data label
    y = keras.utils.to_categorical(y, 6)
    # using transfer learning to reduce the time required to train the algo
    resnet = VGGFace(model='resnet50',input_shape=(224, 224, 3))
    
    layer_name = resnet.layers[-2].name
    #adding our own custom layers to make the model work on our datatset
    out = resnet.get_layer(layer_name).output
    out = Dense(6,activation='softmax')(out)
    resnet_4 = Model(resnet.input, out)
    # removing last layer of the model and adding my own layer to it 
    for layer in resnet_4.layers[:-1]:
        layer.trainable = False
        
        resnet_4.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
        #checking the final created dataset 
        print (resnet_4.summary())
        # training the model we have created with our own dataset
        resnet_4.fit(x, y,batch_size=10,epochs=10,shuffle=True)
        #saving the trained model so that it can be used afterwards
        resnet_4.save("C:\\Users\\hseth\\Desktop\\face recogination\\model_save_face.h5")
        # checking the accuracy of the model on training data only as i used a very small dataset
        scores = resnet_4.evaluate(x, y, verbose=1)
        print('Test accuracy:', scores[1])




