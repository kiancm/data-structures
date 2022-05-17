from typing import Generic

from list.linked_list import LinkedList
from utils import T

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
