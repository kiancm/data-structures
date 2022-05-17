from typing import Generic

from utils import T, Node


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
