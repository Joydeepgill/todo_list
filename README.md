# todo_list 

## Basic Functionality 

A repo containing source code of a todo list application. The application 
will feature Create, Read, Update and Delete (CRUD) functionality and there
will be backend database which will store the tasks as a table. Each user will have
the following fields: id, task, and status (done, in progress). For now, I am deciding to not use a noSQL database since my data is not unstructued (ex:
JSON or documents). 

The same task can be worked on by several people.  


The table will look something like the following: 

Task 001 (Cleaning the dishes): 

| Item              |  Values  | 
| :---------------- |  ------: |
| User              |   char   |
| Id                |   int    |
| Task              |   char   | 
| Status            |   char   | 
| Priority          |   char   |