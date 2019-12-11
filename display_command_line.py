from qr_code import decode
from obj_det_scr_op import model_pred
from ocr import ocr_doc
from object_detection_scratch import model_train
from webcam import camera,image_get_object_detect,image_get_normal,image_preprocess
from train import train
from identify import predict_face
from data_prep import data_prep
from lag_using_google import translate
from warnings import simplefilter
simplefilter(action="ignore",category=Warning)
back="yes"
while back == "yes":
    print("ENTER 1:OBJECT DETECTION\nENTER 2:OPTICAL CHARACTER RECOGINITION(currently not working)\nENTER 3:QR AND BARCODE DECODER\nENTER 4:LANGUAGE TRANSLATION\nENTER 5:FACE RECOGNITION\nENTER 6:TRAIN THE OBJECT DETECTION MODEL\nENTER 7:TRAIN FACE RECOGNITION MODEL\nENTER 8:TO EXIT")
    choice=input("\n\nEnter Your Choice:")
    if choice =="1" :
        print("The Model can predict following objects :\n1.Dog\n2.Cat\n3.Watch\n4.Pen\n5.Mug\n6.Headphones\n7.Book\n8.Bottle\n9.Telephone\n")
        print("ENTER 1:TO USE IMAGE LOCATION\nENTER 2:USE WEBCAM TO TAKE PICTURE")
        choice_obj=input("\n\nEnter Your Choice:")
#        system("clear")
        if choice_obj == "1":
            image=image_get_object_detect()
            pre_image=image_preprocess(image)
            prediction_class=model_pred(pre_image)
            print("\n\nAccording to Model Object in Image is :",prediction_class)
            back=input("\n\n would you like to go back(yes/no):")
            if back=="no":
                print("EXITING")

        elif choice_obj == "2":
            image=camera()
            pre_image=image_preprocess(image)
            prediction_class=model_pred(pre_image)
            print("\n\nAccording to Model Object in Image is :",prediction_class)
            back=input("\n\n would you like to go back(yes/no):")
            if back=="no":
                print("EXITING")


        else :
            print("Wrong input........")
            back=input("\n\n would you like to go back(yes/no):")
            if back=="no":
                print("EXITING")

    elif choice == "2":
        image=image_get_normal(0)
        text=ocr_doc(image)
#        system("clear")
        print("The Text in the Picture is :\n",text)
        print("---------------------------------------------------------------------------------------------------------------------------------")
        print("\n\nENTER 1:TO SAVE THE DOCUMENT IN TEXT FILE\nENTER ANY OTHER KEY TO EXIT WITHOUT SAVING")
        ch=input("\n\nENTER YOUR CHOICE:")
#        system("clear")
        if ch == "1":
            file_up_name=input("Enter Name of file you want to save data as:")
            file_up="/home/hardik/Desktop/"+file_up_name+".txt"
            print("File Stored at Location:",file_up)
            file_des=open(file_up,"w",encoding="utf-8")
            file_des.write(text)
            file_des.close()
            back=input("\n\n would you like to go back(yes/no):")
            if back=="no":
                print("EXITING")

        else: 
            back=input("\n\n would you like to go back(yes/no):")
            if back=="no":
                print("EXITING")

    elif choice == "3":
        image=image_get_normal(5)
        decode(image)
        back=input("\n\n would you like to go back(yes/no):")
        if back=="no":
            print("EXITING")

    elif choice == "4":
        translate()
        back=input("\n\n would you like to go back(yes/no):")
        if back=="no":
            print("EXITING")

    elif choice == "5":
        image=image_get_normal(1)
        predict_face(image)
        back=input("\n\n would you like to go back(yes/no):")
        if back=="no":
            print("EXITING")
       
    elif choice == "6":
        model_train()
    elif choice == "7":
        data_prep()
        train()
        print("RUN AGAIN TO USE YOUR TRAINED MODEL..........")
    elif choice == "8":
        print("EXITING.....")
        back="no"
    else:
        print("WRONG INPUT!!!!")
        back=input("\n\n would you like to go back(yes/no):")
        if back=="no":
            print("EXITING")

