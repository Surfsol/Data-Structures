"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
import sys
sys.path.append('./linked_list.py')
from linked_list import LinkedList

# class Stack:
#     def __init__(self):
#         #size starts at 0
#         self.size = 0
#         self.storage = LinkedList()

#     def push(self, value):
#         #increase size by 1
#         self.size += 1
#         #insert the value in the zero position
#         return self.storage.add_to_tail(value)

#     def pop(self):
#         #decrease size by 1
#         if self.size != 0:
#             self.size -= 1
#         #remove 0 position value
#             return self.storage.remove_head()
#         else:
#             return None

#     def __len__(self):
#         return self.size
   
class Stack:
    def __init__(self):
        #size starts at 0
        self.size = 0
        self.storage = []

    def push(self, value):
        #increase size by 1
        self.size += 1
        #insert the value in the zero position
        return self.storage.append(value)

    def pop(self):
        #decrease size by 1
        if self.size != 0:
            self.size -= 1
        #remove 0 position value
            return self.storage.pop()
        else:
            return None

    def __len__(self):
        return self.size
