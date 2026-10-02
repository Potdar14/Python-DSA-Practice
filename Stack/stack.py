'''
---- Stack ----
- stack is LIFO Data Structure.
- Last in First out
     10 -> 20 -> 30 -> 40 -> 50
- Operations performs in stack:
1] Push            ---> Insert
2] Pop             ---> Delete
3] Total Peak      ---> To check top element
4] Size            ---> To check size of stack/ data present in stack

- stack we can implement in two concepts:
1] Python list data type
2] Linked List
==> mainly we focus on SLL
'''

## 1] Normal Python List Data Type in stack:
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)
print("Top element deleted:-",stack.pop())
print(stack)
### Note - Here , stack follows LIFO method so which element will came last that element will go out first
## and here last element which is entered in the list is 4 so , 4 will go out first.


## 2] Singly Linked List in Stack:
## Pseudo Code of stack : here the o/p is Empty, for adding or deleting we will add one more function.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None         ## top = first added element.
    def display(self):
        if self.top is None:
            print("Empty")
        else:
            temp = self.top
            while temp:
                print(temp.data,end=" ")
                temp = temp.next
s = Stack()
s.display()  ### o/p --> Empty

'''
top = first come element.
'''

## 1] Insert Element in Stack:- (Push operation)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def Push(self,data):
        NB = Node(data)
        NB.next = self.top    ## remember the o/p structure
        self.top = NB         ## is top element will change always??

    def display(self):
        if self.top is None:
            print("Empty")
        else:
            temp = self.top
            while temp:
                print(temp.data,end=" ")
                temp = temp.next
s = Stack()
s.Push(10)
s.Push(20)
s.Push(30)
s.display()  ## o/p --> 30 20 10
## Bcoz of stack follows LIFO therefore 10 will go forward and after 20 and then 30 means 30 20 10 like this we get o/p
## and we can easily delete the last element first.


## 2] To find Top/Peak element from stack -
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None

    def Push(self, data):
        NB = Node(data)
        NB.next = self.top
        self.top = NB

    def Peak(self):
        if self.top is None:
            print("Stack is Empty")
            return
        else:
            temp = self.top
            print("Top element of the stack is:-",temp.data)

    def display(self):
        if self.top is None:
            print("Empty")
        else:
            temp = self.top
            while temp:
                print(temp.data,end=" ")
                temp = temp.next
s = Stack()
s.Push(10)
s.Push(20)
s.Push(30)
s.display()
print()
s.Peak()


## 3] To Delete Top element from the stack
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def Push(self, data):
        NB = Node(data)
        NB.next = self.top
        self.top = NB

    def Pop(self):
        if self.top is None:
            print("Stack is Empty")
            return
        else:
            temp = self.top
            self.top = self.top.next
            print("Top deleted element is:-",temp.data)

    def display(self):
        if self.top is None:
            print("Empty")
        else:
            temp = self.top
            while temp:
                print(temp.data,end=" ")
                temp = temp.next
s = Stack()
s.Push(10)
s.Push(20)
s.Push(30)
s.Push(40)
s.display()
print()
s.Pop()


## 4] To check size of elements from the stack
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def Push(self, data):
        NB = Node(data)
        NB.next = self.top
        self.top = NB

    def Size(self):
        temp = self.top
        count = 0
        while temp:
            count += 1
            temp = temp.next
        print("Size of the stack is:-",count)

    def display(self):
        if self.top is None:
            print("Empty")
        else:
            temp = self.top
            while temp:
                print(temp.data,end=" ")
                temp = temp.next
s = Stack()
s.Push(10)
s.Push(20)
s.Push(30)
s.Push(40)
s.Push(50)
s.display()
print()
s.Size()

