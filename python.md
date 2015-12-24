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
class Queue():
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
class Deque():
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
