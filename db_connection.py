from configparser import ConfigParser
import psycopg2  

#Read config file 
config = ConfigParser() 
config.read("settings.ini")

#get the database connection fields from the config file 
dbConnection = config["Task_TypeConfig"]


try:  
    #opens a database connection 
    connection = psycopg2.connect(
        database= dbConnection["database"],
        user= dbConnection["db_user"], 
        password= dbConnection["pass"],
        host= dbConnection["host"], 
        port= dbConnection["port"]
    ) 


    cursor_obj = connection.cursor() 

    cursor_obj.execute('SELECT * FROM "Household_Tasks"') 

    results = cursor_obj.fetchall() 

    print(results) 

    #close cursor and communication with the db 
    cursor_obj.close() 
    connection.close()  

except Exception as error: 
    print("Unable to connect to the postgres database.")