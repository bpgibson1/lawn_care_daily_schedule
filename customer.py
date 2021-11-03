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
from queue import Queue


class Customer:

    def __init__(self):
        self.name = ""
        self.address = ""
        self.phone_num = ""
        self.yards_queue = Queue()

    def set_yard(self, item):
        self.yards_queue.enqueue(item)
