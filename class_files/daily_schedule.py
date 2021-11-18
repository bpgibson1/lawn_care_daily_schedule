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
from class_files.customer import Customer
from class_files.priority_queue import PriorityQueue
from datetime import date
import os

from class_files.yard import Yard


class DailySchedule:

    def __init__(self):
        self.customer_priority_queue = PriorityQueue()
        self.today = date.today().strftime("%B %d, %Y").replace(",", "")
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
        working_dir = os.path.dirname(__file__)
        for iteration in range(self.customer_priority_queue.size()):
            node = self.customer_priority_queue.remove()
            file_name = '../output_files/invoice/' + (node.customer.name + "_" + self.today + '.txt').replace(" ", "_")
            abs_path = os.path.join(working_dir, file_name)
            invoice_file = open(abs_path, 'x')
            invoice_file.write("~~~~~~~~~~~~~~~~~~Customer Copy~~~~~~~~~~~~~~~~~~")
            invoice_file.write("Customer: {}".format(node.customer.name))
            invoice_file.write("Eamil: {}".format(node.customer.email))
            invoice_file.write("Phone Number: {}".format(node.customer.number))
            invoice_file.write("")
            for index in node.customer.yards_queue.size():
                yard = node.customer.yards_queue.find_at(index)
                invoice_file.write("Yard: {}".format(yard.yard_name))
            invoice_file.close()

    def print_schedule(self):
        pass
    def sort_customer(self):
        pass


if __name__ == '__main__':
    c = Customer()
    c.name = "Bryner Gibson"
    y = Yard()
    y.square_footage = 1250
    c.set_yard(y)

    ds = DailySchedule()
    ds.add_customer(c)

    ds.print_invoice()
