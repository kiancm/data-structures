from typing import Iterable, Iterator, Protocol
from .utils import T

class List(Protocol[T]):
    def __len__(self) -> int:
        ...

    def __getitem__(self, i: int) -> T:
        ...

    def __setitem__(self, i: int, value: T) -> None:
        ...

    def __iter__(self) -> Iterator[T]:
        ...

    def append(self, value: T) -> None:
        ...

    def prepend(self, value: T) -> None:
        ...

    def append_all(self, values: Iterable[T]) -> None:
        ...

    def prepend_all(self, values: Iterable[T]) -> None:
        ...
