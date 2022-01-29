import unittest

from node import Node, DoubleLinkedNode
from task import LinkedList, DoubleLinkedList


class TestLinkedList(unittest.TestCase):
    def test_append(self):
        linkedlist_1 = LinkedList([1, 2, 3, 4])
        linkedlist_2 = LinkedList([])
        append_node = Node(5)

        linkedlist_1.append(append_node)
        linkedlist_2.append(append_node)
        self.assertIs(linkedlist_1.__getitem__(4), append_node)
        self.assertIs(linkedlist_2.__getitem__(0), append_node)

    def test_step_by_step_on_nodes(self):
        linkedlist = LinkedList([1, 2, 3, 4, 5])
        node = linkedlist.step_by_step_on_nodes(1)

        self.assertIs(linkedlist.__getitem__(1), node.value)

    def test_linked_nodes(self):
        linkedlist = LinkedList()
        node_1 = Node(1)
        node_2 = Node(2)

        linkedlist.linked_nodes(node_1, node_2)

        self.assertIs(node_1.next, node_2)

    def test_setitem(self):
        node = Node(5)
        linkedlist = LinkedList([1, 2, 3, 4, 9])

        linkedlist.__setitem__(4, 5)

        self.assertIs(linkedlist.__getitem__(4), node.value)

    def test_delitem(self):
        node = Node(4)
        linkedlist = LinkedList([1, 2, 3, 4, 9])

        linkedlist.__delitem__(4)

        self.assertIs(linkedlist.__getitem__(3), node.value)

    def test_insert(self):
        node = Node(5)
        linkedlist = LinkedList([1, 2, 3, 4, 9])

        linkedlist.insert(4, 5)
        self.assertIs(linkedlist.__getitem__(4), node.value)

        linkedlist.__delitem__(4)

        linkedlist.insert(0, 5)
        self.assertIs(linkedlist.__getitem__(0), node.value)

        linkedlist.__delitem__(0)
        linkedlist.insert(10, 5)
        self.assertIs(linkedlist.__getitem__(5), node.value)

    def test_str(self):
        list_ = [1, 2, 3, 4]
        linkedlist = LinkedList([1, 2, 3, 4])

        self.assertEqual(str(linkedlist), str(list_))

    def test_repr(self):
        linkedlist = LinkedList([1, 2, 3, 4])

        self.assertEqual(repr(linkedlist), 'LinkedList([1, 2, 3, 4])')

    def test_reversed(self):
        list_ = [4, 3, 2, 1]
        linkedlist = LinkedList([1, 2, 3, 4])

        linkedlist.__reversed__()

        self.assertEqual(str(linkedlist), str(list_))

    def test_count(self):
        linkedlist = LinkedList([1, 2, 3, 4, 2])
        number = linkedlist.count(2)

        self.assertEqual(number, 2)

    def test_pop(self):
        linkedlist = LinkedList([1, 2, 3, 4])
        pop_item = linkedlist.pop(2)

        self.assertIs(pop_item, 3)
        self.assertEqual(str(linkedlist), '[1, 2, 4]')

        pop_item_2 = linkedlist.pop()

        self.assertIs(pop_item_2, 4)
        self.assertEqual(str(linkedlist), '[1, 2]')

    def test_extend(self):
        linkedlist = LinkedList([1, 2, 3, 4])
        value_1 = 10.1
        linkedlist.extend(value_1)

        self.assertIs(linkedlist.__getitem__(4), value_1)

        value_2 = [10, 11]
        linkedlist.extend(value_2)

        self.assertIs(linkedlist.__getitem__(5), 10)
        self.assertIs(linkedlist.__getitem__(6), 11)

    def test_remove(self):
        linkedlist = LinkedList([1, 2, 3, 4])
        linkedlist.remove(1)

        self.assertIs(linkedlist.__getitem__(0), 2)

        with self.assertRaises(ValueError):
            linkedlist.remove(10)

    def test_index(self):
        linkedlist = LinkedList([1, 2, 3, 4])
        index_ = linkedlist.index(4)

        self.assertIs(index_, 3)


class TestDoubleLinkedList(unittest.TestCase):
    def test_linked_nodes(self):
        linkedlist = DoubleLinkedList()
        node_1 = DoubleLinkedNode(1)
        node_2 = DoubleLinkedNode(2)

        linkedlist.linked_nodes(node_1, node_2)

        self.assertIs(node_2.prev, node_1)
