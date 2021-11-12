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

class Application:

    def __init__(self, main_window=None):
        self.mw = main_window

    def create_new_customer(self):
        pass

    def build_yard(self):
        nw = Toplevel(self.mw)
        nw.title("Lawn Care Daily Schedule")
        nw.geometry('500x300')
        nw.configure(background='#eee8d5')

        title_label = Label(nw, text='Enter Yard:', bg='#eee8d5', font=('Lucida Console', 12, 'bold'))
        title_label.place(x=25, y=25)

        yard_name_label = Label(nw, text='Name:', bg='#eee8d5', font=('Lucida Console', 10, 'normal'))
        yard_name_label.place(x=25, y=75)

        yard_name_input = Entry(nw)
        yard_name_input.place(x=175, y=75)

        size_label = Label(nw, text='Address:', bg='#eee8d5', font=('Lucida Console', 10, 'normal'))
        size_label.place(x=25, y=125)

        size_input = Entry(nw)
        size_input.place(x=175, y=125)

        exit_button = Button(nw, text='Exit', width=25, font=('Lucida Console', 10, 'normal'), command=nw.destroy)
        exit_button.place(x=25, y=225)

        add_yard_button = Button(nw, text='Add Yard', width=25, font=('Lucida Console', 10, 'normal'), command=self.build_yard)
        add_yard_button.place(x=270, y=225)


    def build(self):
        # build main window
        self.mw.title("Lawn Care Daily Schedule")
        self.mw.geometry('500x300')
        self.mw.configure(background='#eee8d5')

        title_label = Label(self.mw, text='Enter Customer Contact Info', bg='#eee8d5', font=('Lucida Console', 12, 'bold'))
        title_label.place(x=25, y=25)

        name_label = Label(self.mw, text='Name:', bg='#eee8d5', font=('Lucida Console', 10, 'normal'))
        name_label.place(x=25, y=75)

        name_input = Entry(self.mw)
        name_input.place(x=175, y=75)

        address_label = Label(self.mw, text='Address:', bg='#eee8d5', font=('Lucida Console', 10, 'normal'))
        address_label.place(x=25, y=125)

        address_input = Entry(self.mw)
        address_input.place(x=175, y=125)

        number_label = Label(self.mw, text='Phone Number:', bg='#eee8d5', font=('Lucida Console', 10, 'normal'))
        number_label.place(x=25, y=175)

        number_input = Entry(self.mw)
        number_input.place(x=175, y=175)

        exit_button = Button(self.mw, text='Exit', width=25, font=('Lucida Console', 10, 'normal'), command=self.mw.destroy)
        exit_button.place(x=25, y=225)

        add_yard_button = Button(self.mw, text='Add Yard', width=25, font=('Lucida Console', 10, 'normal'), command=self.build_yard)
        add_yard_button.place(x=270, y=225)


def main():
    mw = Tk()
    application = Application(mw)
    application.build()
    mw.mainloop()


if __name__ == '__main__':
    main()
