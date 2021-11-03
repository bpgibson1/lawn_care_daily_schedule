"""
**************************************************************
Name        : yard_test.py
Author      : Bryner Gibson
Created     : 20201102
Course      : CIS 152 Data Structures
Version     : 1.0
OS          : Windows 10
Copyright   : This is my own original work based on
              specifications issued by our instructor
Description : This program overall description here
              Input:  list and describe
              Output: test yard class
Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or
unmodified. I have not given other fellow student(s) access to
my program.
***************************************************************
"""
import unittest
from yard import Yard


class MyTestCase(unittest.TestCase):
    def test_square_footage_to_low(self):
        # Arrange
        yard = Yard()
        yard.square_footage = 0
        # Actual
        actual = 0
        # Assert
        with self.assertRaises(ValueError):
            yard.calculate_total()

    def test_square_footage_first_range(self):
        # Arrange
        yard = Yard()
        yard.square_footage = 480
        expected = 43.2
        # Actual
        actual = yard.calculate_total()
        # Assert
        self.assertEqual(expected, actual)

    def test_square_footage_first_range_low(self):
        # Arrange
        yard = Yard()
        yard.square_footage = 320
        expected = 30
        # Actual
        actual = yard.calculate_total()
        # Assert
        self.assertEqual(expected, actual)

    def test_square_footage_second_range(self):
        # Arrange
        yard = Yard()
        yard.square_footage = 670
        expected = 53.6
        # Actual
        actual = yard.calculate_total()
        # Assert
        self.assertEqual(expected, actual)

    def test_square_footage_third_range(self):
        # Arrange
        yard = Yard()
        yard.square_footage = 1320
        expected = 79.2
        # Actual
        actual = yard.calculate_total()
        # Assert
        self.assertEqual(expected, actual)

    def test_square_footage_fourth_range(self):
        # Arrange
        yard = Yard()
        yard.square_footage = 1750
        expected = 87.5
        # Actual
        actual = yard.calculate_total()
        # Assert
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
