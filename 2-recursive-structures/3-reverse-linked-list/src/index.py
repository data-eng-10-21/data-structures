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

    def reverse(self):
        #original:  7, 'a', 'hello', 19, 'b'
        # reverse 'b', 19, 'hello', 'a', 7
        # head has no next
        # 'a' next 7
        # 'hello' next 'a'
        prev_node = self.head # 7
        current_node = self.head.next_node # 'a'
        while current_node.next_node:
            
            print('current node', current_node.val)
            print('prev node', prev_node.val)
            next_node = current_node.next_node
            current_node.next_node = prev_node # 7
            prev_node = current_node # a
            current_node = next_node # 'hello'
        self.head = current_node
        self.head.next_node = prev_node
        return self
            


class Node:
    def __init__(self, val, next_node=None): 
        self.val = val
        self.next_node = next_node
