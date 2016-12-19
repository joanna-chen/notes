# Python Data Structures

## Stack()

### Operations
* push(item) >> places item at the top of the stack
* pop() >> removes and returns the value at the top of the stack
* peek() >> returns the value at the top of the stack
* isEmpty() >> returns boolean, see if stack is empty
* size() >> returns number of items in stack

### Implementation
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

## Queue()

### Operations
* enqueue(item) >>  adds item to end of queue
* dequeue() >> returns and removes front item of queue
* isEmpty() >> returns boolean whether queue is empty
* size() >> returns number of items in queue

### Implementation
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

## Deque()
* double-ended queue

### Operations
* addFront(item) >> adds item to front of deque
* addRear(item) >> add item to rear of deque
* removeFront() >> returns and removes front item
* removeRear() >> returns and removes rear item
* isEmpty() >> returns boolean whether deque is empty
* size() >> returns number of items in deque

### Implementation
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

## Node()

### Implementation
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

## UnorderedList()
*uses Node class*

### Implementation
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

## OrderedList()

### Implementation
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

## Sequential Search
* goes through every element to check if it is the value we are searching for

### Analysis of Sequential Search in UnorderedList
| Case | Best Case | Worst Case | Average Case |
|------|:----------|:-----------|:-------------|
| item is present | 1 | n | n/2 |
| item is not present | n | n | n |

### Analysis of Sequential Search in OrderedList
| Case | Best Case | Worst Case | Average Case |
|------|:----------|:-----------|:-------------|
| item is present | 1 | n | n/2 |
| item is not present | n | n | n/2 |
*can stop searching when reach midway*

## Binary Search
* start at the middle, eliminate half, go to middle of other half, continue...
* example of *divide and conquer*

### Analysis
* number of comparisons required: n/(2^i) = 1 --> i = log n
* therefore, O(log n)

## Hashing

### Hash Functions
* there is a hash function that takes the value in and maps the value to the out put of the hash function
* however, if there is more than one item in the same slot, there is a collision
* **perfect hash function**: a hash function that maps every item to a unique slot
* **folding method**: construct hash function by dividing item into equal-size parts
* **mid-square method**: first square the item, then extract some part of the result
* ordinal values: add up ordinal values and use remainder method
  * to take care of anagrams --> use weighted ordinal value based on position

### Collision Resolution
* **open addressing**: tries to find next open slot/address for the item that caused the collision
  * **linear probing**: systematically visiting each slot one at a time
  * instead of one at a time, can skip one which potentially reduces clustering
  * **quadratic probing**: uses a skip of successive perfect squares
* **rehashing**: the general name for finding another slot
* **chaining**: allows many items to exist in a slot in a hash table

### Implementation
* Map()
* put(key,val) >> add new key-value pair
* get(key) >> given key, return the value or None otherwise
* del map[key] >> delete key-value pair
* len() >> return number of key-value pairs
* in >> return whether ```key in map```

```python
class HashTable:
  def __init__(self):
    self.size = 11
    self.slots = [None] * self.size #holds the keys
    self.data = [None] * self.size #holds the values

  def put(self,key,data):
    hashvalue = self.hashfunction(key,len(self.slots))

    if self.slots[hashvalue] == None:
      self.slots[hashvalue] = key
      self.data[hashvalue] = data
    else:
      if self.slots[hashvalue] == key:
        self.data[hashvalue] = data  #replace
      else:
        nextslot = self.rehash(hashvalue,len(self.slots))
        while self.slots[nextslot] != None and self.slots[nextslot] != key:
          nextslot = self.rehash(nextslot,len(self.slots))

        if self.slots[nextslot] == None:
          self.slots[nextslot]=key
          self.data[nextslot]=data
        else:
          self.data[nextslot] = data #replace

  def hashfunction(self,key,size):
       return key%size

  def rehash(self,oldhash,size):
      return (oldhash+1)%size

  def get(self,key):
    startslot = self.hashfunction(key,len(self.slots))

    data = None
    stop = False
    found = False
    position = startslot
    while self.slots[position] != None and not found and not stop:
       if self.slots[position] == key:
         found = True
         data = self.data[position]
       else:
         position=self.rehash(position,len(self.slots))
         if position == startslot:
             stop = True
    return data

  def __getitem__(self,key):
      return self.get(key)

  def __setitem__(self,key,data):
      self.put(key,data)      
```

### Analysis
* best case O(1), constant time search

## Bubble Sort
* goes through list multiple times, compares adjacent items and exchanges them
* item "bubbles" up to location where it belongs
* simultaneous swap in Python: ```a,b = b,a```
* **short bubble**: stops swaps if already sorted

### Analysis
* n-1 passes must be made in a list of length n
* O(n^2)

## Selection Sort
* improves on bubble sort by only making one exchange per each pass
* finds the largest item and places it in the proper location

### Analysis
* in worst case, makes the same number of comparisons as bubble sort
* O(n^2)

## Insertion Sort


## Shell Sort


## Merge Sort
* recursive algorithm that continually splits list in half
* when two halves are sorted, they are merged

### Analysis
* to continuously split list in half is log n (binary search)
* merging list of size n requires n operations
* O(n log n)
* note: merge sort requires extra space to hold the split lists, so if the list is really big this could be an issue

## Quick Sort
* selects a value (**pivot value**) in the list
* **split point**: where the pivot value actually belongs in the list
* **partition process**: move all the other items to the correct side of the split point (greater than or less than)
* increment leftmark until find an item greater than the pivot value and decrement rightmark until find an item less than pivot value --> swap the two items, until leftmark is greater than rightmark
* place the pivot value where the split point is and call the function again on both partitions now
* **median of three**: take the first, middle and last value and take the median value to be the pivot value

