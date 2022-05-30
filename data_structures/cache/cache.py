from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Callable, Dict, Generic, Optional, Protocol, TypeVar

from ..list.doubly_linked_list import DoublyLinkedList, Node
from ..utils import T


K = TypeVar("K")
V = TypeVar("V")


class Cache(Protocol[K, V]):
    capacity: int

    @abstractmethod
    def get(self, key: K) -> Optional[V]:
        ...

    @abstractmethod
    def put(self, key: K, value: V) -> None:
        ...

    def get_or_compute(self, key: K, supplier: Callable[[K], V]) -> V:
        return self.get(key) or supplier(key)


@dataclass
class Pair(Generic[K, V]):
    key: K
    value: V


@dataclass
class LRUCache(Cache[K, V]):
    capacity: int
    size: int = 0
    values: DoublyLinkedList[Pair[K, V]] = field(default_factory=DoublyLinkedList)
    table: Dict[K, Node[V]] = field(default_factory=dict)

    def get(self, key: K) -> Optional[V]:
        node = self.table.get(key)

        if node is not None:
            self._reinsert(key, node)
            return node.value.value

        return None

    def _reinsert(self, key: K, node: Node[V]) -> None:
        if (left := node.prev_node) is not None and (right := node.next_node) is not None:
            left.next_node = right
            right.prev_node = left
            self.values.prepend(Pair(key, node.value))

    def put(self, key: K, value: V) -> None:
        if self.size >= self.capacity:
            self._evict()
            self.size -=1

        self.values.prepend(Pair(key, value))
        self.table[key] = self.values.first
        self.size += 1

    def _evict(self) -> None:
        key = self.values[-1].key
        del self.table[key]
        del self.values[-1]
