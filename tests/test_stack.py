import unittest
from abc import ABC, abstractmethod

from data_structures.stack import Stack, LinkedStack, HandRolledStack


class StackTest(ABC):
    @abstractmethod
    def get_stack(self) -> Stack:
        pass

    def setUp(self) -> None:
        self.stack: Stack = self.get_stack()

    def test_peek(self):
        with self.assertRaises(IndexError):
            self.stack.peek()
        self.stack.push(1)
        self.assertEqual(1, self.stack.peek())
        self.stack.push(2)
        self.assertEqual(2, self.stack.peek())

    def test_pop(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

        self.stack.push(1)
        self.assertEqual(1, self.stack.pop())

        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(2, self.stack.pop())

        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(2, self.stack.pop())
        self.assertEqual(1, self.stack.pop())

    def test_len(self):
        self.assertEqual(0, len(self.stack))

        self.stack.push(1)
        self.assertEqual(1, len(self.stack))

        self.stack.push(2)
        self.assertEqual(2, len(self.stack))

        self.stack.push(3)
        self.assertEqual(3, len(self.stack))

        self.stack.pop()
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(0, len(self.stack))


class LinkedStackTest(StackTest, unittest.TestCase):
    def get_stack(self) -> Stack:
        return LinkedStack()


class HandRolledStackTest(StackTest, unittest.TestCase):
    def get_stack(self) -> Stack:
        return HandRolledStack()
