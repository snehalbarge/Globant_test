import unittest
import sys


def get_data(filename):
    """Function to read file and acquire the data"""

    with open(filename, 'r') as f:
        data = f.readlines()

    return data


def process_data(data):
    """Function to process the data"""

    columns = data[0].split(';')
    columns[-1] = columns[-1][: -1]

    # Preparing nested dictionary object of the data
    data = data[1:]
    records = dict()
    for x, i in enumerate(data):
        i = i[: -1]
        fields = i.split(';')
        tmp = dict(zip(columns, fields))

        records[x] = tmp

    # Nested dictionary with no duplicates
    fixed_data = {}

    #list to hold salaries of employees, which can then be used for finding minimum salary
    salaries = []

    # Creating new dictionary with no duplicates
    for key,value in records.items():
        if value not in fixed_data.values():
            fixed_data[key] = value
            salaries.append(int(value['salary']))

    return [fixed_data, salaries]


def get_min_salary(lst):
    """Function to get minimum salary"""

    min_sal = min(lst[1])

    # Printing minimum salary
    print(f"min_sal - {min_sal}")

    # Filtering employees with lowest salaries using dict comprehensions
    result_dict = { key: value for key, value in lst[0].items() if value['salary'] == str(min_sal) }

    # return the records that meet the criteria
    data = []
    for key, value in result_dict.items():
        data.append(value)
    
    return data


def execute(filename):
    data = get_data(filename)
    lst = process_data(data)
    result = get_min_salary(lst)

    print(result)
    return result


class TestFunc(unittest.TestCase):

    def test_execute(self):
        f1 = 'text_task_two.txt'

        output = [{'employee_code': '1', 'name': 'john', 'lastname': 'doe', 'address': 'add1', 'age': '40', 'start_date': '03-05-1980', 'salary': '2500', 'position': 'head', 'department': 'abc'}]

        print("------execute--------")
        print(execute(f1))
        print(output)
        self.assertEqual(execute(f1), output)


if __name__ == "__main__":

    if sys.argv[1] == "test":
        import os
        os.system('python3 -m unittest ques_2.py')

    else:
        execute(sys.argv[1])