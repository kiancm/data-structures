from typing import Generic, Protocol

from .linked_list import LinkedList
from .utils import T, Node

class Stack(Protocol[T]):
    def __len__(self) -> int:
        ...

    def push(self, x) -> None:
        ...

    def peek(self) -> T:
        ...

    def pop(self) -> T:
        ...


class HandRolledStack(Generic[T]):
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


class LinkedStack(Generic[T]):
    def __init__(self) -> None:
        self.values = LinkedList()

    def __len__(self) -> int:
        return len(self.values)

    def push(self, x) -> None:
        self.values.prepend(x)

    def peek(self) -> T:
        return self.values[0]

    def pop(self) -> T:
        value = self.peek()
        del self.values[0]

        return value
