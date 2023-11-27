"""
 * DO NOT ALTER OR REMOVE THIS  NOTICES OR THIS FILE HEADER FROM THE CODE.
 * This code is free software you can redistribute it and/or modify it
   published by the Good will of the author.

 * This code is distributed in the hope that it will be useful,Therefore
   use this code for your need or purpose and you can inform Error or part
   to modify or add.
 * Modifiying this code in a part or as Whole is possible and incremental modification is
   suggested please inform the author any modification you have done.
 * Please contact the Author,if you need additional information or have any questions.
     *Author:Duressa Shukuri
     *Email:duressashukuri2022@gmail.com
"""
class QueueArray:
    """Class that create Array based Queue(using list to simulate Array) object implements
       basic opreation on Queue
    """
    def __init__(self,capacity):
        """constructor for QueueArray and it hava capacity as its  parameter and intilize the
           following variables.
           array:python list and initilize it to zeros.
           capacity: the size of queueArray.
           front:pointer to the front element of the queue
           rear:pointer to the reare element of the queue
        """
        self.array=[0]*self.capacity
        self.capacity=capacity
        self.front=-1
        self.rear=-1
    def isEmpty(self):
        """Checks whether the queue contains element  or not
           params: None
           return:True if it contains else False
        """
        return True if self.front==-1 else False
    def isFull(self):
        """Checks whether the queue is full or not
           params:None
           return:True if it is Full else False
        """
        return true if self.front==0 and self.rear==self.capacity-1 else False
    def enqueue(self,e):
        """Append(or insert) the element into back of the queue that is represented by the list.
           params:e
           return:None
        """
        if self.isFull():
            raise Exception("QUEUE OVERFLOW...")
        if self.isEmpty():
            self.front=self.front+1
        self.rear=self.rear+1
        self.array[self.rear]=e
    def dequeue(self):
        """Pops element from front of  the queue, that represented by the list.
           params:None
           return:element from the stack
        """
        if self.isEmpty():
            raise Exception("QUEUE UNDERFLOW...")
        item=self.array[self.fron]
        if self.front>=self.rear:
            self.rear=-1
            self.front=-1
        self.front=self.front+1
        return item
    def getFront(self):
        """Return but without removing the front  element of the list or queue.
           params:None
           return:The front element of the queue or None if the list or queue is empty
        """
        if self.isEmpty():
            raise Exception("QUEUE IS EMPTY...")
        return self.array[self.front]
    def getRear(self):
        """Return but without removing the rear  element of the list or queue.
           params:None
           return:The rear element of the queue or None if the list or queue is empty
        """
        if self.isEmpty():
            raise Exception("QUEUE IS EMPTY...")
        return self.array[self.rear]
    def printArrayQueue(self):
        """print elements that are in the queue from left to the right raise exception if the queue is empty.
           params:None
           return:None
        """
        if self.isEmpty():
            raise Exception("QUEUE IS EMPTY...")
        for i in range(self.front,self.rear+1):
            print(self.array[i],end="-->")
class circularQueueArray:
    """Class that create Array based Circular Queue(using list to simulate Array) object implements
       basic opreation on Queue
    """
    def __init__(self,capacity):
        """constructor for QueueArray and it hava capacity as its  parameter and intilize the
           following variables.
           array:python list and initilize it to zeros.
           capacity: the size of queueArray.
           front:pointer to the front element of the queue
           rear:pointer to the reare element of the queue
        """
        self.array=[0]*self.capacity
        self.capacity=capacity
        self.front=-1
        self.rear=-1
    def isEmpty(self):
        """Checks whether the queue contains element  or not
           params: None
           return:True if it contains else False
        """
        return True if self.front==-1 else False
    def isFull(self):
        """Checks whether the queue is full or not
           params:None
           return:True if it is Full else False
        """
        return true if self.front==0 and self.rear==self.capacity-1 else False
    def enqueue(self,e):
        """Append(or insert) the element into back of the queue that is represented by the list.
           params:e
           return:None
        """
        if self.isFull():
            raise Exception("QUEUE OVERFLOW...")
        if self.isEmpty():
            self.front=self.front+1
        self.rear=(self.rear+1)%self.capacity
        self.array[self.rear]=e
    def dequeue(self):
        """Pops element from front of  the queue, that represented by the list.
           params:None
           return:element from the stack
        """
        if self.isEmpty():
            raise Exception("QUEUE UNDERFLOW...")
        item=self.array[self.fron]
        if self.front>=self.rear:
            self.rear=-1
            self.front=-1
        self.front=(self.front+1)%self.capacity
        return item
    def getFront(self):
        """Return but without removing the front  element of the list or queue.
           params:None
           return:The front element of the queue or None if the list or queue is empty
        """
        if self.isEmpty():
            raise Exception("QUEUE IS EMPTY...")
        return self.array[self.front]
    def getRear(self):
        """Return but without removing the rear  element of the list or queue.
           params:None
           return:The rear element of the queue or None if the list or queue is empty
        """
        if self.isEmpty():
            raise Exception("QUEUE IS EMPTY...")
        return self.array[self.rear]
    def printArrayQueue(self):
        """print elements that are in the queue from left to the right raise exception if the queue is empty.
           params:None
           return:None
        """
        if self.isEmpty():
            raise Exception("QUEUE IS EMPTY...")
        for i in range(self.front,self.rear+1):
            print(self.array[i],end="-->")
