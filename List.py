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
        while node != None:
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
        
    def delete(self, val, all=False):
        if all == False:
            node = self.head
            while node != None:
                if  node.value == val and (node != self.tail or node != self.head):
                    prev_node.next = next_node
                    node.next = None
                    break
                elif  node.value == val and  node == self.head:
                    node.next = None
                    self.head = node.next
                elif  node.value == val and  node == self.tail:
                    prev_node.next = None
                    self.tail = prev_node
                    break
                prev_node = node
                next_node = node.next.next
                node = node.next
        else:
            node = self.head
            while node != None:
                    if node.value == val and (node != self.tail or node != self.head):
                        node.next = None
                        prev_node.next = next_node
                        node = self.head
                    elif  node.value == val and  node == self.head:
                            node.next = None
                            self.head = node.next
                    elif  node.value == val and  node == self.tail:
                        prev_node.next = None
                        self.tail = prev_node
                        break
                    prev_node = node
                    next_node = node.next.next
                    node = node.next
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
            node = self.head
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
            
n0 = Node(123)
n1 = Node(55)
n2 = Node(33)
n3 = Node(68)
n4 = Node(72)
n5 = Node(55)
n6 = Node(66)
n7 = Node(77)
n8 = Node(88)
n1.next = n2
s_list = LinkedList()
s_list.add_in_tail(n1)
s_list.add_in_tail(n3)
s_list.add_in_tail(n3)
s_list.add_in_tail(n4)
s_list.add_in_tail(Node(128))
s_list.add_in_tail(n5)
s_list.add_in_tail(n6)
s_list.add_in_tail(n7)
s_list.add_in_tail(n8)
s_list.insert(n5,n0)
s_list.find_all(55)
print(s_list.print_all_nodes())
s_list.delete(66, all = False)
s_list.delete(55,all = True)
print("-------------")
print(s_list.len())
s_list.clean()

nf = s_list.find(55)
if nf is not None:
    print(nf.value)