class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

def sum_elements(ll):
    current_node = ll.head
    sum = 0
    while current_node is not None:
        sum += current_node.data
        current_node = current_node.next
    return sum

# Create a linked list
ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)

print(sum_elements(ll))

