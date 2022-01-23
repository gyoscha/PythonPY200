from _collections_abc import MutableSequence
from typing import Any


class LinkedList(MutableSequence):
    def __getitem__(self, item: int) -> Any:
        pass

    def __setitem__(self, key: int, value: Any) -> None:
        pass

    def __delitem__(self, key: int) -> None:
        pass

    def __len__(self) -> int:
        pass

    def insert(self, index: int, value: Any) -> None:
        pass


if __name__ == "__main__":
    ...
