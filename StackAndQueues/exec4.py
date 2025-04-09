class Queue:
    def __init__(self):
        self._head = self._tail = None
        self._size = 0
        
    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values = f'{current_node.data}, ' + values
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<Queue ({self._size} element{plural}): [{values.rstrip(", ")}]>'

        
        
    def enqueue(self, data):
        # Create the node with the value. This is the last node, so next is None,
        # but there can be already some node in the list, hence the prev value
        new_node = ListNode(data, next=None, prev=self._tail)

        # If list is empty, update head and tail pointers
        if self._head is None:
            self._head = self._tail = new_node
        else:
            # In any other case, update tail node to point to the new element
            # and update tail pointer. The new node already points to its
            # previous element
            self._tail.next = new_node
            self._tail = new_node

        # update size
        self._size += 1
    
    def dequeue(self):
        # If list is empty, returns None
        if not self._size:
            return None
        
        # Locate next_node (the node just after first node)
        node_to_remove = self._head
        next_node = node_to_remove.next

        # If node to remove is first node, then update head pointer
        if node_to_remove == self._tail:
            self._head = None
        else:
            # If not, update the pointer of the next node
            next_node.prev = None   # It is now the first node

        # Update tail pointer
        self._head = next_node

        # Update size, remove node and return its content
        self._size -= 1
        value = node_to_remove.data
        del(node_to_remove)
        return value