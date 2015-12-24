# Stack()

## Operations
* push(item) >> places item at the top of the stack
* pop() >> removes and returns the value at the top of the stack
* peek() >> returns the value at the top of the stack
* isEmpty() >> returns boolean, see if stack is empty
* size() >> returns number of items in stack

## Implementation
```python
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
```

# Queue()

## Operations
* enqueue(item) >>  adds item to end of queue
* dequeue() >> returns and removes front item of queue
* isEmpty() >> returns boolean whether queue is empty
* size() >> returns number of items in queue

## Implementation
```python
class Queue:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0,item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)
```

# Deque()

## Operations
* addFront(item) >> adds item to front of deque
* addRear(item) >> add item to rear of deque
* removeFront() >> returns and removes front item
* removeRear() >> returns and removes rear item
* isEmpty() >> returns boolean whether deque is empty
* size() >> returns number of items in deque

## Implementation
```python
class Deque:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    returns self.items == []

  def addFront(self, item):
    self.items.append(item)

  def addRear(self, item):
    self.items.insert(0,item)

  def removeFront(self):
    self.items.pop()

  def removeRear(self):
    self.items.pop(0)

  def size(self):
    return len(self.items)
```

# Node()

## Implementation
```python
class Node:
  def __init__(self,initdata):
    self.data = initdata
    self.next = None

  def getData(self):
    return self.data

  def getNext(self):
    return self.next

  def setData(self,newdata):
    self.data = newdata

  def setNext(self,newnext):
    self.next = newnext
```

# UnorderedList()
*uses Node class*

## Implementation
```python
class UnorderedList:
  def __init__(self):
    self.head = None

  def isEmpty(self):
    return self.head == None

  def add(self,item):
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp

  def size(self):
    current = self.head
    count = 0
    while current != None:
      count = count + 1
      current = current.getNext()

    return count

  def search(self,item):
    current = self.head
    found = False
    while current != None and not found:
      if current.getData() == item:
        found = True
      else:
        current = current.getNext()

    return found

    def remove(self,item):
      current = self.head
      previous = None
      found = False
      while not found:
        if current.getData() == item:
          found = True
        else:
          previous = current
          current = current.getNext()

      if previous == None:
        self.head = current.getNext()
      else:
        previous.setNext(current.getNext())
```

# OrderedList()

## Implementation
*only showing the methods that differ from that of UnorderedList*

```python
class OrderedList:
  def __init__(self):
    self.head = None

  def search(self,item):
    current = self.head
    found = False
    stop = False
    while current != None and not found and not stop:
      if current.getData() == item:
        found = True
      else:
        if current.getData() > item:
          stop = True
        else:
          current = current.getNext()

      return found

    def add(self,item):
      current = self.head
      previous = None
      stop = False
      while current != None and not stop:
        if current.getData() > item:
          stop = True
        else:
          previous = current
          current = current.getNext()

      temp = Node(item)
      if previous == None:
        temp.setNext(self.head)
        self.head = temp
      else:
        temp.setNext(current)
        previous.setNext(temp)
```
