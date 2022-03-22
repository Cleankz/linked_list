import unittest
from random import randint

from List import Node
from List import LinkedList

class MyTests(unittest.TestCase):
    def test_insert(self):
        for i in range(10000000000):
            LinkedList.insert(Node(randint(100)))
        self.assertEqual(LinkedList.insert(Node(randint(100))),LinkedList.insert(Node(randint(100))))

    def test_delete(self):
        LinkedList.delete(50,False)

if __name__ == '__main__':
    unittest.main()