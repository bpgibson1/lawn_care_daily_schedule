"""
**************************************************************
Name        : priority_queue.py
Author      : Bryner Gibson
Created     : 10/20/2021
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
TURNED IN LATE DUE TO MILITARY OBLIGATIONS; COMMUNICATED DURING
PRIOR CONVERSATION OVER EMAIL
***************************************************************
"""
from module_6.list_based_queue.QueueEmptyException import QueueEmptyException
from module_6.list_based_queue.QueueFullException import QueueFullException
import collections


class Node:

    def __init__(self, data, priority):
        self.job_num = data
        self.priority = priority


class PriorityQueue:

    def __init__(self):
        self.head = -1
        self.tail = -1
        self.alpha_priority = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
        self.items = collections.deque()

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return False

    def add(self, item, priority):
        self.head = 0
        if not self.is_full():
            self.tail += 1
            new_node = Node(item, priority)
            if self.is_empty():
                self.items.append(new_node)
                return
            self.items.append(new_node)
            sorting = True
            while sorting:
                sorting = False
                for index in range(len(self.items) - 1):
                    if self.alpha_priority[self.items[index].priority] > self.alpha_priority[self.items[index + 1].priority]:
                        swap = self.items[index]
                        self.items[index] = self.items[index + 1]
                        self.items[index + 1] = swap
                        sorting = True
        else:
            raise QueueFullException

    def remove(self):
        if not self.is_empty():
            self.tail -= 1
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
                queue_str += 'Priority: {} Item: {}\n'.format(item.priority, item.job_num)
            return queue_str
        return "Queue is Empty"


if __name__ == '__main__':
    pn = PriorityQueue()
    pn.add("2365", "B")
    pn.add("2785", "B")
    pn.add("9875", "B")
    pn.add("6995", "D")
    pn.add("7995", "D")
    pn.add("3591", "D")
    pn.add("7853", "D")
    pn.add("4632", "A")
    pn.add("1973", "A")

    print(pn.print_())
