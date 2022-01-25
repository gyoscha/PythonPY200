import unittest

from task import Node, DoubleLinkedNode


class TestNode(unittest.TestCase):
    def test_is_valid(self):
        Node.is_valid(None)
        Node.is_valid(Node(5))

        with self.assertRaises(TypeError):
            Node.is_valid(5)

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

    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        node = Node(5, Node(10))
        self.assertEqual(repr(node), 'Node(5, Node(10))',
                         msg='Неправильный __repr__')

    def test_str(self):
        some_value = 5
        node = Node(some_value)

        self.assertEqual(str(node), str(some_value))

    def test_set_next(self):
        node = Node(5)
        node_1 = Node(10)
        node.next = node_1

        self.assertIs(node.next, node_1)
        self.assertEqual(node.next.value, node_1.value)


class TestDoubleLinkedNode(unittest.TestCase):
    def test_init_node_without_prev(self):
        node = DoubleLinkedNode(10)

        self.assertIsNone(node.prev)
        self.assertIs(10, node.value)

    def test_init_node_with_prev(self):
        left_node = DoubleLinkedNode('left')
        right_node = DoubleLinkedNode('right', None, prev=left_node)

        self.assertIs(right_node.prev, left_node)
        self.assertIsNone(left_node.prev)

        self.assertEqual('left', left_node.value)
        self.assertEqual('right', right_node.value)

    def test_is_valid(self):
        Node.is_valid(None)
        Node.is_valid(DoubleLinkedNode(5))

        with self.assertRaises(TypeError):
            DoubleLinkedNode.is_valid(5)

    def test_repr_node_without_prev(self):
        node = DoubleLinkedNode(10)
        self.assertEqual(repr(node), 'DoubleLinkedNode(10, None, None)',
                         msg='Неправильный __repr__')

        node_2 = DoubleLinkedNode(100, DoubleLinkedNode(15))
        self.assertEqual(repr(node_2), 'DoubleLinkedNode(100, DoubleLinkedNode(15), None)',
                         msg='Неправильный __repr__')

    def test_repr_node_with_prev(self):
        node = DoubleLinkedNode(10, prev=DoubleLinkedNode(15))
        self.assertEqual(repr(node), 'DoubleLinkedNode(10, None, DoubleLinkedNode(15))',
                         msg='Неправильный __repr__')

        node = DoubleLinkedNode(100, DoubleLinkedNode(10), DoubleLinkedNode(15))
        self.assertEqual(repr(node), 'DoubleLinkedNode(100, DoubleLinkedNode(10), DoubleLinkedNode(15))',
                         msg='Неправильный __repr__')

    def test_set_prev(self):
        node = DoubleLinkedNode(5)
        node_1 = DoubleLinkedNode(10)
        node_1.prev = node

        self.assertIs(node_1.prev, node)
        self.assertEqual(node_1.prev.value, node.value)
