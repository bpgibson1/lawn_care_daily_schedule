"""
**************************************************************
Name        : priority_queue.py
Author      : Bryner Gibson
Created     : 20211114
Course      : CIS 152 Data Structures
Version     : 1.0
OS          : Windows 10
Copyright   : This is my own original work based on
              specifications issued by our instructor
Description : This program overall description here
              Input:  none
              Output: call queue order
Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or
unmodified. I have not given other fellow student(s) access to
my program.
***************************************************************
"""
from exceptions.QueueEmptyException import QueueEmptyException
from exceptions.QueueFullException import QueueFullException
import collections


class Node:

    def __init__(self, data, priority):
        self.customer = data
        self.priority = priority


class PriorityQueue:

    def __init__(self):
        self.alpha_priority = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
        self.items = collections.deque()

    def is_empty(self):
        return self.size() == 0

    def add(self, item, priority):
        new_node = Node(item, priority)
        if self.is_empty():
            self.items.append(new_node)
            return
        self.items.append(new_node)
        sorting = True
        while sorting:

            sorting = False
            for index in range(self.size() - 1):
                if self.alpha_priority[self.items[index].priority] > self.alpha_priority[self.items[index + 1].priority]:
                    swap = self.items[index]
                    self.items[index] = self.items[index + 1]
                    self.items[index + 1] = swap
                    sorting = True

    def remove(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise QueueEmptyException

    def peek(self):
        if not self.is_empty():
            first_item = self.items.popleft()
            self.items.appendleft(first_item)
            return first_item
        raise QueueEmptyException

    def size(self):
        count = 0
        for item in self.items:
            count += 1
        return count

    def print_(self):
        queue_str = ""
        if not self.is_empty():
            for item in self.items:
                queue_str += 'Priority: {} Item: {}\n'.format(item.priority, item.customer)
            return queue_str
        return "Queue is Empty"
