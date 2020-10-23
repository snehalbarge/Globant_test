import unittest


class Person():
    counter = 0

    def __init__(self, name, lastname, address, age=None):
        Person.counter += 1
        self.__name = name
        self.__lastname = lastname
        self.age = age
        self.address = address

    def get_name(self):
        return self.__name

    def get_lastname(self):
        return self.__lastname

    def get_instance_without_age(self):
        return Person(name=self.__name, lastname=self.__lastname, address=self.address)

    def get_full_name(self):
        return self.__name + self.__lastname


class Employee(Person):
    def __init__(self, name, lastname, age, address, emp_code, sal_per_hour, start_date, position, dept):
        self.emp_code = emp_code
        self.sal_per_hour = sal_per_hour
        self.start_date = start_date
        self.position = position
        self.dept = dept

        Person.__init__(self, name, lastname, age, address)


class PersonTest(unittest.TestCase):

    def setUp(self):
        self.name = 'Thomas'
        self.lastname = 'George'
        self.address = 'No. 01, Lane 6, Windel'
        self.age = 28
        Person.counter=0
        self.p1 = Person(name=self.name, lastname=self.lastname,
                         address=self.address, age=self.age)

    # def tearDown(self):
    #     Person.counter = 0

    def test_person_count(self):
        # _ = Person(name=self.name, lastname=self.lastname,
        #            address=self.address, age=self.age)

        self.assertEqual(Person.counter, 1)

    def test_attr(self):
        self.assertEqual(self.p1.get_name(), self.name)
        self.assertEqual(self.p1.get_lastname(), self.lastname)
        self.assertEqual(self.p1.address, self.address)
        self.assertEqual(type(self.p1.age), type(self.age))

    def test_full_name(self):
        self.assertEqual(self.p1.get_name() + self.p1.get_lastname() , self.name + self.lastname)

    def test_get_instance_without_age(self):
        person1 = Person(name=self.name, lastname=self.lastname,
                    address=self.address)
        person1_without_age = self.p1.get_instance_without_age()

        self.assertEqual(person1.age, person1_without_age.age)


class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.emp_code = 1005
        self.sal_per_hour = 77
        self.start_date = '8/2/2019'
        self.position = 'Assistant manager'
        self.dept = 'Spark'
        self.name = 'Thomas'
        self.lastname = 'George'
        self.address = 'No. 01, Lane 6, Windel'
        self.age = 28

    def test_attr(self):
        empl1 = Employee(self.name, self.lastname, self.address, self.age, self.emp_code, self.sal_per_hour, self.start_date, self.position, self.dept)
        self.assertEqual(empl1.emp_code, self.emp_code)
        self.assertEqual(empl1.sal_per_hour, self.sal_per_hour)
        self.assertEqual(empl1.start_date, self.start_date)
        self.assertEqual(empl1.position, self.position)
        self.assertEqual(empl1.dept, self.dept)


if __name__ == '__main__':
    unittest.main()