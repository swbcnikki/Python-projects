
#the point of this code is to generate a html doc using tkinter and py that gives
#users the fields to imput their own text that will appear on that html doc. The
#html doc should be launched by an action from the tkinter GUI in a new tab with
#the text from the user displaying

import tkinter
from tkinter import *
import tkinter as tk
import webbrowser #make sure you import the right thing... don't get fancy


class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        

#tkinter page parameters and name
        self.master = master
        self.master.minsize(400,250)
        self.master.maxsize(400,250)
        self.master.title('Webpage Generator')
        self.master.config(bg='#FFA07A')

        
#set the variables to string
        self.varName = StringVar()
        self.varSentence = StringVar()

        
#create the label for the name
        self.lblName = Label(self.master, text='Your Name', font=('Ariel', 12), fg='white', bg='darkblue')
        self.lblName.grid(row=0, column=0,padx=(30,0), pady=(30,0))
#create the label for the sentence
        self.lblSentence = Label(self.master, text='Your Sentence', font=('Ariel', 12), fg='white', bg='darkblue')
        self.lblSentence.grid(row=1, column=0,padx=(30,0), pady=(30,0))


#create the text box for the name
        self.txtName = Entry(self.master, text=self.varName, font=('Ariel', 12), fg='black', bg='white')
        self.txtName.grid(row=0, column=1,padx=(30,0), pady=(30,0))
#create the text box for the sentence
        self.txtSentence = Entry(self.master, text=self.varSentence, font=('Ariel', 12), fg='black', bg='white')
        self.txtSentence.grid(row=1, column=1,padx=(30,0), pady=(30,0))


#create the submit button
        self.btnSubmit = Button(self.master, text='Submit', width=7, height=1, command=self.submit)
        self.btnSubmit.grid(row=3, column=1,padx=(0,0), pady=(30,0), sticky=NE)

    def submit(self): #the part below deals with what happens when the submit event takes place, ie, clicking the submit button       
      
        f = open('tkinterWebpage.html', 'w') #creates the html document
        #the part below allows other users to put in their own text in the tkinter, which then appears in the html doc
        text = ('''
            <html>
                <body>
                    <h1>
                    User: {} said, {}
                    </h1>
                </body>
            </html>
        ''').format(self.txtName.get(),self.txtSentence.get()) 
        f.write(text)
        f.close()
        webbrowser.open_new_tab('tkinterWebpage.html') #opens the html doc you created above in a new webbrowser tab
                        
          

        


if __name__=='__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

