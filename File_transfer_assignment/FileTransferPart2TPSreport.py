
'''
The point of this assignment is to create a GUI to allow the user to browse and choose a folder to move
the files from, and populate the text box with said folder, browse and choose a folder to send the file
to, and populate the text box with said folder. Also, a button to click and move the files successfully
once the folders have been selected and a close button to close the screen
'''

import shutil
import os
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        

        #tkinter page parameters and name
        self.master = master
        self.master.minsize(700,250)
        self.master.maxsize(700,250)
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
        self.btnBrowseS = Button(self.master, text='Browse', width=10,height=1,fg='black',bg='#C4CED4',command=self.browseS)
        self.btnBrowseS.grid(row=0,column=4,padx=(0,0),pady=(30,0))

        self.btnBrowseD = Button(self.master, text='Browse', width=10,height=1,fg='black',bg='#C4CED4',command=self.browseD)
        self.btnBrowseD.grid(row=1,column=4,padx=(0,0),pady=(30,0))
      

        self.btnMove = Button(self.master, text='Move files', width=10, height=1,fg='black',bg='#FFCC00', command=self.selectiveMove)
        self.btnMove.grid(row=2, column=1,padx=(0,0), pady=(30,0), sticky=NW)

        self.btnClose = Button(self.master, text='Close', width=10, height=1,fg='white',bg='#D50032', command=self.close_window)
        self.btnClose.grid(row=2, column=3,padx=(0,0), pady=(30,0), sticky=NE)


        #Move button code - this tells it what to do
    def selectiveMove(self): #selects the specific files you want
        source = self.txtSource.get() #locate the source folder
        destination = self.txtDestination.get() #locate the destination folder
        files = os.listdir(source) #files in the source folder
        for i in files:
            filepath=os.path.join(source, i) #full filepath that has the path(source) and the file with extension (i)
            
            x = datetime.now() #time right now
            y = x - timedelta(hours=24) #time 24hours ago
            modtime=os.path.getmtime(filepath) #checks when the file was last modified. Was it within the 24hr window?
            datetimeOfFile=datetime.fromtimestamp(modtime)#when file was modified last
            if y < datetimeOfFile:
                shutil.move(source + '/' + i, destination) #source is the path, i is the file and its extension
                print(i + ' was transferred') #response on shell to action taken
           

    #browse button action
    def browseS(self):
        sName=fd.askdirectory() #to access the source folder
        self.txtSource.insert(0,sName) #populates the text box with the file path
        print(sName)
              

    def browseD(self):
        dName=fd.askdirectory() #to access the destination folder
        self.txtDestination.insert(0,dName) #populates the text box with the file path
        print(dName)
        
            
    #close button
    def close_window(self):
        self.master.destroy() #close the tkinter



if __name__=='__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
