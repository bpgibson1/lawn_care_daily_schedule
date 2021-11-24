import unittest
from class_files.queue import Queue
from exceptions.QueueEmptyException import QueueEmptyException


class MyTestCase(unittest.TestCase):
    def test_create_queue(self):
        # ARRANGE
        my_queue = Queue()
        # ACT
        actual = my_queue.is_empty()
        # ASSERT
        self.assertTrue(actual)

    def test_is_empty_true(self):
        # ARRANGE
        my_queue = Queue()
        # ACT
        actual = my_queue.is_empty()
        # ASSERT
        self.assertTrue(actual)

    def test_is_empty_false(self):
        # ARRANGE
        my_queue = Queue()
        item = "Python is Fun!"
        # ACT
        my_queue.enqueue(item)
        actual = my_queue.is_empty()
        # ASSERT
        self.assertFalse(actual)

    def test_enqueue(self):
        # ARRANGE
        my_queue = Queue()
        item = "QueueItem"
        expected = "QueueItem1"
        # ACT
        my_queue.enqueue(item + "1")
        my_queue.enqueue(item + "2")
        actual = my_queue.peek()
        # ASSERT
        self.assertEqual(expected, actual)

    def test_dequeue(self):
        # ARRANGE
        my_queue = Queue()
        item = "QueueItem"
        expected = "QueueItem1"
        my_queue.enqueue(item+"1")
        my_queue.enqueue(item+"2")
        # ACT
        actual = my_queue.dequeue()
        # ASSERT
        self.assertEqual(expected, actual)

    def test_size_zero(self):
        # ARRANGE
        my_queue = Queue()
        expected = 0
        # ACT
        actual = my_queue.size()
        # ASSERT
        self.assertEqual(expected, actual)

    def test_size_non_zero(self):
        # ARRANGE
        my_queue = Queue()
        item = "QueueItem"
        expected = 2
        # ACT
        my_queue.enqueue(item + "1")
        my_queue.enqueue(item + "2")
        actual = my_queue.size()
        print(my_queue.tail)
        # ASSERT
        self.assertEqual(expected, actual)

    def test_dequeue_empty_queue(self):
        # ARRANGE
        my_queue = Queue()
        # ACT
        # ASSERT
        with self.assertRaises(QueueEmptyException):
            my_queue.dequeue()

    def test_peek(self):
        # ARRANGE
        my_queue = Queue()
        item = "QueueItem"
        expected = "QueueItem1"
        # ACT
        my_queue.enqueue(item + "1")
        my_queue.enqueue(item + "2")
        actual = my_queue.peek()
        # ASSERT
        self.assertEqual(expected, actual)

    def test_peek_empty_queue(self):
        # ARRANGE
        my_queue = Queue()
        # ACT
        # ASSERT
        with self.assertRaises(QueueEmptyException):
            my_queue.peek()

    def test_swap_empty(self):
        # ARRANGE
        my_queue = Queue()
        # ACT
        # ASSERT
        with self.assertRaises(QueueEmptyException):
            my_queue.swap(1, 2)

    def test_swap_size_1(self):
        # ARRANGE
        my_queue = Queue()
        item = "QueueItem"
        expected = "QueueItem1"
        # ACT
        my_queue.enqueue(item + "1")
        # ASSERT
        self.assertEqual(expected, my_queue.find_at(0))
        my_queue.swap(0, 0)
        self.assertEqual(expected, my_queue.find_at(0))

    def test_swap_good(self):
        # ARRANGE
        my_queue = Queue()
        item = 10
        expected = "QueueItem1"
        # ACT
        my_queue.enqueue(item + 2)
        my_queue.enqueue(item + 200)
        my_queue.enqueue(item + 100)
        # ASSERT
        self.assertEqual(12, my_queue.find_at(0))
        self.assertEqual(210, my_queue.find_at(1))
        self.assertEqual(110, my_queue.find_at(2))
        my_queue.swap(0, 1)
        self.assertEqual(12, my_queue.find_at(1))
        self.assertEqual(210, my_queue.find_at(0))
        self.assertEqual(110, my_queue.find_at(2))
        my_queue.swap(0, 2)
        self.assertEqual(12, my_queue.find_at(1))
        self.assertEqual(210, my_queue.find_at(2))
        self.assertEqual(110, my_queue.find_at(0))


if __name__ == '__main__':
    unittest.main()
