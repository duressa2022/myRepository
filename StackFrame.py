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
class stackArray:
    """Class that create Array based Stack(using list to simulate Array) object implements
       basic opreation on Stack
    """
    def __init__(self,capacity):
        """constructor for stackArray and it hava capacity as its  parameter and intilize the
           following variables.
           array:python list and initilize it to zeros.
           capacity: the size of stackArray.
           TOP:pointer to the top element of the the stack
           """
        self.array=[0]*self.capacity
        self.capacity=capacity
        self.Top=-1
    def isEmpty(self):
        """Checks whether the stack contains element  or not
           params: None
           return:True if it contains else False
        """
        return True if self.Top==-1 else False
    def isFull(self):
        """Checks whether the stack is full or not
           params:None
           return:True if it is Full else False
        """
        return True if self.Top==self.capacity-1 else False
    def push(self,e):
        """Pushes the element into the stack that is represented by the list.
           params:e
           return:None
        """
        if self.isFull():
            raise Exception("STACK OVERFLOW....")
        self.Top=self.Top+1
        self.array[self.Top]=e
    def pop(self):
        """Pops element from top of  the stack, that represented by the list.
           params:None
           return:element from the stack
        """
        if self.isEmpty():
            raise Exception("STACK UNDERFLOW....")
        item=self.array[self.Top]
        self.Top=self.Top-1
        return item
    def peak(self):
        """Return but without removing the first  element of the list or stack.
           params:None
           return:The top element of the stack or None if the list or stack is empty
        """
        if self.isEmpty():
            raise Exception("STACK UNDERfLOW...")
        return self.array[self.Top]
    def prinStack(self):
        """print elements that are in the stack from bottom to the top raise exception if the stack is empty.
           params:None
           return:None
        """
        if self.isEmpty():
            raise Exception("STACK UNDER ITS CAPACITY....")
        for i in range(self.Top+1):
            print(self.array[i],end="-->")
class stackList:
    """Class that create python list based Stack object implements
       basic opreation on Stack
    """
    def __init__(self):
        """constructor for stackList and it doesnt have any hava any parameter and intilize the
           following variables.
           list:python list and initilize it to zeros.
        """
        self.list=[]
    def isEmpty(self):
        """Checks whether the stack contains element  or not
           params: None
           return:True if it not contains else False
        """
        return True if len(self.list)==0 else False
    def push(self,e):
        """Pushes the element into the stack that is represented by the list.
           params:e
           return:None
        """
        self.list.append(e)
    def pop(self):
        """Pops element from top of  the stack, that represented by the list.
           params:None
           return:element from the stack
        """
        return self.pop()
    def peek(self):
        """Return but without removing the first  element of the list or stack.
           params:None
           return:The top element of the stack or None if the list or stack is empty
        """
        return self.list[-1]
    def printStackList(self):
        """print elements that are in the stack from bottom to the top raise exception if the stack is empty.
           params:None
           return:None
        """
        for i in self.list:
            print(i,end="-->")
class listNode:
    def __init__(self,e):
        """constructor for Node and it has parameters and intialize the
           following variables.
           next:pointer to next node of current node.
           value:value that stored in the Node.
        """
        self.value=e
        self.next=None
class stackLinked:
    """Class that create linkedlist based Stack object and implements basic opreation on Stack
    """
    def __init__(self):
        """constructor for stackLinked and it doesnt have any hava any parameter and intilize the
           following variables.
           head:pointer to the to of stack.
        """
        self.head=None
    def isEmpty(self):
        """Checks whether the stack contains element  or not
           params: None
           return:True if it not contains else False
         """
        return True if self.head==None else False
    def push(self,e):
        """Pushes the element into the stack that is represented by the linkedList.
            params:e
            return:None
        """
        newNode=listNode(e)
        if self.head==None:
            self.head=newNode
            return None
        newNode.next=self.head
        self.head=newNode
        return None
    def pop(self):
        """Pops element from top of  the stack, that represented by the LinkedList.
           params:None
           return:element from the stack
        """
        if self.isEmpty()==True:
            raise Exception("Stack UNDERFLOW....")
        item=self.head.value
        self.head=self.head.next
        return item
    def peak(self):
        """Return but without removing the first  element of the list or stack.
           params:None
           return:The top element of the stack or None if the list or stack is empty
        """
        if self.isEmpty()==True:
            raise Exception("STACK IS EMPTY...")
        return self.head.value
    def printStackLinked(self):
        """print elements that are in the stack from bottom to the top raise exception if the stack is empty.
           params:None
           return:None
        """
        if self.isEmpty()==True:
            raise Exception("STACK IS EMPTY...")
        current=self.head
        while current!=None:
            print(current.value,end="-->")
            current=current.next
class stackApplication:
    """Class that works with stack Application(some most Important Application of the stack)
    """
    def preOrderPrint(self,array,root):
        """Traverse the array or list by assuming as tree.where index=0 is the root element
           equivalent with tree preorder traversal.
           params:index of the root
           return:None if linkedlist contains no elements and not correct root index.
        """
        stack=[root]
        while stack:
            current=stack.pop()
            print(array[current],end="-->")
            if current*2+2<len(array):
                stack.append(current*2+2)
            if current*2+2<len(array):
                stack.append(current*2+1)
    def postOrderPrint(self,array,root=0):
        """Traverse the array or list by assuming as tree.where index=0 is the root element
           equivalent with tree postOrder traversal.
           params:index of the root
           return:None if linkedlist contains no elements and not correct root index.
        """
        stack=[]
        current=root
        while stack or current<len(stack):
            while current<len(stack):
                stack.append(current)
                if current*2+2<len(array):
                    stack.append(None)
                current=current*2+1
            if stack:
                temp=stack.pop()
                if temp is not None:
                    print(array[temp],end="-->")
                else:
                    temp=stack.pop()
                    stack.append(temp)
                    current=temp*2+2
    def inOrderPrint(self,array,root):
        """Traverse the array or list by assuming as tree.where index=0 is the root element
           equivalent with tree Inorder.
           params:index of the root
           return:None if linkedlist contains no elements and not correct root index.
        """
        stack=[]
        current=root
        while stack or current<len(array):
            while current<len(stack):
                stack.append(current)
                current=current*2+1
            if stack:
                temp=stack.pop()
                print(array[temp],end="-->")
                current=temp*2+2
    def reverseDataUsingStack(self,array):
        """reverse the natural order of element of GivenData using Stack .
           params:array
           return:reversed array
        """
        stack=[]
        for e in array:
            stack.append(e)
        list=[]
        while stack:
            list.append(stack.pop())
        return list
    def validateParenthsis(self,data):
        """validate if given parenthsis is in correct order(correct openning with correct closing
           params:data
           return:True if the order is valid else False.
        """
        possibleData=["(",")","{","}","[","]"]
        mapOfData={"(":")","{":"}","[":"]"}
        givenData="";tempData="";stack=[]
        for e in data:
            if e in possibleData:
                tempData+=e
        for parenthsis in tempData:
            if parenthsis in mapOfData:
                stack.append(mapOfData[parenthsis])
            else:
                if len(stack)==0 or stack.pop()!=parenthsis:
                    return False
        return True if len(stack)==0 else False








