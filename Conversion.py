import os
from subprocess import call
import subprocess
import sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, Text,messagebox
import time
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'

class ConversionGui:
    def __init__(self):
        def click_Main():
            Gui1.destroy()  
            call([ r"Main.exe"])  
        def click_capture():  
            call(["python", "webcam.py"])  
        def center_window(w=300, h=200):
            # get screen width and height
            ws = Gui1.winfo_screenwidth()
            hs = Gui1.winfo_screenheight()
            # calculate position x, y
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            Gui1.geometry('%dx%d+%d+%d' % (w, h, x, y))

        def get_file():
            filename=filedialog.askopenfilename(initialdir="/Retry number2/",title="Select File",
            filetypes=(("jpeg files","*.jpg"),("PNG Files", "*.png"),("all files", "*.*")))
            language=self.comboExample.get()
            
            if language == 'Afrikaans':
                abbr='afr'
            if language == 'Amharic':
                abbr='amh'
            if language == 'Arabic':
                abbr='ara'
            if language == 'Assamese':
                abbr='asm'
            if language == 'Azerbaijani':
                abbr='aze'
            if language == 'Cyrilic':
                abbr='aze_cyrl'
            if language == 'Belarusian':
                abbr='bel'
            if language == 'Bengali':
                abbr='ben'
            if language == 'Tibetan':
                abbr='tib'
            if language == 'Bosnian':
                abbr='bos'
            if language == 'Breton':
                abbr='bre'
            if language == 'Catalan':
                abbr='cat'
            if language == 'Cebuano':
                abbr='ceb'
            if language == 'Czech':
                abbr='ces'
            if language == 'Chinese simplified':
                abbr='chi_sim'
            if language == 'Chinese traditional':
                abbr='chi_tra'
            if language == 'Cherokee':
                abbr='chr'
            if language == 'Welsh':
                abbr='cym '
            if language == 'Danish':
                abbr='dan'
            if language == 'German':
                abbr='deu'
            if language == 'Dzongkha':
                abbr='dzo'
            if language == 'Greek':
                abbr='ell'
            if language == 'English':
                abbr='eng'
            if language == 'Esperanto':
                abbr='epo'
            if language == 'Persian':
                abbr='fas'
            if language == 'Finnish':
                abbr='fas'
            if language == 'Hebrew':
                abbr='fin'
            if language == 'Japanese':
                abbr='jpn'
            if language == 'Kurdish':
                abbr='kur'
            if language == 'Russian':
                abbr='rus'
            if language == 'Serbian':
                abbr='srp'
            if language == 'Swedish':
                abbr='swe'
            if language == 'Tagalog':
                abbr='tgl'
            if language == 'French':
                abbr='fra'
            if language == 'Hindi':
                abbr='hin'
            if language == 'Bulgarian':
                abbr='bre'
            if language == 'Korean':
                abbr='kor'
            #ocrstring = pytesseract.image_to_string(Image.open(filename), lang= abbr)
            try:
                # print("Processing")
                ocrstring = pytesseract.image_to_string(Image.open(filename), lang= abbr)
                '''
                try:
                    temp = open("temp.txt", "w")
                    temp.write(ocrstring)
                    temp.close()
                except:'''
                temp = open("temp.txt","w", encoding='utf-8')
                temp.write(ocrstring)
                temp.close()
                Gui1.destroy()
                call(["python", "Process.py"])
            except:
                
                messagebox.showinfo("Warning!", "Processing Failed (Wrong file/datatype)")

        Gui1 = Tk()
        helv = "Helvetica", 18,"bold"
        titlefont = "Helvetica", 22,"bold"
        center_window(400, 600) 
        Gui1.title("Optical Character Recognition")
        Gui1.configure(background="#121212")
        Gui1.configure(highlightbackground="#d9d9d9")
        Gui1.configure(highlightcolor="black", borderwidth= 10, relief=RIDGE)
        Gui1.resizable(FALSE,FALSE)
        #Gui1.overrideredirect(TRUE)

        self.Frame1 = Frame(Gui1)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=RIDGE,borderwidth="2",background="#3d3d3d",highlightbackground="#d9d9d9",highlightcolor="black")

        

        self.title = Label(self.Frame1)
        self.title.place(relx=0.08, rely=0.03, height=103, width=300)
        self.title.configure(background="#3d3d3d",foreground="white", text="Pick your choices", font=titlefont)

        self.comboExample = ttk.Combobox(self.Frame1, values=[
            "Afrikaans", "Amharic","Arabic","Assamese","Azerbaijani","Cyrilic","Belarusian","Bengali","Tibetan","Bosnian","Breton",
            "Bulgarian","Catalan","Cebuano","Czech","Chinese simplified","Chinese traditional","Cherokee","Welsh","Danish","German",
            "Dzongkha","Greek","English","Esperanto","Persian","Finnish","French","Hebrew","Hindi","Japanese","Kurdish Kurmanji","Korean",
            "Russian","Serbian","Swedish","Tagalog"
            ])         
        self.comboExample.place(relx=0.30, rely=0.18, height=30, width=150)
        self.comboExample.set('English')

        #print(self.comboExample.get())
        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.12, rely=0.26, height=103, width=266)
        self.Button1.configure(relief=RIDGE,activebackground="#d9d9d9",font=helv,background="#121212",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black")
        self.Button1.configure(text='''Select Image''')
        self.Button1.configure(command = get_file)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.12, rely=0.47, height=103, width=266)
        self.Button2.configure(relief=RIDGE,activebackground="#d9d9d9",font=helv,background="#121212",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black")
        self.Button2.configure(text='''Capture''')
        self.Button2.configure(command = click_capture)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.12, rely=0.68, height=103, width=266)
        self.Button3.configure(relief=RIDGE,activebackground="#d9d9d9",font=helv,background="#121212",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black")
        self.Button3.configure(command = click_Main)
        self.Button3.configure(text='''Back''')

        Gui1.mainloop()
if __name__ == '__main__':
    Gui=ConversionGui()