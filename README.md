# todo_list 

## Basic Functionality 

A repo containing source code of a todo list application. The application 
will feature Create, Read, Update and Delete (CRUD) functionality and there
will be backend database which will store the task types as a table. Each table will have the following fields: id, user, task, status (done,in progressn not started). For now, I am deciding to not use a noSQL database since my data is not unstructued (ex:
JSON or documents).  


The table will look something like the following: 

Task Type 001 (Household chores): 

| Id |  User            |   Task     | Priority | Status      |
|:-- | ---------------- | --------   | -------  | ----------: |
|  1 | Abby             |   Dishes   |  High    | Done        |
|  2 | Tim              |   Vaccum   |  Med     | In Progress |
|  4 | Bruce            |   Make bed |   Low    | Not Started | 


## Currently working on... 

Figuring out how to grab database data in Python. Let's say each time a user wants to add or update a task, having to manually do it through PostgreSQL would be a major pain. Not all users would want to install postgreSQL! (nor would everyone have space to do so). An eaiser way to add and/or update users would be to create a function which does this for you seamlessly. I was thinking of creating getters and setters for some fields (status, priority, and task). And of course a function to delete the user once they're finished with their task (or once the status of the task is "Done"). 

In addition to the backend logic, I need to figure out what language and/or frontend framework to use for my web app. I will most likely be looking into JavaScript (or a JavaScript framework), since those are commonly used for making web applications. 
