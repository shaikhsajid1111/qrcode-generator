import tkinter as tk
from tkinter import filedialog 
from tkinter import ttk
import ttkthemes            #3rd party library, install : pip install ttkthemes
import pyqrcode                         #3rd party library, install : pip install pyrcode
from tkinter import messagebox
from PIL import Image 

class Qr_code_generator:

    def open_file_path(self,file_path):
        
        image_path = file_path.name
        Image.open(image_path).show()

    def popup(self,text,file_path):
        popup_window = tk.Toplevel()
        popup_window.title("Generated Successfully!")
        popup_window.geometry("200x100")
        popup_window.resizable(False, False)
        text = ttk.Label(popup_window,text = "File has been saved!")
        open_button = ttk.Button(popup_window,text = "Open",command = lambda :  self.open_file_path(file_path))
        ok_button = ttk.Button(popup_window,text = "Ok",command = lambda:  popup_window.destroy())
        text.grid(row = 3,column = 3,pady = 4)
        open_button.grid(row = 4,column = 3,padx = 4)
        ok_button.grid(row = 4,column = 4,padx = 4)
    def create_qr(self,text):
        #creating Qr code 
        qr = pyqrcode.create(text)

        #asking user for file name and directory
        file = filedialog.asksaveasfile(mode = 'wb',defaultextension = ".png",filetypes = (("Portable Network Graphics","*.png"), ("All Files","*.*")))
        
        if file:
            qr.png(file, scale=8)
            file.close()
            #messagebox.showinfo("Succesfully Saved!","File has been Saved")
            self.popup("Saved Successfully!",file)
            
        return
    #method to create GUI window    
    def create_window(self,width,height):
        root = ttkthemes.ThemedTk(theme = "breeze") #creating window and setting theme for it
        root.title("Qr Code Generator")             #window title
        root.geometry(f"{width}x{height}")      #window dimension
        root.resizable(False, False)
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
