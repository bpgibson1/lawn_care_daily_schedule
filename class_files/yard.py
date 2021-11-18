"""
**************************************************************
Name        : yard.py
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


class Yard:

    def __init__(self, name="", square_footage=0, address=""):
        self.yard_name = name
        self.square_footage = int(square_footage)
        self.address = address
        self._flat_fee = 30
        self._price_breaks = {0: .09, 500: .08, 1000: .06, 1500: .05}
        self._price_break_keys = [0, 500, 1000, 1500]
        self.priority = None
        self.total_price = None
        self.fee_flag = 0
        self.price_per_square_foot = 0

    def calculate_total(self):
        # Calculate total based on price breaks
        price_per_square_foot = 0
        if self.square_footage <= self._price_break_keys[0]:
            raise ValueError
        elif self.square_footage <= self._price_break_keys[1]:
            self.price_per_square_foot = self._price_breaks[self._price_break_keys[0]]
            self.priority = 'D'
        elif self._price_break_keys[1] < self.square_footage <= self._price_break_keys[2]:
            self.price_per_square_foot = self._price_breaks[self._price_break_keys[1]]
            self.priority = 'C'
        elif self._price_break_keys[2] < self.square_footage <= self._price_break_keys[3]:
            self.price_per_square_foot = self._price_breaks[self._price_break_keys[2]]
            self.priority = 'B'
        elif self.square_footage > self._price_break_keys[3]:
            self.price_per_square_foot = self._price_breaks[self._price_break_keys[3]]
            self.priority = 'A'

        return self.flat_fee_validation(int(round(self.square_footage * self.price_per_square_foot * 100)) / 100)

    def flat_fee_validation(self, current_total):
        if current_total > self._flat_fee:
            return current_total
        self.fee_flag = 1
        return self._flat_fee

    def get_flat_fee(self):
        return self._flat_fee
