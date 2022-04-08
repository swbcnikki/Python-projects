
import sqlite3 # importing sqlite3 module

conn = sqlite3.connect('step222.db') # creating the db where the data
# will go. Once you save and run these first 2 lines successfully, db is created.


with conn: # working within the connection that has been established
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_textFile TEXT)") # table with 2 fields. number in db and name of file
    conn.commit()

#list of file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
# use for to loop through each object in the list to find the txt files
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_fileList(col_textFile) VALUES (?)", (x,))
            # above is inserting the data into the db
            print(x)
conn.close() # remember to always close the connection when your code is done.
