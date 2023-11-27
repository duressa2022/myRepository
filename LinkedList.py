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
class Node:
    """Class that create node object for linkedlist
    """
    def __init__(self, value):
        """constructor for Node and it has parameters and intialize the
            following variables.
            prev:pointer to previous node of current node.
            next:pointer to next node of current node.
            value:value that stored in the Node.
        """
        self.value = value
        self.prev = None
        self.next = None
class LinkedList:
    """Class that create doublely linkelist object implements basic opreation on linkedlist
    """
    def __init__(self):
        """constructor for linkedlist and it doesn't hava any parameter and intilize the
           following variables.
           first:head of linkedlist.
            last: tail of the linkedlist.
            size:size of the linkedlist
        """
        self.first=None
        self.last=None
        self.size=0
    def addFirst(self,e):
        """This method create new Node object then if the first node element
         is none directly assign the node into the first node else links the
         new node with the first node make the new node the first node.
         params: e
         No return"""
        newNode=Node(e)
        if self.first==None:
            self.first=newNode
            self.last=newNode
        else:
            newNode.next=self.first
            self.first.prev=newNode
            self.first=newNode
        self.size+=1
    def addLast(self,e):
        """This method create new Node object then if the first node element
           is none directly assign the node into the first node else links the
           new last node with the new Node,make the new node the last node.
           params: e
           No return """
        newNode=Node(e)
        if self.first==None:
            self.first=newNode
            self.last=newNode
        else:
            self.last.next=newNode
            newNode.prev=self.last
            self.last=newNode
        self.size+=1
    def removeFirst(self):
        """This method return None  if the first node element
            else removes the first node from the list by removing
            links between the first and the next node and return
            its value
            params: None
            return: item """
        if self.first==None:
            return None
        temp=self.first
        temp.next.prev=None
        self.first=self.first.next
        value=temp.value
        del temp
        self.size-=1
        return value
    def removeLast(self):
        """This method return None  if the first node element
           else removes the last node from the list by removing
            link between the last and its previous node and return
            its value.
            params: None
            return: item """
        if self.last==None:
            return None
        temp=self.last
        temp.prev.next=None
        self.last=temp.prev
        temp.prev=None
        value=temp.value
        del temp
        self.size-=1
        return value
    def contains(self,e):
        """Checks whether the list contains element e or not
           params:e (as input)
           return:True if it contains else False
        """
        return True if self.indexOf(e)>=0 and self.indexOf(e)<self.size else False
    def getFirst(self):
        """Returns value of the first node else if the list is empty return none.
           params:None
           return:value of last node
        """
        return self.first.value if self.first!=None else None
    def getLast(self):
        """Returns value of the last node else if the list is empty return none.
           params:None
           return:value of the first node
        """
        return self.last.value if self.first!=None else None
    def length(self):
        """Returns length of the list(linkedlist) by counting the number of element.
           params:None
           return:length of the linkedlist
        """
        return  self.size
    def add(self,e):
        """Appends the element e into the list(linkedlist) equivalent with addLast method
           params:None
           return:None
        """
        self.addLast(e)
    def remove(self,e):
        """Removes the first occurence of  element e from the list(linkedlist) and return True
           if the element e is removed from the list(linkedlist)
           params:e
           return:True if element e is removed from the list else False
        """
        if self.first.next==None or self.first.value==e:
            if self.first.value==e:
                self.removeFirst()
                return True
        else:
            cur=self.first.next
            while cur.next!=None:
                if cur.value==e:
                    cur.prev.next=cur.next
                    cur.next.prev=cur.prev
                    return True
                cur=cur.next
            if cur.next==None:
                if cur.value==e:
                    self.removeLast()
                    return True
        return False


    def addAll(self,collection):
        """Appends all elements of collection such as list or array,tuple,set
            or string into list or linkedlist.
           params:collection
           return:None
        """
        for e in collection:
            self.addLast(e)
        self.size+=len(collection)
    def addAllAt(self,index,collection):
        currentIndex=index
        for e in collection:
            self.addAt(currentIndex,e)
            currentIndex+=1
    def clear(self):
        """Removes every element from  the list(linkedlist) after calling of this
           the list will be empty.
            params:None
            return:True if clearing operation is done else False
         """
        if self.first!=None:
            cur=self.first
            while cur!=None:
                next=cur.next
                cur.prev=None
                cur.next=None
                cur=next
            self.first=self.last=None
            self.size=0
            return True
        else:
            return False
    def get(self,pos):
        """Returns element  at specified position or index
           params:pos or index of the element
           return: value of element at specified index or pos
        """
        cur=self.first
        index=0
        while cur!=None and index!=pos:
            index+=1
            cur=cur.next
        if cur!=None:
            return cur.value
        else:
            return None
    def set(self,pos,e):
        """Replace element  at specified position or index with e.
           params:pos or index of the element and element e
           return:the ald value or replaced value otherwise None
        """
        cur=self.first
        index=0
        while cur!=None and index!=pos:
            index+=1
            cur=cur.next
        if cur!=None:
            oldValue=cur.value
            cur.value=e
            return oldValue
        else:
            return None
    def addAt(self,pos,e):
        """Add element e at specified position or index.
           params:pos or index of the element and element e
           return:True if the element is succesfully added into the list
        """
        newNode=Node(e)
        cur=self.first
        index=0
        if pos==0 or self.first==None:
            self.addFirst(e)
            return True
        else:
            while cur!=None and index!=pos:
                index+=1
                cur=cur.next
            if cur.next==None or cur!=None:
                cur.prev.next=newNode
                newNode.prev=cur.prev
                cur.prev=newNode
                newNode.next=cur
                return True
        return False
    def removeAt(self,pos):
        """Remove element from  specified position or index.
           params:pos or index of the element
           return:Element at specified position before removal
        """
        cur=self.first
        index=0
        if pos==0 and self.first!=None:
            item=self.first.value
            self.removeFirst()
            return  item
        else:
            while index!=pos and cur!=None:
                index+=1
                cur=cur.next
            if cur!=None:
                if cur.next!=None:
                    item=cur.value
                    cur.prev.next=cur.next
                    cur.next.prev=cur.prev
                    self.size-=1
                    return item
                else:
                    if cur.next==None:
                        item=cur.value
                        self.removeLast()
                        return item
            else:
                return None

    def isElementIndex(self,index):
        """Tell wether given index is an index of list or not.
           params:pos or index of the element.
           return:True if specified index is correct index"""
        return True if index>=0 and index<self.size else False
    def isPositionIndex(self,index):
        """Tell wether given index is a position of list at which element is inserted or not.
           params:pos or index of the element.
           return:True if specified index or position is correct index or position"""
        return True if index>=0 and index<=self.size else False
    def getNode(self,index):
        """Returns Node at specified position or index.
           params:pos or index of the element
           return:Node at specified position or index or None
        """
        cur=self.first
        i=0
        while cur!=None and i!=index:
            i=i+1
            cur=cur.next
        if cur==None:
            return None
        else:
            return cur
    def indexOf(self,e):
        """Returns the index of the first occurrence of element e.
           params:e
           return:index of the first occurrence of Element e otherwise -1
        """
        cur=self.first
        index=0
        while cur!=None:
            if cur.value==e:
                return index
            cur=cur.next
            index+=1
        if cur==None:
            return -1
    def lastIndexOf(self,e):
        """Returns the index of the last occurrence of element e.
           params:e
           return:index of the last occurrence of Element e otherwise -1
        """
        cur=self.last
        index=self.size-1
        while cur!=None:
            if cur.value==e:
                return index
            cur=cur.prev
            index-=1
        if cur==None:
            return -1
    def peek(self):
        """Return without removing the first  element of the list(linkedlist).
           params:None
           return:The first element of the list or None if the list is empty
        """
        return self.first.value if self.first!=None else None
    def element(self):
        """Return without removing the first  element of the list(linkedlist).
           params:None
           return:The first element of the list or None if the list is empty
        """
        return self.getFirst()
    def poll(self):
        """Return and removes the first  element of the list(linkedlist).
           params:None
           return:The first element of the list or None if the list is empty
        """
        if self.first!=None:
            return None
        else:
            item=self.first.value
            self.removeFirst()
            return item
    def offer(self,e):
        """Adds the specified element at the end of the list(linkedlist).
           params:e
           return:None
        """
        self.add(e)
    def peekFirst(self):
        """Return but without removing the first  element of the list(linkedlist).
           params:None
           return:The first element of the list or None if the list is empty
        """
        return self.first.value if self.first!=None else None
    def peekLast(self):
        """Return the last element of but without removing from the list(linkedlist).
           params:None
           return:The last element of the list or None if the list is empty
        """
        return self.last.value if self.first!=None else None
    def pollFirst(self):
        """Return and removes the first  element of the list(linkedlist).
           params:None
           return:The first element of the list or None if the list is empty
        """
        return self.removeFirst() if self.first!=None else None
    def pollLast(self):
        """Return and removes the lasr element of the list(linkedlist).
            params:None
            return:The last element of the list or None if the list is empty
        """
        return self.removeLast() if self.last!=None else None
    def push(self,e):
        """Pushes the element into the stack that is represented by the list.
           params:e
           return:None
        """
        self.add(e)
    def pop(self):
        """Pops element from top of  the stack, that represented by the list.
           params:e
           return:element from the stack
           """
        return self.removeFirst()
    def removeFirstOccurence(self,e):
        """Removes first occured element e from the list or linkedlist.
           params:e
           return:None
        """
        self.remove(e)
    def removeLastOccurence(self,e):
        """Removes last occured element e from the list or linkedlist.
           params:e
           return:True if the element is succesfully removed.
        """
        cur=self.last
        while cur.prev!=None:
            if cur.value==e:
                cur.prev.next=cur.next
                cur.next.prev=cur.prev
                return True
            cur=cur.prev
        if cur.prev==None:
            self.removeFirst()
            return True
        self.size-=1
        return False
    def hasNext(self,index):
        """Returns True if element at specified index has next that is not None.
           if the next is None the method returns False
            params:index
            return:True if element at specified index has next else False
        """
        return True if index>=0 and index<self.size-1 else False
    def getNext(self,index):
        """Returns element  next to the specified index
           params:index
           return:element next to the specified index else None
        """
        return self.get(index+1) if index+1>=0 and index+1<self.size else None
    def hasPrevious(self,index):
        """Returns True if element at specified index has previous element that is not None.
           if the previous element  is None the method returns False
           params:index
           return:True if element at specified index has previous else False
        """
        return True if index-1>=0 and index-1<self.size else False
    def getPrevious(self):
        """Returns element previous to the specified index
           params:index
           return:element previous to the specified index else None
        """
        return self.get(index-1) if index-1>=0 and index-1<size else False
    def nextIndex(self,index):
        """Returns index of next element that is specified by given index
           params:index
           return:index next to specified index else None
        """
        return  index+1 if index+1>=0 and index+1<self.size else None
    def previousIndex(self):
        """Returns index of previous element that is specified by given index
           params:index
           return:index pervious to specified index else None
        """
        return index-1 if index-1>=0 and index-1<self.size else None
    def clone(self):
        """Clone the element of list or linkedlist into other list and returns new list.
           params:None
           return:new linkedlist that is cloned from old list
        """
        if self.first==None:
            return None
        clone=LinkedList()
        clone.first=None
        clone.last=None
        clone.size=None
        cur=self.first
        while cur!=None:
            clone.add(cur.value)
            cur=cur.next
        return clone
    def toArray(self):
        """Convert element of linkedlist into array or python list and return created array.
           params:None
           return:array that is populated by element of linkedlist
        """
        if self.first==None:
            return None
        cur=self.first
        array=[]
        while cur!=None:
            array.append(cur.value)
            cur=cur.next
        return array
    def toString(self):
        """Convert element of linkedlist into string or python string and return created string.
           params:None
           return:string that contains element of linkedlist as its character.
        """
        if self.first==None:
            return None
        cur=self.first
        string=""
        while cur!=None:
            string+=cur.value
            cur=cur.next
        return string
    def printFromLeft(self):
        """Print element of linkedlist from left to right.
           params:None
           return:None if the list is empty
        """
        cur=self.first
        while cur!=None:
            print(cur.value,end="-->")
            cur=cur.next
        if self.first==None:
            return None
    def printFromRight(self):
        """Print element of linkedlist from right to left.
           params:None
           return:None if the list is empty
        """
        cur=self.last
        while cur!=None:
            print(cur.value,end="--->")
            cur=cur.prev
        if self.first==None:
            return None
    def reverse(self):
        """reverse the natural order of element of linkedlist.
           params:None
           return:head of the reversed linkedlist
        """
        cur=self.first
        pre=None
        while cur!=None:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
        self.first=pre
        return pre
    def partition(self,low,high):
        """partition the linkedlist by choosing the pivot from the end of the list
           and put into position suchthat any element lessthan the pivot is to the left
           side of the list or linkedlist.
           params:low(initial pos) and high(final position)
           return:index of the pivot after partition
         """
        pivot=self.get(high)
        i=low-1
        for j in range(low,high):
            if self.get(j)<pivot:
                i+=1
                temp=self.get(i)
                self.set(i,self.get(j))
                self.set(j,temp)
        temp=self.get(i+1)
        self.set(i+1,pivot)
        self.set(high,temp)
        return i+1
    def QuickSort(self,low,high):
        """sort the list or linkedlist by using wellknown Sorting  algorithem.sorts
           elements between low and high index
           params:low(initial pos) and high(final position)
           return:None if linkedlist contains no or one elements.
        """
        if low>=high or self.first==None:
            return None
        i=self.partition(low,high)
        self.QuickSort(low,i-1)
        self.QuickSort(i+1,high)
    def binarySearch(self,key,low,high,sorted=True):
        """search key in list or linkedlist by using wellknown searching  algorithem.searches
           elements between low and high index
           params:low(initial pos), high(final position),key to search and sorted value if
                  is already sorted
           return:None if linkedlist contains no elements.
        """
        if sorted==False:
            self.QuickSort(low,high)
        if self.first==None:
            return -1
        while low<=high:
            mid=(low+high)//2
            if self.get(mid)==key:
                return mid
            elif self.get(mid)<key:
                low=mid+1
            else:
                high=mid-1
        return -1
    def preOrderPrint(self,index=0):
        """Traverse the linkedlist or list by assuming as tree.where index=0 is the root element
           equivalent with tree preorder traversal.
           params:index of the root
           return:None if linkedlist contains no elements and not correct root index.
         """
        if self.first==None or index>=self.size:
            return None
        stack=[index]
        while stack:
            cur=stack.pop()
            print(self.get(cur),end="-->")
            if cur*2+2<self.size and self.get(cur*2+1)!=None:
                stack.append(cur*2+1)
            if cur*2+1<self.size and self.get(cur*2+2)!=None:
                stack.append(cur*2+2)

    def inOrderPrint(self,index=0):
        """Traverse the linkedlist or list by assuming as tree.where index=0 is the root element
           equivalent with tree Inorder.
           params:index of the root
           return:None if linkedlist contains no elements and not correct root index.
        """
        if self.first==None or index>=self.size:
            return None
        stack=[]
        cur=index
        while stack or cur<self.size:
            while cur<self.size and self.get(cur)!=None:
                stack.append(cur)
                cur=cur*2+1
            if len(stack)>0:
                temp=stack.pop()
                print(self.get(temp),end="-->")
                cur=temp*2+2
    def postOrderPrint(self,index=0):
        """Traverse the linkedlist or list by assuming as tree.where index=0 is the root element
           equivalent with tree postOrder traversal.
           params:index of the root
           return:None if linkedlist contains no elements and not correct root index.
        """
        if self.first==None or index>=self.size:
            return None
        stack=[]
        cur=index
        while stack or cur<self.size:
            while cur<self.size and self.get(cur):
                stack.append(cur)
                if self.get(cur*2+2)!=None:
                    stack.append(None)
                cur=cur*2+1
            if stack:
                temp=stack.pop()
                if temp!=None:
                    print(self.get(temp),end="-->");
                else:
                    temp=stack.pop()
                    stack.append(temp)
                    cur=temp*2+2
    def breadthFirstPrint(self,index=0):
        """Traverse the linkedlist or list by assuming as tree.where index=0 is the root element
           equivalent with breath fist traversal of the tree.
           params:index of the root
           return:None if linkedlist contains no elements and not correct root index.
        """
        if self.first==None or index>=self.size:
            return None
        queue=[index]
        while queue:
            cur=queue.pop(0)
            print(cur,end="-->")
            if cur*2+2<self.size and self.get(cur*2+2)!=None:
                queue.append(cur*2+2)
            if cur*2+1<self.size and self.get(cur*2+1)!=None:
                queue.append(cur*2+1)
    def getMax(self):
        """Find the maximum element from the linkedlist or list.
           params:None
           return:max value from linkedlist or None
        """
        if self.first==None:
            return None
        cur=self.first
        maxVal=-float("inf")
        while cur!=None:
            if cur.value>maxVal:
                maxVal=cur.value
            cur=cur.next
        return maxVal
    def getMin(self):
        """Find the minimum element from the linkedlist or list.
           params:None
           return:min value from linkedlist or None
        """
        if self.first==None:
            return None
        cur=self.first
        minVal=float("inf")
        while cur!=None:
            if cur.value<minVal:
                minVal=cur
            cur=cur.next
        return minVal
    def getMaxBetween(self,low,high):
        """Find the maximum element from the linkedlist or list between low and high index
           inclusive.
           params:lower and higher index which indicate the interval.
           return:max value from linkedlist or None
        """
        if low>=high or self.first==None:
            return None
        cur=low
        last=high+1
        maxVal=-float("inf")
        while cur!=last:
            if maxVal<self.get(cur):
                maxVal=self.get(cur)
            cur+=1
        return maxVal
    def getMinbetween(self,low,high):
        """Find the minimum element from the linkedlist or list between low and high index
           inclusive.
           params:lower and higher index which indicate the interval.
           return:min value from linkedlist or None
        """
        if low>=high or self.first==None:
            return None
        cur=low
        last=high+1
        minVal=float("inf")
        while cur!=last:
            if minVal>self.get(cur):
                minVal=self.get(cur)
            cur+=1
        return minVal























