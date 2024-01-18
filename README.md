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
|  3 | Drake            |   Mop      |    Med   | Not Started |
|  4 | Bruce            |   Make bed |   Low    | Not Started |