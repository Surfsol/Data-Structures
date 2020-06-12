from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
 #  None <- prev (Head node) next -> <-prev (node) next -> <- prev (Tail node) next -> None        
    def append(self, item):
        #remove head
        self.current = self.storage.head
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(self.current)
            self.current = self.storage.head
        if len(self.storage) == self.capacity:
            #if it is the head
            if not self.current.prev:
                #assgin current
                self.current = self.storage.head.next
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
             #if tail   
            elif not self.current.next:
                #reassign current to head
                self.current = self.storage.head
                self.storage.remove_from_tail()
                self.storage.move_to_end(item)
            else:
                self.current = self.current.next
                self.current.insert_after(item)
                self.current.delete()
               
        


        


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        #place into list_buffer_contents and return
        self.current = self.storage.head
        while self.current:
            list_buffer_contents.append(self.current.value)
        self.current.next.get()

        return list_buffer_contents