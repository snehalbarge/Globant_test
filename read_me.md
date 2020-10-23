#### Exercise - 1
To get the output - 
* In the same folder, type *python* and hit enter
* Run the following
```
from exercise_one import Employee
employee = Employee("Jane","Doe","No. 12 Short Street, Greenville",21,21,60,"2/3/2020","SDE","XYZ")
print(f'Total number of instance created {Person.count}')
print(employee)
pr = employee.get_object_without_age()
```

#### Exercise - 2
To get the output - 
* In the same folder, type *python* and hit enter
* Run the following
```
from exercise_two import get_data_from_txt
f1 = 'text_task_two.txt'
print(get_data_from_txt(f1))

```

#### Exercise - 3
To get the output -
* In the same folder, type *python* and hit enter
* Run the following
```
from exercise_three import validator

@validator(int, int, str)
def f(a, b, c):
    pass

f(1, 2, 3)
```

#### Exercise - 5
To get the output - 
* In the same folder, type *python* and hit enter
* Run the following
```
from exercise_five import List
mylist = List()
mylist.append(1).append(2).append(3).append(4).append(5)
list(mylist.items())

list(mylist.map(lambda x: x*x).items())

list(mylist.map(lambda x: x*x).filter(lambda x: x > 3 and x < 25).items())

list(mylist.map(lambda x: x*x).filter(lambda x: x > 3 and x < 25).reduce(lambda x,y:x+y).items())

list(mylist.items())
```
