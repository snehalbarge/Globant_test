import unittest


class List():
    """   Creates a LinkedList   """

    def __init__(self):
        self.head = None
        self.size = 0

    class Node():
        """   Shows a Single Node of LinkedList   """

        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def append(self, val):
        new = self.Node(val)
        self.size += 1
        if self.head :
            current = self.head
            while current.next :
                current = current.next
            current.next = new

        else:
            self.head = new
        return self

    def items(self):
        current = self.head
        while current:
            yield current.val
            current = current.next

    def map(self, function):
        current = self.head
        while current:
            current.val = function(current.val)
            current = current.next
        return self

    def filter(self, function):
        current = self.head
        if function(current.val):
            self.head = current.next
            self.size -= 1
        else:
            previous = None
            while current.next:
                previous = current
                current = current.next
            previous.next = current.next
            self.size -= 1

        return self

    def reduce(self, function):
        current = self.head
        temp = current.val
        for i in range(self.size-1):
            current = current.next
            temp = function(temp, current.val)

        self = List().append(temp)
        return self


class TestList(unittest.TestCase):
    def setUp(self):
        self.l1 = List()
        self.l1.append(55).append(5).append(77).append(4).append(0)

    def test_append(self):
        self.assertEqual(list(self.l1.items()), [55,5,77,4,0])

    def test_map(self):
        self.l1.map(lambda x: x * 2)
        self.assertEqual(list(self.l1.items()), [110, 10, 154, 8, 0])

    def test_filter(self):
        self.l1.filter(lambda x: x > 50)
        self.assertEqual(list(self.l1.items()), [5, 77, 4, 0])

    def test_reduce(self):
        l1 = self.l1.reduce(lambda x, y: x - y)
        self.assertEqual(list(l1.items()), [-31])


if __name__ == "__main__":
    unittest.main()