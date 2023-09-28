from index import LinkedList, Node
def build_ll():
    b = Node('b')
    nineteen = Node(19, b)
    hello = Node('hello', nineteen)
    a = Node('a', hello)
    seven = Node(7, a)
    ll = LinkedList(seven)
    return ll

def test_find_by_returns_val_at_idx():
    ll = build_ll()
    assert ll.find_by(2) == 'hello'
    assert ll.find_by(3) == 19
