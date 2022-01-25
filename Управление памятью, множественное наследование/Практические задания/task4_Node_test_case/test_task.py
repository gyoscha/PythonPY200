import unittest

from task import Node


class TestCase(unittest.TestCase):
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        node = Node(5)
        self.assertIsNone(node.next)

        self.assertEqual(5, node.value)

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        right_node = Node('right')
        left_node = Node('left', next_=right_node)

        self.assertIs(right_node, left_node.next)
        self.assertIsNone(right_node.next)

        self.assertEqual('left', left_node.value)
        self.assertEqual('right', right_node.value)

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        node = Node(5)
        self.assertEqual(repr(node), 'Node(5, None)',
                         msg='Неправильный __repr__')

    @unittest.skip('Будет реализован позже')
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        node = Node(5, Node(10))
        self.assertEqual(repr(node), 'Node(5, Node(10))',
                         msg='Неправильный __repr__')

    def test_str(self):
        some_value = 5
        node = Node(some_value)

        self.assertEqual(str(node), str(some_value))

    def test_is_valid(self):
        Node.is_valid(None)
        Node.is_valid(Node(5))

        with self.assertRaises(TypeError):
            Node.is_valid(5)
