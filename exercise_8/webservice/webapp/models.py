from operator import itemgetter

from webapp.Linked_list import LinkedList as List


class Employee_Details:
    def __init__(self, e_id, e_name, e_sal, e_loc, email, designation):
        self.e_id = e_id
        self.e_name = e_name
        self.e_sal = e_sal
        self.e_loc = e_loc
        self.email = email
        self.designation = designation

    def add_employee(self):
        is_unique = list.check_list(self.e_id)
        if is_unique:
            list.add_value(self)
            return "employees details Saved"
        else:
            return "e_id is already exist"


def get_all_object():
    data_list = []
    list_data = list.get_head()
    while list_data:
        d = {'e_id': list_data.data.e_id, 'e_name': list_data.data.e_name, 'e_sal': list_data.data.e_sal,
             'e_loc': list_data.data.e_loc, 'email': list_data.data.email,
             'designation': list_data.data.designation}
        data_list.append(d)
        list_data = list_data.next
    return data_list


def filter_by_id(e_id):
    data_list = []
    list_data = list.get_head()
    while list_data:
        d = {}
        if list_data.data.e_id == str(e_id):
            d['e_id'] = list_data.data.e_id
            d['e_name'] = list_data.data.e_name
            d['e_sal'] = list_data.data.e_sal
            d['e_loc'] = list_data.data.e_loc
            d['email'] = list_data.data.email
            d['designation'] = list_data.data.designation
            data_list.append(d)
        list_data = list_data.next
    return data_list


def filter_by_e_loc(emp_e_loc):
    data_list = []
    list_data = list.get_head()
    while list_data:
        d = {}
        if list_data.data.e_loc == str(emp_e_loc):
            d['e_id'] = list_data.data.e_id
            d['e_name'] = list_data.data.e_name
            d['e_sal'] = list_data.data.e_sal
            d['e_loc'] = list_data.data.e_loc
            d['email'] = list_data.data.email
            d['designation'] = list_data.data.designation
            data_list.append(d)
        list_data = list_data.next
    return data_list


def filter_by_designation(emp_designation):
    data_list = []
    list_data = list.get_head()
    while list_data:
        d = {}
        if list_data.data.designation == str(emp_designation):
            d['e_id'] = list_data.data.e_id
            d['e_name'] = list_data.data.e_name
            d['e_sal'] = list_data.data.e_sal
            d['e_loc'] = list_data.data.e_loc
            d['email'] = list_data.data.email
            d['designation'] = list_data.data.designation
            data_list.append(d)
        list_data = list_data.next
    return data_list


def filter_by_name(e_name):
    data_list = []
    list_data = list.get_head()
    while list_data:
        d = {}
        if list_data.data.e_name == e_name:
            d['e_id'] = list_data.data.e_id
            d['e_name'] = list_data.data.e_name
            d['e_sal'] = list_data.data.e_sal
            d['e_loc'] = list_data.data.e_loc
            d['email'] = list_data.data.email
            d['designation'] = list_data.data.designation
            data_list.append(d)
        list_data = list_data.next
    return data_list


def delete_emp(e_id):
    return list.delete(e_id)


def get_top_emp(value):
    data = get_all_object()
    data.sort(key=itemgetter('e_sal'))
    return data[:int(value)]

def display():
    return list.get_head()


list = List.LinkedList()
