from typing import Generic

from ..list.doubly_linked_list import DoublyLinkedList
from ..utils import T

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.size: int = 0
        self.values = DoublyLinkedList()

    def __repr__(self) -> str:
        values = [x for x in self.values]
        return f"{self.__class__.__qualname__}({values})"

    def push(self, value: T) -> None:
        """O(1)"""

        self.values.append(value)
        self.size += 1

    def peek(self) -> T:
        """O(1)"""

        try:
            return self.values[0]
        except IndexError:
            raise IndexError("Can't peek an empty queue")

    def pop(self) -> T:
        """O(1)"""

        value = self.values[0]
        del self.values[0]
        self.size -= 1

        return value
