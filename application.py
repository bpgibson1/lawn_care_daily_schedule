"""
**************************************************************
Name        : application.py
Author      : Bryner Gibson
Created     : 20211111
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
from tkinter import *
import re
from class_files.customer import Customer
from class_files.yard import Yard
from class_files.daily_schedule import DailySchedule


class Application:

    def __init__(self, main_window=None):
        self.mw = main_window
        self.name_input = Entry(self.mw)
        self.address_input = Entry(self.mw)
        self.number_input = Entry(self.mw)
        self.nw = None
        self.yard_name_input = None
        self.size_input = None
        self.customer_obj = None
        self.error_label = Label()
        self.daily_schedule = DailySchedule()

    def validate_main_window(self):
        self.error_label.destroy()
        self.error_label = Label(self.mw, text='', bg='#eee8d5', fg='#eb4034', font=('Lucida Console', 10, 'bold'))
        self.error_label.place(x=25, y=325)
        if self.name_input.get() == "":
            self.error_label.config(text='Please enter customer name')
            return False
        if self.address_input.get() == "":
            self.error_label.config(text='Please enter customer address')
            return False
        if self.number_input.get() != "":
            phone_re = '\w{3}-\w{3}-\w{4}'
            if not re.search(phone_re, self.number_input.get()):
                self.error_label.config(text='Incorrect number format (###-###-####)')
                return False
        else:
            self.error_label.config(text='Please enter customer phone number')
            return False
        return True

    def validate_yard_window(self):
        pass

    def exit_yard(self):
        # add to daily_schedule queue
        if self.customer_obj is not None:
            self.daily_schedule.add_customer(self.customer_obj)
        self.customer_obj = None
        self.nw.destroy()

    def create_new_yard(self):
        # Create the customer unless it exists
        if self.customer_obj is None:
            self.create_new_customer()
        y = Yard(self.yard_name_input.get(), self.size_input.get())
        y.total_price = y.calculate_total()
        self.customer_obj.set_yard(y)
        print(self.customer_obj.yards_queue.size())
        # set fields back to empty
        self.yard_name_input.delete('0', 'end')
        self.size_input.delete('0', 'end')

    def create_new_customer(self):

        # create customer object and append it onto the list
        c = Customer(self.name_input.get(), self.address_input.get(), self.number_input.get())
        self.customer_obj = c
        print(self.customer_obj.name)
        # Reset the fields
        self.name_input.delete('0', 'end')
        self.address_input.delete('0', 'end')
        self.number_input.delete('0', 'end')

    def build_yard(self):
        # add validation to ensure good input
        if not self.validate_main_window():
            return

        self.nw = Toplevel(self.mw)
        self.nw.title("Lawn Care Daily Schedule")
        self.nw.geometry('500x300')
        self.nw.configure(background='#eee8d5')

        customer_name = self.name_input.get()
        title_label = Label(self.nw, text='Enter Yard: Customer:' + customer_name, bg='#eee8d5', font=('Lucida Console', 12, 'bold'))
        title_label.place(x=25, y=25)

        yard_name_label = Label(self.nw, text='Yard Name:', bg='#eee8d5', font=('Lucida Console', 10, 'normal'))
        yard_name_label.place(x=25, y=75)

        self.yard_name_input = Entry(self.nw)
        self.yard_name_input.place(x=175, y=75)

        size_label = Label(self.nw, text='Square Footage:', bg='#eee8d5', font=('Lucida Console', 10, 'normal'))
        size_label.place(x=25, y=125)

        self.size_input = Entry(self.nw)
        self.size_input.place(x=175, y=125)

        exit_button = Button(self.nw, text='Exit', width=25, font=('Lucida Console', 10, 'normal'), command=self.exit_yard)
        exit_button.place(x=25, y=225)

        submit_button = Button(self.nw, text='Submit Yard', width=25, font=('Lucida Console', 10, 'normal'), command=self.create_new_yard)
        submit_button.place(x=270, y=225)

    def build(self):
        # build main window
        self.mw.title("Lawn Care Daily Schedule")
        self.mw.geometry('500x400')
        self.mw.configure(background='#eee8d5')

        title_label = Label(self.mw, text='Enter Customer Contact Info', bg='#eee8d5', font=('Lucida Console', 12, 'bold'))
        title_label.place(x=25, y=25)

        name_label = Label(self.mw, text='Name:', bg='#eee8d5', font=('Lucida Console', 10, 'normal'))
        name_label.place(x=25, y=75)

        self.name_input.place(x=175, y=75)

        address_label = Label(self.mw, text='Address:', bg='#eee8d5', font=('Lucida Console', 10, 'normal'))
        address_label.place(x=25, y=125)

        self.address_input.place(x=175, y=125)

        number_label = Label(self.mw, text='Phone Number:', bg='#eee8d5', font=('Lucida Console', 10, 'normal'))
        number_label.place(x=25, y=175)

        self.number_input.place(x=175, y=175)

        # add_yard_button = Button(self.mw, text='Add Yard', width=15, font=('Lucida Console', 10, 'normal'), command=self.build_yard)
        # add_yard_button.place(x=335, y=175)

        exit_button = Button(self.mw, text='Exit', width=25, font=('Lucida Console', 10, 'normal'), command=self.mw.destroy)
        exit_button.place(x=25, y=225)

        submit_button = Button(self.mw, text='Submit/Add yard', width=25, font=('Lucida Console', 10, 'normal'), command=self.build_yard)
        submit_button.place(x=270, y=225)

        invoice_button = Button(self.mw, text='Print Invoices', width=25, font=('Lucida Console', 10, 'normal'), command=None)
        invoice_button.place(x=25, y=275)

        schedule_button = Button(self.mw, text='Print Schedule', width=25, font=('Lucida Console', 10, 'normal'), command=None)
        schedule_button.place(x=270, y=275)


def main():
    mw = Tk()
    application = Application(mw)
    application.build()
    mw.mainloop()


if __name__ == '__main__':
    main()
