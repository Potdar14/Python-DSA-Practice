'''
--- Queue ---
- Queue follows FIFO order (First in First out)
- In this elements will insert from backside and delete from front side.
- 1st element will enter from back and go towards front and that element only delete first,like that Queue will run.
- The entry side we call enqueue and the deleting side we call dequeue.
- queue can be implemented in:
    1] Normal list
    2] Collection (dequeue)
    3] Singly Linked List
    4] Doubly Linked List
    5] Circular Linked List
- In Queue two parts are mandatory:
    1] front - 1st element
    2] rear - last element
- Enqueue = for insertion
- Dequeue = for deletion
- Peak = Top
- size = Check data
'''

### Implementation of Queue:--
## 1] Normal Python List Data Type:-
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print(queue)
print("Front element:-",queue[0])
print("Rear element:-",queue[-1])
print("First element deleted:-",queue.pop(0))


## 2] Use collection:-
from collections import deque
x = deque()
x.append(1)
x.append(2)
x.append(3)
x.append(4)
x.append(5)
print("All element data:-",x)
print("Front element:-",x[0])
print("Rear element:-",x[-1])
print("First element deleted:-",x.popleft())

### Note:- if we want to delete element directly from left or right side without passing index position we will delete
##   it by using method var_name.popleft() --> for left side and var_name.popright() --> for right side
## but we can't use this directly we have to import --> from collections import deque

## 3] Singly Linked List:-
## pseudo code of SLL in queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print("None")
s = Queue()
s.display()       ## o/p -> Queue is empty


### Operations perform on queue -
## 1] Insert element in Queue (Using Enqueue)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, data):     ## for insertion we use enqueue
        NB = Node(data)      ## New Node
        if self.front is None:     ## if front 1st element is None
            self.front = NB         ## we will assign the same element front and rear.
            self.rear = NB
        else:
            self.rear.next = NB
                ## if 1st front element is not None we will assign rear(last) element's next part as New Node
            self.rear = NB     ## now the new node becomes last node so we will declare it here.
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print()
s = Queue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.enqueue(4)
s.enqueue(5)
s.display()


## 2] Delete element from the queue (using dequeue)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, data):
        NB = Node(data)
        if self.front is None:
            self.front = NB
            self.rear = NB
        else:
            self.rear.next = NB
            self.rear = NB
    def dequeue(self):
        if self.front is None:
            print("Empty")
            return
        data = self.front.next
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print()
s = Queue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.enqueue(4)
s.enqueue(5)
s.dequeue()
s.display()


## 3] to find peek element from Queue -
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
      
    def enqueue(self, data):
        NB = Node(data)
        if self.front is None:
            self.front = NB
            self.rear = NB
        else:
            self.rear.next = NB
            self.rear = NB
    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return
        return self.front.data
      
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print()
s = Queue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.enqueue(4)
s.enqueue(5)
s.peek()
s.display()
