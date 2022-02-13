import unittest
from typing import Generic, TypeVar
from dataclasses import dataclass

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.head: Node[T] | None = None
        self.size: int = 0

    def __len__(self) -> int:
        return self.size

    def push(self, x) -> None:
        if self.head is None:
            self.head = Node(x, None)
        else:
            old_head = self.head
            self.head = Node(x, old_head)
        self.size += 1

    def peek(self) -> T:
        match self.head:
            case Node(value, _):
                return value
            case None:
                raise IndexError("can't peek an empty stack")

    def pop(self) -> T:
        if self.head is None:
            raise IndexError("can't pop from an empty stack")
        value = self.head.value
        self.head = self.head.next_node
        self.size -= 1
        return value


@dataclass
class Node(Generic[T]):
    value: T
    next_node: Node[T] | None


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
