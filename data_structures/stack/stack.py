from typing import Protocol

from utils import T


class Stack(Protocol[T]):
    def __len__(self) -> int:
        ...

    def push(self, x) -> None:
        """O(1)"""
        ...

    def peek(self) -> T:
        """O(1)"""
        ...

    def pop(self) -> T:
        """O(1)"""
        ...