### Analysis
* O(n log n) if the split point is at the middle
* in the worst case, it would become O(n^2) if splitpoint not in the middle
* but it does not require extra memory

## Tree

### List of lists representation

### Tree Traversals
* **preorder**: root, left, right
* **inorder**: left, root, right
* **postorder**: left, right, root

```python
def preorder(tree):
  if tree:
    print(tree.getRootVal())
    preorder(tree.getLeftChild())
    preorder(tree.getRightChild())
```

```python
def preorder(tree):
  print(self.key)  
  if self.leftChild:
    self.leftChild.preorder()
  if self.rightChild:
    self.rightChild.preorder()
```
*for inorder, put the print statement in the middle and for postorder, put the print statement at the end*

## Binary Heaps
* **priority queue**: a queue that is ordered by priority, so that the greatest priority goes to the front of the queue
* **min heap**: smallest key is in front
* **max heap**: largest value is at front
* **heap order property:** in a heap, for every node *x* with parent *p*, the key in *p* <= key in *x*

### Operations
* insert(k): add new item to heap
* findMin(): return item with the min key value, item stays in the heap
* delMin(): return item with the min key value, removes item form the heap
* isEmpty(): returns boolean whether the heap is empty
* size(): returns number of items int he heap
* buildHeap(list): builds new heap from list of keys

### Implementation
```python
class BinHeap:
  def __init__(self):
    self.heapList = [0]
    self.currentSize = 0

  # needed to swap items in the list when appending that does not follow the heap property
  def percUp(self, i):
    while i // 2 > 0:
      if self.heapList[i] < self.heapList[i // 2]: # diving by 2 gets the parent location
        temp = self.heapList[i // 2]
        self.heapList[i // 2] = self.heapList[i]
        self.heapList[i] = temp
      i = i // 2

  def insert(self, k):
    self.heapList.append(k)
    self.currentSize += 1
    self.percUp(self.currentSize)

  def percDown(self, i):
    while i*2 <= self.currentSize:
      mc = minChild(i)


  def delMin():

```

## Binary Search Tree

### Operations
* the operations of a map

### Implementation
* **bst property:**: the keys less than the parent are in left subtree, keys greater than the parent are in right subtree

### Analysis

## Graph

### Definitions
* **vertex:** the node
* **edge:** connects two nodes together, can be one-way or two-way
  * **directed graph/digraph:** all edges are one-way
* **weight:** edges can be weighted to show that there is a cost to go from vertex to vertex
* **path:** sequence of vertices connected by edges
* **cycle:** path that starts and ends at the same node
  * **acyclic graph:** graph with no cycle
  * **directed acyclic graph (DAG):** directed graph with no cycle

### Graph ADT
* ```Graph()``` creates new, empty graph
* ```addVert(vertex)``` adds an instance of ```Vertex``` to graph
* ```addEdge(fromVert, toVert)``` adds new, directed edge that connects two vertices
* ```addEdge(fromVert, toVert, weight)``` adds new, weighted, directed edge that connects two vertices
* ```getVertex(vertKey)``` finds vertex in graph called ```vertKey```
* ```getVertices()``` returns list of all vertices in graph
* ```in``` returns ```True``` for statement ```vertex in graph```, if the given vertex is in the graph, ```False``` otherwise

### Adjacency Matrix
* implement graph using two-dimensional matrix: each row and column represents a vertex in the graph
* value stored at cell intersection of row *v* and column *w* means there's an edge from vertex *v* to vertex *w*
* **adjacent:** when two vertices are connected by an edge
* the value in the cell represents the weight of the edge from vertex *v* to vertex *w*

#### Pros & Cons
| Pros | Cons |
| :------------- | :------------- |
| simple: for small graphs, easy to see which nodes are connected to others | "sparse": most of the cells in the matrix are empty |
| good implementation when number of edges is large (number of edges required to fill matrix is V^2) | not very efficient |

### Adjacency List
* more space-efficient way to implement sparsely connected graphs
* keep master list of all vertices in Graph object and each vertex object maintains list of other vertices it is connected to
* allows compact representation of sparse graphs
* allows to easily find all links that are directly connected to particular vertex

### Implementation

#### Vertex Class
```python
class Vertex:
  def __init__(self, key):
    self.id = key
    self.connectedTo = {}

  def addNeighbour(self, nbr, weight=0):
    self.connectedTo[nbr] = weight

  def __str__(self):
    return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

  def getConnections(self):
    return self.connectedTo.keys()

  def getId(self):
    return self.id

  def getWeight(self, nbr):
    return self.connectedTo[nbr]
```

#### Graph Class
```python
class Graph:
  def __init__(self):
    self.vertList = {}
    self.numVertices = 0

  def addVertex(self, key):
    self.numVertices = self.numVertices + 1
    newVertex = Vertex(key)
    self.verList[key] = newVertex
    return newVertex

  def getVertex(self, n):
    if n in self.vertList:
      return self.vertList[n]
    else:
      return None

  def __contains__(self, n):
    return n in self.vertList

  def addEdge(self, f, t, cost=0):
    if f not in self.vertList:
      nv = self.addVertex(f)
    if t not in self.vertList:
      nv = self.addVertex(t)
    self.vertList[f].addNeightbor(self.vertList[t], cost)

  def getVertices(self):
    return self.vertList.keys()

  def __iter__(self):
    return iter(self.vertList.values())
```
