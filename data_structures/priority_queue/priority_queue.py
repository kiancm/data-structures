from abc import ABC, abstractmethod
from typing import Generic

from ..utils import T


class PriorityQueue(ABC, Generic[T]):
    @abstractmethod
    def pop(self) -> T:
        ...

    @abstractmethod
    def push(self, value: T, priority: int) -> None:
        ...

    @abstractmethod
    def peek(self) -> T:
        ...
