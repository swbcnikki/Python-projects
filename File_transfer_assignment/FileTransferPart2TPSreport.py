
import shutil
import os
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import *

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        

        #tkinter page parameters and name
        self.master = master
        self.master.minsize(1000,500)
        self.master.maxsize(1000,500)
        self.master.title('File Transfer of TPS Reports')
        self.master.config(bg='#005C5C')
        
        #set the variables to string
        self.varSource = StringVar()
        self.varDestination = StringVar()



        #label for the source file
        self.lblSource = Label(self.master, text='Source', font=('Times New Roman', 12), fg='white', bg='#0C2C56')
        self.lblSource.grid(row=0, column=0,padx=(30,0), pady=(30,0))
        #label for the destination file
        self.lblDestination = Label(self.master, text='Destination', font=('Times New Roman', 12), fg='white', bg='#0C2C56')
        self.lblDestination.grid(row=1, column=0,padx=(30,0), pady=(30,0))

        #create the text box for source folder
        self.txtSource = Entry(self.master, text=self.varSource, font=('Times New Roman', 12), fg='black', bg='white')
        self.txtSource.grid(row=0,column=1,padx=(30,0), pady=(30,0))
        #create the text box for destination folder
        self.txtDestination = Entry(self.master, text=self.varDestination, font=('Times New Roman', 12), fg='black', bg='white')
        self.txtDestination.grid(row=1,column=1,sticky=tk.W,padx=(30,0), pady=(30,0))

        #create buttons
        self.btnBrowseS = Button(self.master, text='Browse', width=10,height=1,command=self.browseS)
        self.btnBrowseS.grid(row=0,column=4,padx=(0,0),pady=(30,0))

        self.btnBrowseD = Button(self.master, text='Browse', width=10,height=1,command=self.browseD)
        self.btnBrowseD.grid(row=1,column=4,padx=(0,0),pady=(30,0))

       

        self.btnMove = Button(self.master, text='Move files', width=10, height=1, command=self.move)
        self.btnMove.grid(row=2, column=1,padx=(0,0), pady=(30,0), sticky=NW)

        self.btnClose = Button(self.master, text='Close', width=10, height=1, command=self.close_window)
        self.btnClose.grid(row=2, column=3,padx=(0,0), pady=(30,0), sticky=NE)

    def selectiveCopy(source, destination): #selects the specific files you want
        x = datetime.datetime.now() #time right now
        y = x - datetime.timedelta(hours=24) #time 24hours ago
        for i in files: #move the files represented by i (i is the filename and extention)
            timeStamp = os.path.getmtime(source) #evaluate the timestamp

    #browse button action
    def browseS(self):
        #Peter has prepared the reports that go in a general folder with old and new files
        source = '/Users/Bibo/Documents/GitHub/Python-Projects/Python-projects_in_Github/File_transfer_assignment/PeterGibbonsSends/'

    def browseD(self):
        #Bill is expecting to receive the report
        destination = '/Users/Bibo/Documents/GitHub/Python-Projects/Python-projects_in_Github/File_transfer_assignment/BillLumberghreceives/'
        files = os.listdir(source)        


    #move files button
    def move(self):
        if timeStamp == y:
            shutil.move(source+i, destination) #move those particular files
 
    
    #close button
    def close_window(self):
        self.master.destroy() #close the tkinter



if __name__=='__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
