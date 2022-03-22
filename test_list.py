import unittest
import random

from numpy import equal
from List import Node
from List import LinkedList
from platform import node

class MyTests(unittest.TestCase):
    def test_insert(self):
        s_list = LinkedList()
        one_item_list = LinkedList()
        zero_list = LinkedList()
        n1 = Node(12)
        one_item_list.add_in_tail(n1)
        one_item_list.insert(n1,Node(random.randint(0,100000)))
        for j in range(10):
            s_list.add_in_tail(Node(random.randint(0,100000)))
        for i in range(1000):
            s_list.insert(None,Node(random.randint(0,100000)))
        for node in range(1010):
            s_list.insert(Node(random.randint(0,100000)),Node(random.randint(0,100000)))
        self.assertEqual(zero_list.insert(Node(random.randint(0,100000)),Node(random.randint(0,100000))),None)

    def test_delete_false(self):#тест удаления одного элемента
        s_list = LinkedList()
        zero_list = LinkedList()
        one_item_list = LinkedList()
        for i in range(1000000):
            s_list.add_in_tail(Node(random.randint(3,100000)))

        s_list.add_in_tail(Node(2))
        lenght = s_list.len()
        s_list.delete(2,False)
        self.assertEqual(s_list.len() == 1000000,True)
        s_list.delete(50,False)
        one_item_list.add_in_tail(50)
        one_item_list.delete(50,False)

        self.assertEqual(s_list.len()<lenght,True)
        self.assertEqual(zero_list.delete(14,False),None)

    def test_delete_True(self):#тест удаления всех элементов с заданным значением
        s_list = LinkedList()
        zero_list = LinkedList()
        one_item_list = LinkedList()
        for i in range(1000000):
            s_list.add_in_tail(Node(random.randint(0,100000)))
        s_list.add_in_tail(Node(2))
        lenght = s_list.len()
        s_list.delete(2,True)
        self.assertEqual(s_list.len() < 1000001,True)
        s_list.delete(50,True)
        self.assertEqual(s_list.len()<lenght,True)
        one_item_list.add_in_tail(50)
        one_item_list.delete(50,True)

        self.assertEqual(zero_list.delete(14,True),None)


    def test_clean(self):#тест  очищения списка
        s_list = LinkedList()
        for i in range(1000000):
            s_list.add_in_tail(Node(random.randint(0,100000)))
        self.assertEqual(s_list.clean(),None)

    def test_add_in_tail(self):#тест  добавления элемента в конец списка
        s_list = LinkedList()
        for i in range(1000000):
            s_list.add_in_tail(Node(random.randint(0,100000)))

    def test_find(self):#тест  поиска элемента
        s_list = LinkedList()
        for i in range(1000):
            s_list.add_in_tail(Node(random.randint(0,100)))
        result = s_list.find(100)
        one_item_list = LinkedList()
        n1 = Node(5)
        one_item_list.add_in_tail(n1)
        self.assertEqual(one_item_list.find(5),n1)
        self.assertEqual(s_list.find(100),result)
        zero_item_list = LinkedList()
        self.assertEqual(zero_item_list.find(100),None)
        

    def test_find_all(self):#тест  поиска элементов
        s_list = LinkedList()
        for i in range(2000):
            s_list.add_in_tail(Node(random.randint(0,100)))
        result = s_list.find_all(100)
        self.assertEqual(s_list.find_all(100),result)
        one_item_list = LinkedList()
        n1 = Node(359)
        one_item_list.add_in_tail(n1)
        self.assertNotEqual(one_item_list.find_all(359),None)
        zero_item_list = LinkedList()
        self.assertEqual(zero_item_list.find_all(100),[])

    def test_print_all_nodes(self):#тест  вывода элементов списка на экран
        s_list = LinkedList()
        for i in range(200):
            s_list.add_in_tail(Node(random.randint(0,100)))
        result = s_list.print_all_nodes()
        self.assertEqual(s_list.print_all_nodes(),result)

    def test_len(self):#тест  вычисления длины
        s_list = LinkedList()
        for i in range(200):
            s_list.add_in_tail(Node(random.randint(0,100)))
        self.assertEqual(s_list.len(),200)


if __name__ == '__main__':
    unittest.main()