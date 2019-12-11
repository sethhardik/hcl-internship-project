import tkinter as tk
from tkinter import filedialog
from googletrans import Translator
from os import system 
from webcam import UploadAction,pick_file

def translate():
	translator = Translator()
	print("ENTER 1:TO ENTER TEXT YOU WANT OT TRANSLATE\nENTER 2:TO UPLOAD TEXT FILE YOU WANT TO TRANSLATE")
	char=int(input("\nEnter your Choice:"))
	if char is 1:
		text=input("Type Text you want to Translate:")
		trans=translator.translate(text)
		print("\n\nLanguage you Entered Text is--------->",trans.src,"\n\nTranslation of above Text in English is:\n",trans.text)
	elif char is 2:
		system("clear")
		filename=pick_file()
		file_up_name=input("Enter Name of file you want to save data as:")
		with open(filename,"r",encoding="utf-8") as file:
			text=file.read()
			trans=translator.translate(text)
			print("\n\nLanguage you Entered Text is--------->",trans.src)
		file_up="C:\\Users\\hseth\\Desktop\\"+file_up_name+".txt"
		print(file_up)
		file_des=open(file_up,"w",encoding="utf-8")
		file_des.write(trans.text)
		file_des.close()