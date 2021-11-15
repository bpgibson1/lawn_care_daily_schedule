"""
**************************************************************
Name        : daily_schedule_test.py
Author      : Bryner Gibson
Created     : 20211114
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
import unittest
from class_files.customer import Customer
from class_files.daily_schedule import DailySchedule
from class_files.yard import Yard


class MyTestCase(unittest.TestCase):
    def test_add_high_low(self):
        # Arrange
        yard = Yard("", 1250)
        yard2 = Yard("", 480)
        customer = Customer()
        customer.set_yard(yard)
        customer.set_yard(yard2)
        ds = DailySchedule()
        ds.add_customer(customer)
        # Actual
        actual = ds.customer_priority_queue.peek()
        actual = actual.priority
        # Assert
        expected = "B"
        self.assertEquals(expected, actual)

    def test_add_low_high(self):
        # Arrange
        yard = Yard("", 1250)
        yard2 = Yard("", 480)
        customer = Customer()
        customer.set_yard(yard2)
        customer.set_yard(yard)
        ds = DailySchedule()
        ds.add_customer(customer)
        # Actual
        actual = ds.customer_priority_queue.peek()
        actual = actual.priority
        # Assert
        expected = "B"
        self.assertEquals(expected, actual)

    def test_add_only_high(self):
        # Arrange
        yard = Yard("", 1250)
        yard2 = Yard("", 480)
        customer = Customer()
        customer.set_yard(yard)
        ds = DailySchedule()
        ds.add_customer(customer)
        # Actual
        actual = ds.customer_priority_queue.peek()
        actual = actual.priority
        # Assert
        expected = "B"
        self.assertEquals(expected, actual)

    def test_add_only_low(self):
        # Arrange
        yard = Yard("", 1250)
        yard2 = Yard("", 480)
        customer = Customer()
        customer.set_yard(yard2)
        ds = DailySchedule()
        ds.add_customer(customer)
        # Actual
        actual = ds.customer_priority_queue.peek()
        actual = actual.priority
        # Assert
        expected = "D"
        self.assertEquals(expected, actual)

    def test_add_out_of_range(self):
        # Arrange
        yard2 = Yard("", 0)
        customer = Customer()
        customer.set_yard(yard2)
        ds = DailySchedule()
        # Actual
        # Assert
        with self.assertRaises(ValueError):
            ds.add_customer(customer)

    def test_add_priority_A(self):
        # Arrange
        yard = Yard("", 1600)
        yard2 = Yard("", 480)
        yard3 = Yard("", 1250)
        customer = Customer()
        customer.set_yard(yard)
        customer.set_yard(yard2)
        customer.set_yard(yard3)
        ds = DailySchedule()
        ds.add_customer(customer)
        # Actual
        actual = ds.customer_priority_queue.peek()
        actual = actual.priority
        # Assert
        expected = "A"
        self.assertEquals(expected, actual)

    def test_add_priority_C(self):
        # Arrange
        yard = Yard("", 480)
        yard2 = Yard("", 850)
        customer = Customer()
        customer.set_yard(yard2)
        customer.set_yard(yard)
        ds = DailySchedule()
        ds.add_customer(customer)
        # Actual
        actual = ds.customer_priority_queue.peek()
        actual = actual.priority
        # Assert
        expected = "C"
        self.assertEquals(expected, actual)

    def test_add_priority_D(self):
        # Arrange
        yard = Yard("", 480)
        customer = Customer()
        customer.set_yard(yard)
        ds = DailySchedule()
        ds.add_customer(customer)
        # Actual
        actual = ds.customer_priority_queue.peek()
        actual = actual.priority
        # Assert
        expected = "D"
        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
