class Node:
    def __init__(self, value = None, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self):
        pass

    def access(self):
        pass

    def search(self):
        pass

n1 = Node(3)
n2 = Node(4)
n3 = Node(5)
n4 = Node(6)

# print(n1.value, n2.value, n3.value,n4.value)

LL = LinkedList()
LL.head = n1
n1.next = n2
n2.next = n3
n3.next = n4

print(n1,n2,n3,n4)