import tkinter as tk
from tkinter import filedialog

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    return filename

root = tk.Tk()
button = tk.Button(root, text='Open', command=UploadAction)
button.pack()
filename=UploadAction()
