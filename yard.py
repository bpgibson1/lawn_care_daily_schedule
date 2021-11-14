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

    def __init__(self, name, square_footage):
        self.yard_name = name
        self.square_footage = square_footage
        self.total_price = self.calculate_total()
        self._flat_fee = 30
        self._price_breaks = {0: .09, 500: .08, 1000: .06, 1500: .05}
        self._price_break_keys = [0, 500, 1000, 1500]

    def calculate_total(self):
        # Calculate total based on price breaks
        price_per_square_foot = 0
        if self.square_footage <= self._price_break_keys[0]:
            raise ValueError
        elif self.square_footage <= self._price_break_keys[1]:
            price_per_square_foot = self._price_breaks[self._price_break_keys[0]]
        elif self._price_break_keys[1] < self.square_footage <= self._price_break_keys[2]:
            price_per_square_foot = self._price_breaks[self._price_break_keys[1]]
        elif self._price_break_keys[2] < self.square_footage <= self._price_break_keys[3]:
            price_per_square_foot = self._price_breaks[self._price_break_keys[2]]
        elif self.square_footage > self._price_break_keys[3]:
            price_per_square_foot = self._price_breaks[self._price_break_keys[3]]

        return self.flat_fee_validation(int(round(self.square_footage * price_per_square_foot * 100)) / 100)

    def flat_fee_validation(self, current_total):
        if current_total > self._flat_fee:
            return current_total
        return self._flat_fee
