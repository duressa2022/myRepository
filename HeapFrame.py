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
class maxHeap:
    """Class that create Array based maxheap(using list to simulate Array) object implements
       basic opreation on maxheap
    """
    def __init__(self):
       """constructor for maxheap and it doesnt have any hava any parameter and intilize the
          following variable.
          list:python list.
        """
       self.array=[]
    def heapfiy(self,index):
        """This method assumes that every element above index of heap except at index are on their correct position
            therefore try to put element at index=index to its correct position.
           params:index of incorrect position.
           return:None
        """
        left=index*2+1
        right=index*2+2
        largest=index
        if left<len(self.array) and self.array[left]>self.array[largest]:
            largest=left
        if right<len(self.array) and self.array[right]>self.array[largest]:
            largest=right
        if index!=largest:
            (self.array[index],self.array[largest])=(self.array[largest],self.array[index])
            self.heapfiy(largest)
    def bottomUp(self,fromWhere):
        """This method assumes that every element below index=index of heap are on their correct position
           therefore try to put element at index=index to its correct position.
           params:index of incorrect position.
           return:None
        """
        if len(self.array)<0:
            raise Exception("EMPTY HEAP...")
        index=fromWhere
        while index>=0 and self.array[index]>self.array[index//2]:
            (self.array[index],self.array[index//2])=(self.array[index//2],self.array[index])
            index=index//2
    def heapPush(self,e):
        """Insert element e in to the heap ana heapfiy the heap inorder to make sure e is on its correct position.
          :param e:
          :return: None
        """
        if len(self.array)<0:
            self.array.append(e)
            return None
        index=len(self.array)
        self.array.append(e)
        self.bottomUp(index)
    def heapPop(self):
        """remove and return the element on the top of the heap and heapfiy .
           :param e:
           :return: removed item
        """
        if len(self.array)<0:
            raise Exception("REMOVING FROM EMPTY HEAP...")
        item=self.array[0]
        self.array[0]=self.array[len(self.array)-1]
        self.array.pop()
        self.heapfiy(0)
        return item
    def increaseKey(self,key,index):
        """increase value of given index and heapfiy to keep the heap property of the tree.
           :param key,index:
           :return: None
        """
        if self.array[index]>key:
            raise Exception("ALREADY MAXIMUM ELEMENT AT {}".format(index))
        self.array[index]=key
        self.bottomUp(index)
    def decreaseKey(self,key,index):
        """decrease value of given index and heapfiy to keep the heap property of the tree.
           :param key,index:
           :return: None
        """
        if self.array[index]<key:
            raise Exception("ALREADY MINIMUM ELEMENT AT {}".format(index))
        self.array[index]=key
        self.heapfiy(index)
    def getMax(self):
        """return the maximum  element from the heap(element on the top of the tree) .
           :param :None
           :return: max value of array
        """
        if len(self.array)<0:
            raise Exception("EMPTY HEAP....")
        return self.array[0]

class minHeap:
    """Class that create Array based maxheap(using list to simulate Array) object implements
       basic opreation on maxheap
    """
    def __init__(self):
        """constructor for maxheap and it doesnt have any hava any parameter and intilize the
           following variable.
           list:python list.
        """
        self.array=[]
    def heapfiy(self,index):
        """This method assumes that every element above index of heap except at index are on their correct position
           therefore try to put element at index=index to its correct position.
           params:index of incorrect position.
           return:None
        """
        left=index*2+1
        right=index*2+2
        smallest=index
        if left<len(self.array) and self.array[left]<self.array[smallest]:
            smallest=left
        if right<len(self.array) and self.array[right]<self.array[smallest]:
            smallest=right
        if index!=smallest:
            (self.array[index],self.array[smallest])=(self.array[smallest],self.array[index])
            self.heapfiy(smallest)

    def bottomUp(self, fromWhere):
        """This method assumes that every element below index=index of heap are on their correct position
           therefore try to put element at index=index to its correct position.
           params:index of incorrect position.
           return:None
        """
        if len(self.array)<0:
            raise Exception("EMPTY HEAP...")
        inde =fromWhere
        while index>=0 and self.array[index]<self.array[index // 2]:
            (self.array[index],self.array[index//2])=(self.array[index//2], self.array[index])
            index = index // 2
    def heapPush(self,e):
        """Insert element e in to the heap ana heapfiy the heap inorder to make sure e is on its correct position.
           :param e:
           :return: None
        """
        if len(self.array)<0:
            self.array.append(e)
            return None
        index=len(self.array)
        self.array.append(e)
        self.bottomUp(index)
    def heapPop(self):
        """remove and return the element on the top of the heap and heapfiy .
           :param e:
           :return: removed item
        """
        if len(self.array)<0:
            raise Exception("REMOVING FROM EMPTY HEAP...")
        item=self.array[0]
        self.array[0]=self.array[len(self.array)-1]
        self.array.pop()
        self.heapfiy(0)
        return item
    def increaseKey(self,key,index):
        """increase value of given index and heapfiy to keep the heap property of the tree.
           :param key,index:
           :return: None
        """
        if self.array[index]>key:
            raise Exception("ALREADY MAXIMUM ELEMENT AT {}".format(index))
        self.array[index]=key
        self.heapfiy(index)
    def decreaseKey(self,key,index):
        """decrease value of given index and heapfiy to keep the heap property of the tree.
           :param key,index:
           :return: None
        """
        if self.array[index]<key:
            raise Exception("ALREADY MINIMUM ELEMENT AT {}".format(index))
        self.array[index]=key
        self.bottomUp(index)

    def getMin(self):
        """return the minimum  element from the heap(element on the top of the tree) .
           :param :None
           :return: min value of array
        """
        if len(self.array) < 0:
            raise Exception("EMPTY HEAP....")
        return self.array[0]
class heapApplication:
    def heapSort(self,array):
        pass
    def prims(self,graph):
        pass
    def djiskatra(self,graph):
        pass
