import tkinter as tk
from tkinter import filedialog 
from tkinter import ttk
import ttkthemes            #3rd party library, install : pip install ttkthemes
import pyqrcode                         #3rd party library, install : pip install pyrcode
import os
from tkinter import messagebox

class Qr_code_generator:

    def create_qr(self,text):
        #creating Qr code 
        qr = pyqrcode.create(text)

        #asking user for file name and directory
        file = filedialog.asksaveasfile(mode = 'wb',defaultextension = ".png",filetypes = (("Portable Network Graphics","*.png"), ("All Files","*.*")))
        if file:
            qr.png(file, scale=8)
            messagebox.showinfo("Succesfully Saved!","File has been Saved")
        return
    #method to create GUI window    
    def create_window(self,width,height):
        root = ttkthemes.ThemedTk(theme = "plastik") #creating window and setting theme for it
        root.title("Qr Code Generator")             #window title
        root.geometry(f"{width}x{height}")      #window dimension
        
        fr = tk.Frame(root)                 #frame inside GUI window
        
        fr.pack()
        #variable to store Entry Box Content
        text = tk.StringVar()
        input = ttk.Entry(fr,textvariable = text,width = 30)      #Entry Box
        input.grid(row = 1,column = 0,pady = 30,ipady = 6)  
        
        #Generate Button
        create_button = ttk.Button(fr,text = "Create",command = lambda :  self.create_qr(text.get()))
        create_button.grid(row = 2,column = 0,ipady = 5,ipadx = 5)
        root.mainloop()
        

qr_code = Qr_code_generator()           #object of Qr_code_generator class
qr_code.create_window(400,400)          #method calling