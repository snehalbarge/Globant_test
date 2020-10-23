# Exercise 8: Web service using Django

## Technology used :
* Django
* JSON
* Django-rest-framework




## API endpoints :

     **Get :**

| URL                                     |         Purpose                         |
|-----------------------------------------|---------------------------------------
| 127.0.0.1:8000/employee/                |   Get all the employees                 |
| 127.0.0.1:8000/employee/?e_id=5         | get employee by employee id             |
| 127.0.0.1:8000/employee/?e_name=Raj     |   get employee by employee name         |
| 127.0.0.1:8000/employee/?e_loc=zzzz     |   get employee by location              |
| 127.0.0.1:8000/employee/?designation    |   get employee by designation           |
| 127.0.0.1:8000/employee/?top_emp=< integer : n >     |   get top n employees with lowest salaries    |


**POST :** Insert an employee <br />
127.0.0.1:8000/employee/ <br />
   body:{
    "e_id":"5",
    "e_name":"Raj",
    "e_sal":100000,
    "e_loc":"zzzz",
    "email":"abc@gmail.com",
    "designation":"Engg"

}

**DELETE :** Delete an employee <br />
127.0.0.1:8000/employee/
body:{
    "e_id":"1"
}


## Command to run :

    > cd web_service/webservice
    > python3 manage.py runserver
