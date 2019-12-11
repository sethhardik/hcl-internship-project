import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input
import cv2
import tkinter as tk
from tkinter import filedialog

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    return filename

def pick_file():
    root = tk.Tk()
    button = tk.Button(root, text='Open', command=UploadAction)
    button.pack()
    filename=UploadAction()
    root.mainloop()
    return filename
def camera():
    camera = cv2.VideoCapture(0)
    print("enter *s* to save the image ")
    while True:
        return_value,image = camera.read()
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imshow('image',gray)
        if cv2.waitKey(1)& 0xFF == ord('s'):
            cv2.imwrite("C:\\Users\\hseth\\Desktop\\HCL_project_1\\test.jpg",image)
            break
    camera.release()
    cv2.destroyAllWindows()
    img=image_get_normal(2)
    return img
def image_get_object_detect():
    print("Select the file:")
    input_image_dir=pick_file()
    image = load_img(input_image_dir, target_size=(224, 224))
    return image
def image_preprocess(image):
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

    image = preprocess_input(image)
    return image
def image_get_normal(value):
    if value is 2:
        input_image_dir="C:\\Users\\hseth\\Desktop\\HCL_project_1\\test.jpg"
        image = load_img(input_image_dir, target_size=(224, 224))
    elif value is 0:
        print("Select the file:")
        input_image_dir=pick_file()
        image=cv2.imread(input_image_dir,0)
    elif value is 1:
        print("Select the file:")
        image=pick_file()
    else:
        print("Select the file:")
        input_image_dir=pick_file()
        image = cv2.imread(input_image_dir)
        
    return image