class Node:
    """make node"""

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        """adds a node to the end"""
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
    def print_all_nodes(self):
        """print all nodes"""
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        """finds a node by value"""
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        """finds all nodes by value"""
        result = []
        node = self.head
        while node is not None:
            if node == self.head and node == self.tail:
                result.append(node)
            elif node.value == val:
                result.append(node)
            node = node.next
        return result
            

    def delete(self, val, all=False):
        """if all is False - delete one node by value, else delete all nodes """
        if all is False:
            node = self.head
            while node is not None:
                if node == self.tail and node == self.head:
                    self.tail = None
                    self.head = None
                    node = None
                    break
                elif  node.value == val and  node == self.head:
                    self.head = node.next
                    prev_node = node
                    node = node.next
                    prev_node.next = None
                    prev_node = None
                    break
                elif  node.value == val and  node == self.tail:
                    prev_node.next = None
                    node = None
                    self.tail = prev_node
                    node = prev_node
                    break
                elif  node.value == val and (node != self.tail or node != self.head):
                    next_node = node.next
                    prev_node.next = next_node
                    node.next = None
                    node = None
                    node = prev_node
                    break
                prev_node = node
                node = node.next
        elif all is True:
            node = self.head
            while node is not None:
                if node == self.tail and node == self.head:
                    self.tail = None
                    self.head = None
                    node = None
                    break
                elif  node.value == val and  node == self.head:
                    prev_node = node
                    self.head = node.next
                    node = node.next
                    prev_node.next = None
                    prev_node = None
                    prev_node = node
                elif  node.value == val and  node == self.tail:
                    prev_node.next = None
                    node.next = None
                    node = None
                    self.tail = prev_node
                    next_node = None
                    break
                elif node.value == val:
                    next_node = node.next
                    prev_node.next = next_node
                    node.next = None
                    node = None
                    node = prev_node
                else:
                    prev_node = node
                    node = node.next
        return None
    def clean(self):
        """clears all variables"""
        node = self.head
        prev_node = node
        while node is not None:
            if node.next is not  None:
                node = node.next
                prev_node.next = None
                prev_node = None
            else:
                node = node.next
                prev_node.next = None
                prev_node = None
                break
            prev_node = node
        self.__init__()

    def len(self):
        """prints len of list"""
        len_t = 0
        node = self.head
        while node is not None:
            len_t +=1
            node = node.next
        return len_t

    def insert(self, afterNode, newNode):
        """inserts node into the list"""
        if afterNode is None:
            node = self.head
            newNode.next = node
            self.head = newNode
        elif afterNode is not None and afterNode == self.tail:
            afterNode.next = newNode
            self.tail = newNode
        elif afterNode is not None and (afterNode != self.tail and afterNode != self.head):
            node = afterNode
            next_node = node.next
            afterNode.next = newNode
            newNode.next = next_node
        else:
            return None