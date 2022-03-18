class Node:
    
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def clean(self):
        node = self.head
        prev_node = node
        while node != None:
            if node.next != None:
                node = node.next
                prev_node.next = None
                prev_node.value = None
            else:
                node = node.next
                prev_node.next = None
                prev_node.value = None
                break
            prev_node = node

    def len(self):
        lenght = 0
        node = self.head
        while node is not None:
            lenght +=1
            node = node.next
        return lenght

    def insert(self, afterNode, newNode):
        if afterNode != None and afterNode != self.tail:
            node = afterNode
            next_node = node.next
            afterNode.next = newNode
            newNode.next = next_node
        elif afterNode == None:
            node = self.head
            newNode.next = node
            self.head = newNode
        elif afterNode != None and afterNode == self.tail:
            afterNode.next = newNode
            self.tail = newNode