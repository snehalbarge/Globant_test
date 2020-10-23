class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add_value(self, value):
        if self.head is None:
            node = Node(value)
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            node = Node(value)
            temp.next = node

    def get_head(self):
        return self.head

    def check_list(self, e_id):
        temp = self.head
        while temp:
            if temp.data.e_id == e_id:
                return 0
            temp = temp.next
        return 1

    def delete(self, value):
        head_temp = self.head
        f = 0
        # for stating values
        while head_temp and head_temp.data.emp_id == value:
            f = 1
            temp = head_temp.next
            head_temp = temp

        # any value in the middle
        self.head = head_temp
        temp = self.head
        prev = None

        while temp and temp.next:

            if temp.data.emp_id == value:
                f = 1
                t1 = temp.next
                prev.next = t1
                temp = t1
            else:
                prev = temp
                temp = temp.next

        if temp and temp.data.emp_id == value:
            f = 1
            prev.next = None
        if f != 0:
            return "Employee is deleted"
        else:
            return "Employee not found"
