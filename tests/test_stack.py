import unittest

from data_structures.stack import Stack

class StackTest(unittest.TestCase):
    def test_peek(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.peek()
        stack.push(1)
        self.assertEqual(1, stack.peek())
        stack.push(2)
        self.assertEqual(2, stack.peek())

    def test_pop(self):
        stack = Stack()

        with self.assertRaises(IndexError):
            stack.pop()

        stack.push(1)
        self.assertEqual(1, stack.pop())

        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.pop())

        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())

    def test_len(self):
        stack = Stack()
        self.assertEqual(0, len(stack))

        stack.push(1)
        self.assertEqual(1, len(stack))

        stack.push(2)
        self.assertEqual(2, len(stack))

        stack.push(3)
        self.assertEqual(3, len(stack))

        stack.pop()
        stack.pop()
        stack.pop()
        self.assertEqual(0, len(stack))
