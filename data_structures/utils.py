from dataclasses import dataclass
from typing import Generic, Optional, TypeVar


T = TypeVar("T")

@dataclass
class Node(Generic[T]):
    value: T
    next_node: Optional["Node[T]"]
