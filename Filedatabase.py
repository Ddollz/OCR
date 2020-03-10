import os
from subprocess import call
import sys
from tkinter import *
from tinydb import TinyDB, Query
from tkinter import filedialog, Text,messagebox, ttk
class Databaseprocess:
    def __init__(self):
        def click_Main():
            DBgui.destroy()          
            call([ r"Main.exe"]) 

        def all_children (window) :
            _list = window.winfo_children()

            for item in _list :
                if item.winfo_children() :
                    _list.extend(item.winfo_children())

            return _list

        def export_file():
            try:
                Elementrow = self.Comboboxid.get()
                row = int(self.Comboboxid.get())
                row2 = int(self.Comboboxid.get())
            except: 
                messagebox.showinfo("Warning!!!", "Please Choose An ID.",icon = 'warning')
                return

            files = [('Text Document', '*.txt'), ('All Files', '*.*')] 
            filess = filedialog.asksaveasfilename(filetypes = files, defaultextension=files)
            if filess is None:  # ask saveasfile return `None` if dialog closed with "cancel".
                return
                
            print(row)
            
            for rows in table:
                eids = rows.eid
                tableinfo = table.get(eid=eids)
                tabletext = table2.get(eid=eids)
                if row == rows.eid:
                    res = 'Element ID: '+str(rows.eid)+" \n"+ " ".join(("{}: {} ".format(k, v) for k, v in tableinfo.items()))+" "
                    res2 = "".join(("{}: \n{} ".format(k, v) for k, v in tabletext.items()))+" "
            for rows in table2:
                if row2 == rows.eid:
                    print(res2)
            if filess:
                with open(filess, 'w', encoding='utf-8') as filess:
                    filess.write(res)
                    filess.write('\n')
                    filess.write(res2)
                    
                    print ("Export Succeeded")
                    messagebox.showinfo("Export Complete.", "Export Successfully!",icon = 'info')


        def open_file():
            try:
                Elementrow = self.Comboboxid.get()
                row = int(self.Comboboxid.get())
            except: 
                messagebox.showinfo("Warning!!!", "Please Choose An ID.",icon = 'warning')
                return
            
            temp = open("temp.txt","w", encoding='utf-8')
            for rows in table2:
                eids = rows.eid
                mydict2 = table2.get(eid=eids)
                if row == rows.eid:
                    ress = mydict2.get('Text')
            
            print('Processing')
            temp.write(ress)
            temp.close()
            DBgui.destroy()
            call(["python", "Process.py"])
                    

        def delete_row():
            try:
                row = int(self.Comboboxid.get())
                MsgBox = messagebox.askquestion ('Remove','Are you sure you want to remove ID: '+str(row),icon = 'warning')
                if MsgBox == 'yes':
                    for rows in table:
                        if row == rows.eid:
                            table.remove(eids=[row])
                            table2.remove(eids=[row])
            except: 
                messagebox.showinfo("Warning!!!", "Please Choose An ID.",icon = 'warning')
            rowid=[]
            for rows in table:
                rowid.append(rows.eid)
            #removing all widgets in frame1 
            widget_list = all_children(self.Frame1)
            for item in widget_list:
                item.pack_forget()
            #Adding back all widgets in frame1
            for rows in table:
                eids = rows.eid
                mydict = table.get(eid=eids)
                res = 'Element ID: '+str(rows.eid)+" \n"+ " ".join(("{}: {} ".format(k, v) for k, v in mydict.items()))+" "
                self.infos = Label(self.Frame1, text = res)
                self.infos.configure(background="white",foreground="black")
                self.infos.pack()
            self.Comboboxid.set('Please Choose An ID')
            self.Comboboxid.configure(values = rowid)
            
            

        def center_window(w=300, h=200):
            # get screen width and height
            ws = DBgui.winfo_screenwidth()
            hs = DBgui.winfo_screenheight()
            # calculate position x, y
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            DBgui.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
        helv = "Helvetica", 18,"bold"
        titlefont = "Helvetica", 22,"bold"
        subfont = "Helvetica", 12,"bold"

        DBgui = Tk()
        center_window(800, 650) 
        DBgui.title("Optical Character Recognition")
        DBgui.configure(background="#121212")
        DBgui.configure(highlightbackground="#d9d9d9")
        DBgui.configure(highlightcolor="black", borderwidth= 10, relief=RIDGE)
        DBgui.resizable(FALSE,FALSE)

        self.Frame1 = Frame(DBgui)
        self.Frame1.place(relx=0.02, rely=0.13, height=500, width=500)
        self.Frame1.configure(relief=RIDGE,borderwidth="2",background="white",highlightbackground="#d9d9d9",highlightcolor="black")
        DB = TinyDB('Database.json')
        table = DB.table('Files')
        table2 = DB.table('Text')
        User = Query()

        for rows in table:
            eids = rows.eid
            mydict = table.get(eid=eids)
            res = 'Element ID: '+str(rows.eid)+" \n"+ " ".join(("{}: {} ".format(k, v) for k, v in mydict.items()))+" "
            self.infos = Label(self.Frame1, text = res)
            self.infos.configure(background="white",foreground="black")
            self.infos.pack()
        
        
        self.Title = Label(DBgui)
        self.Title.place(relx=0.15, rely=0.07, height=30, width=300)
        self.Title.configure(background="#121212",foreground="white", text="File Database", font=titlefont)

        self.label1 = Label(DBgui)
        self.label1.place(relx=0.73, rely=0.17, height=15, width=100)
        self.label1.configure(background="#121212",foreground="white", text="Element ID", font=subfont)

        self.Comboboxid = ttk.Combobox(DBgui, values=[1])         
        self.Comboboxid.place(relx=0.74, rely=0.2, height=30, width=150)
        self.Comboboxid.set('Please Choose an Element ID')

        #Combobox
        rowid=[]
        for rows in table:
            rowid.append(rows.eid)
        self.Comboboxid.configure(values = rowid)


        self.Button1 = Button(DBgui)
        self.Button1.place(relx=0.74, rely=0.26, height=50, width=150)
        self.Button1.configure(relief=RIDGE,activebackground="#d9d9d9",font=helv,background="#3d3d3d",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black")
        self.Button1.configure(text='''Export File''')
        self.Button1.configure(command = export_file)

        self.Button2 = Button(DBgui)
        self.Button2.place(relx=0.74, rely=0.38, height=50, width=150)
        self.Button2.configure(relief=RIDGE,activebackground="#d9d9d9",font=helv,background="#3d3d3d",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black")
        self.Button2.configure(text='''Translator''')
        self.Button2.configure(command = open_file)

        self.Button3 = Button(DBgui)
        self.Button3.place(relx=0.74, rely=0.50, height=50, width=150)
        self.Button3.configure(relief=RIDGE,activebackground="#d9d9d9",font=helv,background="#3d3d3d",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black")
        self.Button3.configure(text='''Delete''', command = delete_row)


        self.Button4 = Button(DBgui)
        self.Button4.place(relx=0.74, rely=0.62, height=50, width=150)
        self.Button4.configure(relief=RIDGE,activebackground="#d9d9d9",font=helv,background="#3d3d3d",foreground="#ffffff",highlightbackground="#d9d9d9",highlightcolor="black")
        self.Button4.configure(text='''Back''', command = click_Main)




        DBgui.mainloop()

if __name__ == '__main__':
    Database=Databaseprocess()