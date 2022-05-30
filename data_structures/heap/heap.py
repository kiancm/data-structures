from abc import abstractmethod
from typing import Protocol

from ..utils import T


class Heap(Protocol[T]):
    @abstractmethod
    def pop(self) -> T:
        ...

    @abstractmethod
    def push(self, value: T) -> T:
        ...

    @abstractmethod
    def peek(self) -> T:
        ...


class MinHeapWithRef(Heap):
    def __init__(self):
        self.array = []

    def peek(self) -> T:
        return super().peek()

    def push(self, value: T) -> T:
        return super().push(value)

    def pop(self) -> T:
        return super().pop()
