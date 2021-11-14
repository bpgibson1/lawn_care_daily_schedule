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
from customer import Customer
from yard import Yard


class Application:

    def __init__(self, main_window=None):
        self.mw = main_window
        self.nw = None
        self.name_input = Entry(self.mw)
        self.address_input = Entry(self.mw)
        self.number_input = Entry(self.mw)
        self.yard_name_input = None
        self.size_input = None
        self.customer_name = ""
        self.customer_objs = []
        self.current_c_added = False

    def exit_yard(self):
        self.current_c_added = False
        self.nw.destroy()

    def create_new_yard(self):
        # Create the customer unless it exists
        if not self.current_c_added:
            self.create_new_customer()
            self.current_c_added = True
        y = Yard(self.yard_name_input.get(), self.size_input.get())
        self.customer_objs[len(self.customer_objs) - 1].yards_queue.enqueue(y)

        # set fields back to empty

    def create_new_customer(self):
        self.customer_name = self.name_input.get()

        # create customer object and append it onto the list
        c = Customer(self.name_input.get(), self.address_input.get(), self.number_input.get())
        self.customer_objs.append(c)
        print([obj.name for obj in self.customer_objs])
        # Reset the fields
        self.name_input.delete('0', 'end')
        self.address_input.delete('0', 'end')
        self.number_input.delete('0', 'end')

    def build_yard(self):
        self.nw = Toplevel(self.mw)
        self.nw.title("Lawn Care Daily Schedule")
        self.nw.geometry('500x300')
        self.nw.configure(background='#eee8d5')

        title_label = Label(self.nw, text='Enter Yard: Customer:' + self.customer_name, bg='#eee8d5', font=('Lucida Console', 12, 'bold'))
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


def main():
    mw = Tk()
    application = Application(mw)
    application.build()
    mw.mainloop()


if __name__ == '__main__':
    main()
