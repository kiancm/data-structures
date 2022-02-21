from typing import Iterable, Iterator, List, Optional

from .list import List
from .utils import T, Node


class LinkedList(List[T]):
    def __init__(self, init: Optional[List[T]] = None) -> None:
        self.head: Optional[Node[T]] = None
        self.size: int = 0
        if init:
            for x in init:
                self.append(x)

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator[T]:
        node = self.head
        while node is not None:
            yield node.value
            node = node.next_node

    def __delitem__(self, i: int) -> None:
        if self.head is None:
            raise IndexError("Can't delete from an empty list")
        if i == 0:
            self.head = self.head.next_node
        else:
            head = self.head
            for _ in range(i - 1):
                head = head.next_node
            match head:
                case Node(_, Node(_, next_node)):
                    head.next_node = next_node
                case Node(_, None):
                    raise IndexError(f"index out of bounds: {i}")
        self.size -= 1

    def __repr__(self):
        return f"{self.__class__.__qualname__}({list(self.__iter__())})"

    def prepend(self, x: T) -> None:
        self.head = Node(x, self.head)
        self.size += 1

    def append(self, x: T) -> None:
        if self.head is None:
            self.head = Node(x, self.head)
        elif self.head.next_node is None:
            self.head.next_node = Node(x, None)
        else:
            node = self.head.next_node
            while node.next_node is not None:
                node = node.next_node
            node.next_node = Node(x, None)
        self.size += 1

    def append_all(self, values: Iterable[T]) -> None:
        for value in values:
            self.append(value)

    def prepend_all(self, values: Iterable[T]) -> None:
        for value in values:
            self.prepend(value)

    def _get_node(self, i: int) -> Node[T]:
        if i < 0 or i >= self.size:
            raise IndexError("index out of bounds")
        head = self.head
        for _ in range(i):
            head = head.next_node
        return head

    def __getitem__(self, i: int) -> T:
        return self._get_node(i).value

    def __setitem__(self, i: int, value: T) -> None:
        self._get_node(i).value = value
