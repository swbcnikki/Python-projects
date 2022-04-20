

from tkinter import *
import tkinter as tk
import webbrowser


class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        


        self.master = master
        self.master.minsize(400,250)
        self.master.maxsize(400,250)
        self.master.title('Webpage Generator')
        self.master.config(bg='#FFA07A')

        

        self.varName = StringVar()
        self.varSentence = StringVar()

        

        self.lblName = Label(self.master, text='Your Name', font=('Ariel', 12), fg='white', bg='darkblue')
        self.lblName.grid(row=0, column=0,padx=(30,0), pady=(30,0))

        self.lblSentence = Label(self.master, text='Your Sentence', font=('Ariel', 12), fg='white', bg='darkblue')
        self.lblSentence.grid(row=1, column=0,padx=(30,0), pady=(30,0))



        self.txtName = Entry(self.master, text=self.varName, font=('Ariel', 12), fg='black', bg='white')
        self.txtName.grid(row=0, column=1,padx=(30,0), pady=(30,0))

        self.txtSentence = Entry(self.master, text=self.varSentence, font=('Ariel', 12), fg='black', bg='white')
        self.txtSentence.grid(row=1, column=1,padx=(30,0), pady=(30,0))



        self.btnSubmit = Button(self.master, text='Submit', width=7, height=1, command=self.submit)
        self.btnSubmit.grid(row=3, column=1,padx=(0,0), pady=(30,0), sticky=NE)

    def submit(self):        
      
        f = open('tkinterWebpage.html', 'w')
        
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
        webbrowser.open_new_tab('tkinterWebpage.html')
                        
          

        


if __name__=='__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

