from typing import Generic

from .doubly_linked_list import DoublyLinkedList
from .utils import T

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.size: int = 0
        self.values = DoublyLinkedList()

    def __repr__(self) -> str:
        values = [x for x in self.values]
        return f"{self.__class__.__qualname__}({values})"

    def push(self, value: T) -> None:
        self.values.append(value)
        self.size += 1

    def peek(self) -> T:
        try:
            return self.values[0]
        except IndexError:
            raise IndexError("Can't peek an empty queue")

    def pop(self) -> T:
        value = self.values[0]
        del self.values[0]
        self.size -= 1

        return value
