import unittest

from class_files.priority_queue import PriorityQueue
from exceptions.QueueEmptyException import QueueEmptyException


class MyTestCase(unittest.TestCase):
    def test_create_queue_and_empty(self):
        pq = PriorityQueue()
        self.assertTrue(pq.is_empty())

    def test_is_empty_false(self):
        pq = PriorityQueue()
        pq.add("item", 'A')

        self.assertFalse(pq.is_empty())

    def test_add_and_find_at(self):
        pq = PriorityQueue()
        pq.add("item2", 'D')
        pq.add("item1", 'A')

        self.assertEqual('A', pq.find_at(0).priority)
        self.assertEqual('item1', pq.find_at(0).customer)
        self.assertEqual('D', pq.find_at(1).priority)
        self.assertEqual('item2', pq.find_at(1).customer)

    def test_find_at_out_of_range_low(self):
        pq = PriorityQueue()
        pq.add("item2", 'D')
        pq.add("item1", 'A')

        self.assertEqual(None, pq.find_at(-1))

    def test_find_at_out_of_range_high(self):
        pq = PriorityQueue()
        pq.add("item2", 'D')
        pq.add("item1", 'A')

        self.assertEqual(None, pq.find_at(12))

    def test_remove_empty(self):
        pq = PriorityQueue()

        with self.assertRaises(QueueEmptyException):
            pq.remove()

    def test_remove(self):
        pq = PriorityQueue()
        pq.add("item2", 'D')
        pq.add("item1", 'A')

        expected = pq.find_at(0).customer
        actual = pq.remove().customer

        self.assertEqual(actual, expected)
        self.assertEqual(1, pq.size())

    def test_peek_empty(self):
        pq = PriorityQueue()

        with self.assertRaises(QueueEmptyException):
            pq.peek()

    def test_peek(self):
        pq = PriorityQueue()
        pq.add("item2", 'D')
        pq.add("item1", 'A')

        expected = pq.find_at(0).customer
        actual = pq.peek().customer

        self.assertEqual(actual, expected)
        self.assertEqual(2, pq.size())


if __name__ == '__main__':
    unittest.main()
