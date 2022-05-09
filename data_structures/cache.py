from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Callable, Dict, Generic, Optional, Protocol, TypeVar, List

from .utils import T


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
class CacheValue(Generic[T]):
    value: T
    priority: int



@dataclass
class LRUCache(Cache[K, V]):
    capacity: int
    size: int = 0
    queue: List[CacheValue[K]] = field(default_factory=list)
    table: Dict[K, V] = field(default_factory=dict)

    def get(self, key: K) -> Optional[V]:
        value = self.table.get(key)

        if value is not None:
            for cvalue in self.queue:
                if cvalue.value == key:
                    cvalue.priority += 1
                    self.queue = list(sorted(self.queue, key=lambda x: x.priority))

        return value

    def put(self, key: K, value: V) -> None:
        self.queue.append(CacheValue(value=key, priority=1))
        self.queue = list(sorted(self.queue, key=lambda x: x.priority))
        self.table[key] = value
        self.size += 1

        if self.size > self.capacity:
            self._evict()

    def _evict(self) -> CacheValue[K]:
        cvalue = self.queue.pop(0)
        del self.table[cvalue.value]

        return cvalue
