import sqlite3 

#create connection to the db 
connection = sqlite3.connect('tasks.db')

#Cursor obj used to execute & fetch results from SQL queries 
cursor = connection.cursor()  


cursor.execute("CREATE TABLE task(Id integer, User text, Task text, Priority text, Status text)") 


cursor.execute(""" 
    INSERT INTO task VALUES
         (1, 'Jenny', 'Vaccum', 'Med', 'In Progress'), 
         (2, 'Abby', 'Clean dishes', 'High', 'Complete')
""")  


#print rows of the task table 
for row in cursor.execute("SELECT * FROM task"):
    print(row)


connection.close() 
