from _collections_abc import MutableSequence
from typing import Any, Iterable, Optional, Iterator

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    CLASS_NODE = Node

    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self._len = 0
        self._head = None
        self._tail = self._head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = self.CLASS_NODE(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    def step_by_step_on_nodes(self, index: int):
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError('Индекс не соответствует типу int.')

        if not 0 <= index < self._len:  # для for
            raise IndexError('Индекс выходит за рамки связного списка.')

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int) -> None:
        """
        Метод удаляет узел по указанному индексу.
        :param index: Индекс удаляемого узла.
        :return: None
        """
        if not isinstance(index, int):
            raise TypeError('Индекс не соответствует типу int.')

        if not 0 <= index < self._len:  # для for
            raise IndexError('Индекс выходит за рамки связного списка.')

        if index == 0:
            self._head = self._head.next
        elif index == self._len - 1:
            tail = self.step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next

            self.linked_nodes(prev_node, next_node)

        self._len -= 1

    def __len__(self) -> int:
        """
        Метод определения длины последовательности.
        :return: Значение длины
        """
        return self._len

    def insert(self, index: int, value: Any) -> None:
        """
        Добавление в LinkedList узла по опреденному идексу.
        :param index: Индекс, по которому хотим вставить элемент.
        :param value: Значение, которое хотим вставить.
        :return: None
        """
        if not isinstance(index, int):
            raise TypeError('Индекс не соответствует типу int.')

        insert_node = self.CLASS_NODE(value)
        if index == 0:
            self.linked_nodes(insert_node, self._head)
            self._head = insert_node
            self._len += 1
        elif index >= self._len - 1:
            self.append(value)
            self._tail = insert_node
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next
            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)

            self._len += 1

    def __str__(self):
        return f"{self.to_list()}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.to_list()})"

    def nodes_iterator(self):
        """
        Итератор по узлам LinkedList.
        :return: Итератор.
        """
        current_node = self._head
        for _ in range(self._len):
            yield current_node
            current_node = current_node.next

    def __iter__(self) -> Iterator[Any]:
        """
        Переопределяем метод iter для LinkedList.
        :return: Итератор.
        """
        for node in self.nodes_iterator():
            yield node.value

    def __contains__(self, item: Any) -> bool:
        """
        Метод проверяет вхождение значения item в LinkedList.
        :param item: Значение, вхождение котрого хотим проверить.
        :return: True/False
        """
        for node in self.nodes_iterator():
            if node.value == item:
                return True

        return False

    def __reversed__(self) -> None:
        """
        Метод для реализации обратного итерирования по объекту.
        """
        prev_node = None
        current_node = self._head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self._head = self._tail

    def count(self, value: Any) -> int:
        """ Метод подсчитывает количество экземпляров элемента в списке. """
        count = 0
        for val in self.to_list():
            if val == value:
                count += 1

        return count

    def pop(self, index: Optional[int] = None) -> Any:
        """ Метод удаляет элемент по указанному индексу и возвращает его.
            Если индекс не указан, то удаляет и возвращает последний элемент. """

        list_values = self.to_list()

        if index is not None:
            self.__delitem__(index)
            return list_values[index]
        else:
            self.__delitem__(self._len - 1)
            return list_values[len(list_values) - 1]

    def extend(self, value: Any) -> None:
        """ Этот метод обновляет список, добавляя элементы в конец. """
        if isinstance(value, (int, float)):
            self.append(value)
        else:
            for i in value:
                self.append(i)

    def remove(self, value: Any) -> None:
        """
        Метод удаляет элемент из LinkedList.
        """
        if value not in self.to_list():
            raise ValueError('Введенное значение отсутсвтует')

        index = self.index(value)
        self.__delitem__(index)

    def index(self, value: Any, start: int = ..., stop: int = ...) -> int:
        """ Метод ищет элемент в списке и возвращает его индекс. """
        if value not in self.to_list():
            raise ValueError('Введенное значение отсутсвтует')

        for index, val in enumerate(self.to_list()):
            if val == value:
                return index


class DoubleLinkedList(LinkedList):
    CLASS_NODE = DoubleLinkedNode

    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node


if __name__ == "__main__":
    pass

