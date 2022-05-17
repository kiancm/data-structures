import unittest

from data_structures.queue.queue import Queue

class QueueTest(unittest.TestCase):
    def test_queue(self):
        queue = Queue()
        queue.push(1)
        self.assertEqual(1, queue.peek())
        self.assertEqual(1, queue.pop())
        with self.assertRaises(IndexError):
            queue.peek()
        queue.push(2)
        self.assertEqual(2, queue.peek())
        self.assertEqual(2, queue.pop())
        queue.push(3)
        queue.push(4)
        self.assertEqual(3, queue.pop())
        # self.assertEqual(3, queue.pop())
