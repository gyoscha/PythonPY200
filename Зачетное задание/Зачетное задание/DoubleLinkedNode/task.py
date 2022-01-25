from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    """
    Класс, который описывает узел двусвязного списка
    """
    def __init__(self, value, next_: Optional["DoubleLinkedNode"] = None,  prev: Optional["DoubleLinkedNode"] = None):
        """
        Создаем новый узел для двусвязного списка
        :param prev: Прошлый узел, если он есть
        """
        super().__init__(value, next_)
        self.prev = prev

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["DoubleLinkedNode"]):
        self.is_valid(prev)
        self._prev = prev

    def is_valid(self, node: Any) -> None:
        """
        Проверка узла на приверженность типу None или DoubleLinkedNode
        """
        if not isinstance(node, (type(None), DoubleLinkedNode)):
            raise TypeError('Дан узел неверного типа')

    def __repr__(self) -> str:
        next_ = str(None) if self.next is None else f"{self.__class__.__name__}({self.next.value})"
        prev = str(None) if self.prev is None else f"{self.__class__.__name__}({self.prev.value})"
        return f"{self.__class__.__name__}({self.value}, {next_}, {prev})"


if __name__ == "__main__":
    dll = DoubleLinkedNode(10)
    dll_1 = DoubleLinkedNode(35)

    dll_1.prev = dll
    dll.next = dll_1

    print(repr(dll))
    print(repr(dll_1))
