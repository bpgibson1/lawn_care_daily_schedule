"""
**************************************************************
Name        : customer.py
Author      : Bryner Gibson
Created     : 20211101
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
from class_files.queue import Queue
from class_files.yard import Yard


class Customer:

    def __init__(self, name="", email="", number=""):
        self.name = name
        self.email = email
        self.phone_num = number
        self.yards_queue = Queue()

    def set_yard(self, item):
        self.yards_queue.enqueue(item)

    def sort_yard(self):
        if self.yards_queue.size() < 2:
            return
        for index in range(self.yards_queue.size()):
            min_index = index
            for j in range(index+1, self.yards_queue.size()):
                if self.yards_queue.find_at(min_index).square_footage < self.yards_queue.find_at(j).square_footage:
                    min_index = j
            self.yards_queue.swap(min_index, index)


if __name__ == '__main__':
    c = Customer()
    y1 = Yard("", 450)
    # y2 = Yard("", 350)
    # y3 = Yard("", 250)
    # y4 = Yard("", 1250)
    # c.set_yard(y1)
    # c.set_yard(y2)
    # c.set_yard(y3)
    c.set_yard(y1)

    print(c.yards_queue.size())
    for yard in c.yards_queue.items:
        print(yard.square_footage)

    c.sort_yard()

    print(c.yards_queue.size())
    for yard in c.yards_queue.items:
        print(yard.square_footage)


