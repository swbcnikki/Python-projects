

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


