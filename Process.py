import os
from subprocess import call
import sys
from tkinter import *
from datetime import date
from tinydb import TinyDB, Query
from tkinter import ttk,filedialog, Text, messagebox
from googletrans import Translator

class TranslateGui:
    def __init__(self):
        def click_Subgui():
            Subgui.destroy()        
            call(["python", "Conversion.py"])
        
        def click_Save():
            #table.insert({'Date' : '22/02/2020','Extension File' : '.jpg', 'Translated' : 'Yes', 'Source' : 'Chineese','Destination' : 'English'})
            today = str(date.today())
            ftitle = self.entry1.get()
            res = len(ftitle.split()) 
            if int(res) > 5:
                messagebox.showinfo("Instructions!", "Filename must not have more than 5 words")
                return
            if int(res) <= 0:
                messagebox.showinfo("Warning!", "Filename must be added", icon = 'warning')
                return
            if self.bools == 0:
                translator = Translator()
                langs = translator.detect(self.Text1.get(1.0,END))
                Languagecode = langs.lang
                table.insert({'Date' : today,'Title': ftitle,'Translated' : 'No', 'Language Code' : Languagecode})
                table2.insert({'Text' : self.Text1.get(1.0,END)})
            else:
                table.insert({'Date' : today,'Title': ftitle, 'Translated' : 'Yes', 'Source' : self.abbr,'Destination' : self.destabbr})
                table2.insert({'Text' : self.Text1.get(1.0,END)})
            messagebox.showinfo("Save Completed", "The data successfully added to Database")

        def translate(text):
            self.bools = TRUE
            translator = Translator()
            Sourcelanguage = self.Sourcelang.get()
            Destinationlanguages = self.Destinationlang.get()
            beingtranslated = self.Text1.get(1.0,END)
            #Dest
            if Destinationlanguages == 'Afrikaans':
                self.destabbr='af'
            if Destinationlanguages == 'Arabic':
                self.destabbr='ar'
            if Destinationlanguages == 'Azerbaijani':
                self.destabbr='az'
            if Destinationlanguages == 'Belarusian':
                self.destabbr='be'
            if Destinationlanguages == 'Bengali':
                self.destabbr='bn'
            if Destinationlanguages == 'Catalan':
                self.destabbr='ca'
            if Destinationlanguages == 'Czech':
                self.destabbr='cs'
            if Destinationlanguages == 'Chinese simplified':
                self.destabbr='zh-CN'
            if Destinationlanguages == 'Chinese traditional':
                self.destabbr='zh-TW'
            if Destinationlanguages == 'Welsh':
                self.destabbr='cy'
            if Destinationlanguages == 'Danish':
                self.destabbr='da'
            if Destinationlanguages == 'German':
                self.destabbr='de'
            if Destinationlanguages == 'Greek':
                self.destabbr='el'
            if Destinationlanguages == 'English':
                self.destabbr='en'
            if Destinationlanguages == 'Esperanto':
                self.destabbr='eo'
            if Destinationlanguages == 'Persian':
                self.destabbr='fa'
            if Destinationlanguages == 'Finnish':
                self.destabbr='fi'
            if Destinationlanguages == 'Hebrew':
                self.destabbr='iw'
            if Destinationlanguages == 'Japanese':
                self.destabbr='ja'
            if Destinationlanguages == 'Kurdish':
                self.destabbr='kur'
            if Destinationlanguages == 'Russian':
                self.destabbr='ru'
            if Destinationlanguages == 'Serbian':
                self.destabbr='sr'
            if Destinationlanguages == 'Swedish':
                self.destabbr='sv'
            if Destinationlanguages == 'Tagalog':
                self.destabbr='tl'
            if Destinationlanguages == 'Korean':
                self.destabbr='ko'
            if Destinationlanguages == 'Hindi':
                self.destabbr='hi'
            if Destinationlanguages == 'French':
                self.destabbr='fr'
            if Destinationlanguages == 'Bulgarian':
                self.destabbr='bg'
            #Source 
            if Sourcelanguage == 'Detect Language':
                langs = translator.detect(beingtranslated)
                self.abbr = langs.lang
            if Sourcelanguage == 'Afrikaans':
                self.abbr='af'
            if Sourcelanguage == 'Arabic':
                self.abbr='ar'
            if Sourcelanguage == 'Azerbaijani':
                self.abbr='az'
            if Sourcelanguage == 'Belarusian':
                self.abbr='be'
            if Sourcelanguage == 'Bengali':
                self.abbr='bn'
            if Sourcelanguage == 'Catalan':
                self.abbr='ca'
            if Sourcelanguage == 'Czech':
                self.abbr='cs'
            if Sourcelanguage == 'Chinese simplified':
                self.abbr='zh-CN'
            if Sourcelanguage == 'Chinese traditional':
                self.abbr='zh-TW'
            if Sourcelanguage == 'Welsh':
                self.abbr='cy'
            if Sourcelanguage == 'Danish':
                self.abbr='da'
            if Sourcelanguage == 'German':
                self.abbr='de'
            if Sourcelanguage == 'Greek':
                self.abbr='el'
            if Sourcelanguage == 'English':
                self.abbr='en'
            if Sourcelanguage == 'Esperanto':
                self.abbr='eo'
            if Sourcelanguage == 'Persian':
                self.abbr='fa'
            if Sourcelanguage == 'Finnish':
                self.abbr='fi'
            if Sourcelanguage == 'Hebrew':
                self.abbr='iw'
            if Sourcelanguage == 'Japanese':
                self.abbr='ja'
            if Sourcelanguage == 'Kurdish':
                self.abbr='kur'
            if Sourcelanguage == 'Russian':
                self.abbr='ru'
            if Sourcelanguage == 'Serbian':
                self.abbr='sr'
            if Sourcelanguage == 'Swedish':
                self.abbr='sv'
            if Sourcelanguage == 'Tagalog':
                self.abbr='tl'
            if Sourcelanguage == 'Korean':
                self.abbr='ko'
            if Sourcelanguage == 'Hindi':
                self.abbr='Hi'
            if Sourcelanguage == 'French':
                self.abbr='fr'
            if Sourcelanguage == 'Bulgarian':
                self.abbr='bg'
            translated = translator.translate(beingtranslated,dest=self.destabbr,src=self.abbr)
            self.Text1.delete(1.0,END)
            self.Text1.insert(INSERT,translated.text)
            messagebox.showinfo("Translate Completed", "Text has been translated")

        def center_window(w=300, h=200):
            # get screen width and height
            ws = Subgui.winfo_screenwidth()
            hs = Subgui.winfo_screenheight()
            # calculate position x, y
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            Subgui.geometry('%dx%d+%d+%d' % (w, h, x, y))

        def export_file():
            files = [('Text Document', '*.txt'),('All Files', '*.*')] 
            filess = filedialog.asksaveasfilename(filetypes = files, defaultextension=files)
            if filess is None:  # ask saveasfile return `None` if dialog closed with "cancel".
                return
            string = self.Text1.get(1.0,END)
            print ("Export Succeeded")
            if filess:
                with open(filess, 'w', encoding='utf-8') as filess:
                    filess.write(string)
            

        Subgui = Tk()
        helv = "Helvetica", 18,"bold"
        titlefont = "Helvetica", 18,"bold"
        realtitlefont = "Helvetica", 22,"bold"
        subtitlefont = "Helvetica", 18
        subfont = "Helvetica", 12,"bold"
        textf = "Courier New",10,"bold"
        self.bools = FALSE
        self.destabbr=''
        self.abbr=''
        center_window(800, 800) 

        #Table Configuration
        DB = TinyDB('Database.json')
        table = DB.table('Files')
        table2 = DB.table('Text')
        User = Query()
        
        #Window configuration
        Subgui.title("Optical Character Recognition")
        Subgui.configure(background="#121212")
        Subgui.configure(highlightbackground="#d9d9d9")
        Subgui.configure(highlightcolor="black", borderwidth= 10, relief=RIDGE)
        Subgui.resizable(FALSE,FALSE)
        #Subgui.overrideredirect(TRUE)
        
        fopen = open("temp.txt", "r", encoding= "utf-8")
        text = fopen.read()
        self.Frame1 = Frame(Subgui)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=RIDGE,borderwidth="2",background="#3d3d3d",highlightbackground="#d9d9d9",highlightcolor="black")


        
        self.title = Label(self.Frame1)
        self.title.place(relx=0.32, rely=0.05, height=50, width=250)
        self.title.configure(background="#3d3d3d",foreground="white", text='Text Conversion', font=realtitlefont)

        self.entry1 = Entry(self.Frame1)
        self.entry1.place(relx=0.15, rely=0.2, height=20, width=500)

        self.label1 = Label(self.Frame1)
        self.label1.place(relx=0.15, rely=0.13, height=50, width=103)
        self.label1.configure(background="#3d3d3d",foreground="white", text='Filename', font=subtitlefont)

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.15, rely=0.25, height=300, width=500)
        self.Text1.configure(background="WHITE")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=764)
        self.Text1.insert(INSERT,text)
        self.Text1.configure(wrap=WORD)
        self.yscrollbar = Scrollbar(self.Text1,orient='vertical')
        self.yscrollbar.pack(side=RIGHT, fill=Y)
        self.Text1.configure(width=20, yscrollcommand=self.yscrollbar.set)
        self.yscrollbar.config(command=self.Text1.yview)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.20, rely=0.70, height=18, width=135)
        self.Label1.configure(background="#3d3d3d",foreground="white", text='Source Language', font=subfont)

        self.Sourcelang = ttk.Combobox(self.Frame1, values=[
            "Afrikaans","Arabic",'Azerbaijani',"Belarusian","Bengali",
            "Bulgarian","Catalan","Czech","Chinese simplified","Chinese traditional","Welsh","Danish","German",
            "Greek","English","Esperanto","Persian","Finnish","French","Hebrew","Hindi","Japanese" ,"Korean",
            "Russian","Serbian","Swedish","Tagalog"
            ])         
        self.Sourcelang.place(relx=0.192, rely=0.73, height=30, width=150)
        self.Sourcelang.set('Detect Language')

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.54, rely=0.70, height=18, width=169)
        self.Label2.configure(background="#3d3d3d",foreground="white", text='Destination Language', font=subfont)

        self.Destinationlang = ttk.Combobox(self.Frame1, values=[
            "Afrikaans","Arabic",'Azerbaijani',"Belarusian","Bengali",
            "Bulgarian","Catalan","Czech","Chinese simplified","Chinese traditional","Welsh","Danish","German",
            "Greek","English","Esperanto","Persian","Finnish","French","Hebrew","Hindi","Japanese","Korean",
            "Russian","Serbian","Swedish","Tagalog"
            ])         
        self.Destinationlang.place(relx=0.55, rely=0.73, height=30, width=150)
        self.Destinationlang.set('English')


        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.09, rely=0.85, height=50, width=150)
        self.Button1.configure(relief=RIDGE,activebackground="#d9d9d9",font=helv,background="#121212",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black")
        self.Button1.configure(command = click_Subgui)
        self.Button1.configure(text='''Back''')

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.30, rely=0.85, height=50, width=150)
        self.Button2.configure(relief=RIDGE,activebackground="#d9d9d9",font=helv,background="#121212",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black")
        self.Button2.configure(command = click_Save)
        self.Button2.configure(text='''Save''')

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.509, rely=0.85, height=50, width=150)
        self.Button3.configure(relief=RIDGE,activebackground="#d9d9d9",font=helv,background="#121212",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black", text='''Translate''',command = lambda : translate(text))
        
        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.719, rely=0.85, height=50, width=150)
        self.Button4.configure(relief=RIDGE,activebackground="#d9d9d9",font=helv,background="#121212",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black")
        self.Button4.configure(command = lambda : export_file())
        self.Button4.configure(text='''Export File''')
        
        

        
        
        Subgui.mainloop()

if __name__ == '__main__':
    print("Completed")
    Translate=TranslateGui()