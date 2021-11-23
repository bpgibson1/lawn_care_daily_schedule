import unittest

from class_files.customer import Customer
from class_files.yard import Yard


class MyTestCase(unittest.TestCase):
    def test_set_yard(self):
        # Arrange
        c = Customer()
        y1 = Yard("yard1", 450)
        c.set_yard(y1)

        # Assert
        self.assertEqual(450, c.yards_queue.find_at(0).square_footage)
        self.assertEqual("yard1", c.yards_queue.find_at(0).yard_name)

    def test_sort_method(self):
        # Arrange
        c = Customer()
        y1 = Yard("", 450)
        y2 = Yard("", 350)
        y3 = Yard("", 250)
        y4 = Yard("", 1250)
        c.set_yard(y1)
        c.set_yard(y2)
        c.set_yard(y3)
        c.set_yard(y4)

        # Assert before sort
        self.assertEqual(1250, c.yards_queue.find_at(3).square_footage)
        self.assertEqual(450, c.yards_queue.find_at(0).square_footage)
        self.assertEqual(350, c.yards_queue.find_at(1).square_footage)
        self.assertEqual(250, c.yards_queue.find_at(2).square_footage)

        c.sort_yard()

        # Assert after sort
        self.assertEqual(1250, c.yards_queue.find_at(0).square_footage)
        self.assertEqual(450, c.yards_queue.find_at(1).square_footage)
        self.assertEqual(350, c.yards_queue.find_at(2).square_footage)
        self.assertEqual(250, c.yards_queue.find_at(3).square_footage)

    def test_sort_one_object(self):
        # Arrange
        c = Customer()
        y1 = Yard("", 450)
        c.set_yard(y1)

        # Assert before sort
        self.assertEqual(450, c.yards_queue.find_at(0).square_footage)

        c.sort_yard()

        # Assert After sort
        self.assertEqual(450, c.yards_queue.find_at(0).square_footage)

    def test_sort_two_equal_objects(self):
        # Arrange
        c = Customer()
        y1 = Yard("yard1", 450)
        y2 = Yard("yard2", 450)
        c.set_yard(y1)
        c.set_yard(y2)

        # Assert before sort
        self.assertEqual(450, c.yards_queue.find_at(0).square_footage)
        self.assertEqual("yard1", c.yards_queue.find_at(0).yard_name)
        self.assertEqual(450, c.yards_queue.find_at(1).square_footage)
        self.assertEqual("yard2", c.yards_queue.find_at(1).yard_name)

        c.sort_yard()

        # Assert After sort
        self.assertEqual(450, c.yards_queue.find_at(0).square_footage)
        self.assertEqual("yard1", c.yards_queue.find_at(0).yard_name)
        self.assertEqual(450, c.yards_queue.find_at(1).square_footage)
        self.assertEqual("yard2", c.yards_queue.find_at(1).yard_name)

if __name__ == '__main__':
    unittest.main()
