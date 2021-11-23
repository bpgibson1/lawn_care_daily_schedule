"""
**************************************************************
Name        : queue.py
Author      : Bryner Gibson
Created     : 20211102
Course      : CIS 152 Data Structures
Version     : 1.0
OS          : Windows 10
Copyright   : This is my own original work based on               
              specifications issued by our instructor
Description : This program overall description here
              Input:  list and describe
              Output: list and describe
Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or 
unmodified. I have not given other fellow student(s) access to
my program.         
***************************************************************
"""
import collections
from exceptions.QueueEmptyException import QueueEmptyException


class Queue:
    def __init__(self):
        self.head = -1
        self.tail = -1
        self.items = collections.deque()

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.head = 0
        self.tail += 1
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            self.tail -= 1
            return self.items.popleft()
        else:
            raise QueueEmptyException

    def peek(self):
        if not self.is_empty():
            first_item = self.items.popleft()
            self.items.append(first_item)
            return first_item
        raise QueueEmptyException

    def find_at(self, index):
        if 0 <= index <= self.size():
            return self.items[index]
        else:
            return None

    def swap(self, a_index, b_index):
        if 0 <= a_index <= self.size() and 0 <= b_index <= self.size() and a_index != b_index:
            self.items[a_index], self.items[b_index] = self.items[b_index], self.items[a_index]

    def size(self):
        count = 0
        for item in self.items:
            count += 1
        return count

