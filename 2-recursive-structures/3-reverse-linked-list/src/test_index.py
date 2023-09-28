from index import LinkedList, Node
def build_ll():
    b = Node('b')
    nineteen = Node(19, b)
    hello = Node('hello', nineteen)
    a = Node('a', hello)
    seven = Node(7, a)
    ll = LinkedList(seven)
    return ll

# def test_find_by_returns_val_at_idx():
#     ll = build_ll()
#     assert ll.find_by(2) == 'hello'
#     assert ll.find_by(3) == 19

def test_reverse_ll():
    ll = build_ll() # 7, 'a', 'hello', 19, 'b' 
    reversed_ll = ll.reverse() # 'b', 19, 'hello', 'a', 7
    assert reversed_ll.head.val == 'b'
    assert reversed_ll.head.next_node.val == 19