class queueList:
    """Class that create python list based queue object implements
       basic opreation on queue
    """
    def __init__(self):
        """constructor for queueList and it doesnt have any hava any parameter and intilize the
           following variables.
           list:python list.
        """
        self.list=[]
    def isEmpty(self):
        """Checks whether the queue contains element  or not
           params: None
           return:True if it not contains else False
        """
        return True if len(self.list)==0 else False
    def enqueue(self,e):
        """Pushes the element into the queue that is represented by the list.
           params:e
           return:None
        """
        self.list.append(e)
    def dequeue(self):
        """Pops element from front of  the queue, that represented by the list.
           params:None
         return:element from the queue
                """
        return self.list.pop()
    def getFront(self):
        """Return but without removing the front  element of the list or queue.
           params:None
           return:The front element of the queue or None if the list or queue is empty
        """
        return self.list[0]
    def getRear(self):
        """Return but without removing the rear  element of the list or queue.
           params:None
           return:The rear element of the queue or None if the list or queue is empty
        """
        return self.list[-1]
    def printList(self):
        """print elements that are in the queue from left to the right raise exception if the queue is empty.
           params:None
           return:None
        """
        for i in self.list:
            print(i,end="-->")
class linkedNode:
    """constructor for Node and it has parameters and intialize the
       following variables.
       next:pointer to next node of current node.
       value:value that stored in the Node.
    """
    def __init__(self,e):
        self.value=e
        self.next=None
class queueLinked:
    """Class that create linkedlist based queue object and implements basic opreation on queue
    """
    def __init__(self):
        """constructor for queueLinked and it doesnt have any hava any parameter and intilize the
           following variables.
           front:pointer to the of queue.
           rear:pointer to the of queue
         """
        self.front=None
        self.rear=None
    def isEmpty(self):
        """Checks whether the queue contains element  or not
           params: None
           return:True if it not contains else False
        """
        return True if self.front==None else False
    def enqueue(self,e):
        """Pushes the element into the queue that is represented by the list.
           params:e
           return:None
        """
        newNode=linkedNode(e)
        if self.isEmpty():
            self.front=newNode
            self.rear=newNode
            return None
        self.rear.next=newNode
        self.rear=newNode

    def dequeue(self):
        """Pops element from front of  the queue, that represented by the list.
           params:None
           return:element from the queue
        """
        if self.isEmpty():
            raise Exception("QUEUE IS EMPTY...")
        item=self.front.value
        self.front=self.front.next
        return item
    def getFront(self):
        """Return but without removing the front  element of the list or queue.
           params:None
           return:The front element of the queue or None if the list or queue is empty
        """
        if self.isEmpty():
            raise Exception("QUEUE IS EMPTY...")
        return self.front.value
    def getRear(self):
        """Return but without removing the rear  element of the list or queue.
           params:None
           return:The rear element of the queue or None if the list or queue is empty
        """
        if self.isEmpty():
            raise Exception("QUEUE IS EMPTY...")
        return self.rear.value
    def printLinkedQueue(self):
        """print elements that are in the queue from left to the right raise exception if the queue is empty.
           params:None
           return:None
        """
        if self.isEmpty():
            raise Exception("QUEUE ID EMPTY...")
        cur=self.front
        while cur!=None:
            print(cur.value,end="-->")
            cur=cur.next
class QueueApplication:
    """Class that works with queue Application(some most Important Application of the queue)
    """
    def breadthFirstPrint(self,array,root=0):
        """Traverse the array or list by assuming as tree.where index=0 is the root element
           equivalent with breadth first traversal of the tree.
           params:index of the root
           return:None .
        """
        queue=[root]
        while queue:
            current=queue.pop(0)
            print(array[current],end="-->")
            if current*2+1<len(array) :
                queue.append(current*2+1)
            if current*2+2<len(array):
                queue.append(current*2+2)



