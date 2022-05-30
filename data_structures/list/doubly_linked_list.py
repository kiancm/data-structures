from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Optional

from .list import List
from ..utils import T

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
        match node:
            case Node(_, None, None):
                self.first = self.last = None
            case Node(_, None, next_node):
                self.first = Node(next_node.value, None, next_node.next_node)
            case Node(_, prev_node, None):
                self.last = prev_node
            case Node(_, prev_node, next_node):
                prev_node.next_node = next_node
                next_node.prev_node = prev_node
        self.size -= 1

    def __repr__(self):
        return f"{self.__class__.__qualname__}({list(self.__iter__())})"

    def _get_node(self, index: int) -> Node[T]:
        negative = index < 0
        normalized_index = -(index + 1) if negative else index
        for i, node in enumerate(self._node_iter(reversed=negative)):
            if i == normalized_index:
                return node
        raise IndexError(f"index out of bounds: {index}")

    def _node_iter(self, reversed=False) -> Iterator[Node[T]]:
        node = self.last if reversed else self.first
        while node is not None:
            yield node
            node = node.prev_node if reversed else node.next_node

    def __reversed__(self) -> Iterator[T]:
        for node in self._node_iter(reversed=True):
            yield node.value

    def __iter__(self) -> Iterator[T]:
        for node in self._node_iter():
            yield node.value

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
