

import sqlite3
connection = sqlite3.connect("C:/Users/bibo/Documents/GitHub/Python-Projects/test_database.db") #Creating a new db. Same process to connect to an existing one.

c = connection.cursor() #Instantiating Cursor object c

#c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)") #creating new table and inserting 3 columns with text fields. Once created, this line is not needed

#c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)") #Inserting data into the table

#connection.commit() #Commit to db to verify intentions

#connection = sqlite3.connect(':memory:') #To create it in temporary RAM

#c.execute("DROP TABLE IF EXISTS People") #To delete table

#connection.close() #Closes the connection


with sqlite3.connect("test_database.db") as connection: #More compact form of rhe code. "with" allows connecting to db, autocommit as you go with changes visible at connection close.
    #If you need to see changes immediately, and are not ready to close, do a manual commit.
    c.execute("CREATE TABLE Weapons(Name TEXT, Type TEXT, Number INT)")
    c.execute("INSERT INTO Weapons VALUES('Claws', 'Cat', 7), ('Teeth', 'Dog', 3)")

connection.close()


