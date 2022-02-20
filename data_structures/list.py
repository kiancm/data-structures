from typing import Protocol
from .utils import T

class List(Protocol[T]):
    def __len__(self) -> int:
        ...

    def __getitem__(self, i: int) -> T:
        ...

    def __setitem__(self, i: int, value: T) -> None:
        ...

    def append(self, value: T) -> None:
        ...

    def prepend(self, value: T) -> None:
        ...

    def insert(self, i: int, value: T) -> None:
        ...
