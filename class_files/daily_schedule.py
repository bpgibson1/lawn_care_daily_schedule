"""
**************************************************************
Name        : daily_schedule.py
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
from class_files.priority_queue import PriorityQueue
from datetime import date


class DailySchedule:

    def __init__(self):
        self.customer_priority_queue = PriorityQueue()
        self.today = date.today()
        self._taxes = 0.07
        self._surcharge = 10

    def add_customer(self, customer_obj):
        # calculate and set priority
        yard_priority = 'E'
        for iteration in range(customer_obj.yards_queue.size()):
            yard = customer_obj.yards_queue.find_at(iteration)
            if yard.priority is None:
                yard.calculate_total()
            if self.customer_priority_queue.alpha_priority[yard_priority] > self.customer_priority_queue.alpha_priority[yard.priority]:
                yard_priority = yard.priority
        # call queue add
        self.customer_priority_queue.add(customer_obj, yard_priority)

    def print_invoice(self):
        pass

    def sort_customer(self):
        pass

    def print_schedule(self):
        pass
