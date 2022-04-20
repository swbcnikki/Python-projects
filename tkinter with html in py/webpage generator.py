import tkinter as tk
from tkinter import*
import webbrowser

f = open('myfile.html', 'w')

text = '''
    <html>
        <body>
            <h1>
        Stay tuned for our amazing summer sale!
            </h1>
        </body>
    </html>    
'''
f.write(text)
f.close()
webbrowser.open_new_tab('myfiles.html')

