Big o - judge algo based on own merrit, not dependent on your computer
 - can measure by counting number of operation code performs
 - how does number of operations scale on input

o(1)  # of operations does not scale based upon index
no matter input, will always take same amount of operations

o(n) number of operations does depend on input size.
        - such as looping
        - doesn't matter if increasing by 1/2 2 or ..., it is always o(n)
                because the line is the same shape (striaght)
    
    # step will do every other
    for i in range(0, len(arr), step=2):

stacks
    lifo order - put one on top of other.  would take off last one to use.
        -ex. stack of plates

queue - horizontial
    FiFo - first in first out

Arrays : allow you to index

arrays and link lists : store things in order

link lists are nodes connected to each other.
    - each element stored in its own node and nodes are connected.

    - can point to nodes from any other node, does not need to go in order 
    like array

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = Node(value=None, next_node=None)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, value):
        new_node = Node(value)
        #what if list is empty
        if not self.head:
            self.head = new_node

        else:
            # what node do we want to add new node to
            # add to last node on list
            # can get to last node in list by traversing
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            # we are at end of the linked list
            current.set_next(new_node)
    
    def remove_from_head(self):
        #what if list is empty
        if not self.head:
            return None
        # what is list is not empty
        else:
            # return value at the current head
            value = self.head.get_value()
            # remove value at the head
            # update self.head
            self.head = self.head.get_next()
            return value


run time complexity 
log(n)  run time for binary tree