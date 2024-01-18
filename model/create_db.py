import sqlite3 

#create connection to the db 
connection = sqlite3.connect('tasks.db')

#Cursor obj used to execute & fetch results from SQL queries 
cursor = connection.cursor()  


cursor.execute("CREATE TABLE task(Id, User, Task, Priority, Status)")