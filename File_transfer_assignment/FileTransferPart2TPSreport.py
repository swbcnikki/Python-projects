
import shutil
import os
import time
import tkinter as tk
from tkinter import *

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        

#tkinter page parameters and name
        self.master = master
        self.master.minsize(800,250)
        self.master.maxsize(800,250)
        self.master.title('File Transfer of TPS Reports')
        self.master.config(bg='#20B2AA')




#space for tkinter labels and text boxes


        

#Peter has prepared the reports that go in a general folder with old and new files
source = '/Users/Bibo/Documents/GitHub/Python-Projects/Python-projects_in_Github/File_transfer_assignment/PeterGibbonsSends/'




#space for sort button to select files needed




def selectiveCopy(source, destination): #selects the specific files you want
    for i in files: #move the files represented by i
        os.path.getmtime(source)
        if mtime<24: #if timestamp is less than 24 hours ago
            shutil.move(source+i, destination)

#Bill is expecting to receive the late night and overnight report by noon
destination = '/Users/Bibo/Documents/GitHub/Python-Projects/Python-projects_in_Github/File_transfer_assignment/BillLumberghreceives/'
files = os.listdir(source)




#space for submit button to send the files to Bill




if __name__=='__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
