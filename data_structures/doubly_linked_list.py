from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Optional

from .list import List
from .utils import T

@dataclass
class Node(Generic[T]):
    value: T
    prev_node: Optional["Node[T]"]
    next_node: Optional["Node[T]"]

class DoublyLinkedList(List[T]):
    def __init__(self):
        self.first: Optional[Node[T]] = None
        self.last: Optional[Node[T]] = None
        self.size: int = 0

    def __len__(self) -> int:
        return self.size

    def __getitem__(self, i: int) -> T:
        return self._get_node(i).value

    def __setitem__(self, i: int, value: T) -> None:
        self._get_node(i).value = value

    def __delitem__(self, i: int) -> None:
        node = self._get_node(i)
        if node is None:
            raise IndexError("Can't delete from an empty list")
        match node:
            case Node(_, None, None):
                self.first = self.last = None
            case Node(_, None, next_node):
                self.first = next_node
            case Node(_, prev_node, None):
                self.last = prev_node
            case Node(_, prev_node, next_node):
                prev_node.next_node = next_node
                next_node.prev_node = prev_node
        self.size -= 1

    def __repr__(self):
        return f"{self.__class__.__qualname__}({list(self.__iter__())})"

    def _get_node(self, i: int) -> Optional[Node[T]]:
        if i < 0 or i >= self.size:
            raise IndexError("index out of bounds")
        node = self.first
        for _ in range(i):
            node = node.next_node
        return node

    def __iter__(self) -> Iterator[T]:
        node = self.first
        while node is not None:
            yield node.value
            node = node.next_node

    def append(self, value: T) -> None:
        if self.last is None:
            self.last = self.first = Node(value, prev_node=None, next_node=None)
        else:
            node = Node(value, prev_node=self.last, next_node=None)
            self.last.next_node = node
            self.last = node
        self.size += 1

    def prepend(self, value: T) -> None:
        if self.first is None:
            self.first = self.last = Node(value, prev_node=None, next_node=None)
        else:
            node = Node(value, prev_node=None, next_node=self.first)
            self.first.prev_node = node
            self.first = node

        self.size += 1

    def append_all(self, values: Iterable[T]) -> None:
        for value in values:
            self.append(value)

    def prepend_all(self, values: Iterable[T]) -> None:
        for value in values:
            self.prepend(value)
