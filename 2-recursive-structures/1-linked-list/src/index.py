class LinkedList:
    def __init__(self, head = None):  
        self.head = head

    def find_by(self, idx):
        current_node =  self.head
        for i in range(idx):
            current_node = current_node.next_node
        return current_node.val
    
    def insert_next_node(self, val):
        current_node = self.head
        if current_node:
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = Node(val)
        else:
            self.head = Node(val)

        
class Node:
    def __init__(self, val, next_node=None): 
        self.val = val
        self.next_node = next_node
