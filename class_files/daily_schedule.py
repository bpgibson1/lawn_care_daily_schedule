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
import uuid

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
        total = 0
        working_dir = os.path.dirname(__file__)
        schedule_name = ('../output_files/schedule/' + 'daily_schedule' + "_" + self.today + '.txt').replace(" ", "_")
        schedule_path = os.path.join(working_dir, schedule_name)
        schedule_file = open(schedule_path, 'w')

        for iteration in range(self.customer_priority_queue.size()):
            invoice_id = uuid.uuid4()
            node = self.customer_priority_queue.remove()
            invoice_name = '../output_files/invoice/' + (node.customer.name + "_" + self.today + '.txt').replace(" ", "_")
            invoice_path = os.path.join(working_dir, invoice_name)
            invoice_file = open(invoice_path, 'w')
            invoice_file.write("~~~~~~~~~~~~~~~~~~Customer Copy~~~~~~~~~~~~~~~~~~~\n")
            invoice_file.write("Invoice Id: {}\n".format(invoice_id))
            invoice_file.write("Customer: {}\n".format(node.customer.name))
            invoice_file.write("Eamil: {}\n".format(node.customer.email))
            invoice_file.write("Phone Number: {}\n".format(node.customer.phone_num))
            invoice_file.write("\n")
            invoice_file.write("~~~~~~~~~~~~~~~~~Yard Information~~~~~~~~~~~~~~~~~\n")
            for index in range(node.customer.yards_queue.size()):
                yard = node.customer.yards_queue.find_at(index)
                self.print_schedule(schedule_file, invoice_id, iteration + index + 1, node.customer, yard)
                invoice_file.write("Yard: {}\n".format(yard.yard_name))
                invoice_file.write("Location: {}\n".format(yard.address))
                if yard.fee_flag == 1:
                    invoice_file.write("1 @ ${}\n".format(yard.get_flat_fee()))
                else:
                    invoice_file.write("{}sqft @ ${}\n".format(yard.square_footage, yard.price_per_square_foot))
                invoice_file.write("Yard Subtotal: ${}\n".format(yard.total_price))
                total += yard.total_price
                invoice_file.write("--------------------------------------------------\n")

            tax = total - total * self._taxes
            invoice_file.write("Tax: {} @ ${} = ${}\n".format(total, self._taxes, tax))
            surcharge = node.customer.yards_queue.size() * self._surcharge
            invoice_file.write("Surcharge: {} @ ${} = ${}\n".format(node.customer.yards_queue.size(), self._surcharge, surcharge))
            invoice_file.write("--------------------------------------------------\n")
            total_due = total + tax + surcharge
            invoice_file.write("TOTAL DUE: ${}\n".format(total_due))
            invoice_file.write("I agree to pay the total indicated on this invoice\n")
            invoice_file.write("Invoice will be due at the time of service\n")
            invoice_file.close()

    def print_schedule(self, file, i_id, completed, customer, yard):
        file.write('----------------------Customer----------------------\n')
        file.write('Invoice Id: {} \n'.format(i_id))
        file.write('Needs Completed: {}\n'.format(completed))
        file.write("Customer: {}\n".format(customer.name))
        file.write("Eamil: {}\n".format(customer.email))
        file.write("Phone Number: {}\n\n".format(customer.phone_num))
        file.write('Yard Address: {}\n'.format(yard.address))
        file.write('Yard Size: {}\n'.format(yard.square_footage))



    def sort_customer(self):
        pass


# if __name__ == '__main__':
#     c = Customer()
#     c.name = "Bryner Gibson"
#     y = Yard()
#     y.square_footage = 1250
#     y.total_price = y.calculate_total()
#     c.set_yard(y)
#
#     ds = DailySchedule()
#     ds.add_customer(c)
#
#     ds.print_invoice()
