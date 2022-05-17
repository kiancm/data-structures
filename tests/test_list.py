import unittest
from abc import ABC

from data_structures.list.doubly_linked_list import DoublyLinkedList
from data_structures.list.linked_list import LinkedList
from data_structures.list import List


class ListTest(ABC):
    def get_list(self) -> List:
        pass

    def setUp(self) -> None:
        self.list = self.get_list()

    def test_prepend(self):
        self.list.prepend(1)
        self.list.prepend(2)
        self.list.prepend(10)
        self.assertEqual(1, self.list[2])
        self.assertEqual(2, self.list[1])
        self.assertEqual(10, self.list[0])

    def test_append(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(10)
        self.assertEqual(1, self.list[0])
        self.assertEqual(2, self.list[1])
        self.assertEqual(10, self.list[2])

    def test_getitem_out_of_bounds(self):
        self.list.append(1)
        with self.assertRaises(IndexError):
            self.list[1]
        with self.assertRaises(IndexError):
            self.list[-1]

    def test_len(self):
        self.assertEqual(0, len(self.list))
        self.list.append(1)
        self.assertEqual(1, len(self.list))
        del self.list[0]
        self.assertEqual(0, len(self.list))

    def test_del_first(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        del self.list[0]
        self.assertEqual(2, self.list[0])
        self.assertEqual(3, self.list[1])

    def test_del_last(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        del self.list[2]
        self.assertEqual(1, self.list[0])
        self.assertEqual(2, self.list[1])

    def test_del_middle(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        del self.list[1]
        self.assertEqual(1, self.list[0])
        self.assertEqual(3, self.list[1])

    def test_del_bounds(self):
        with self.assertRaises(IndexError):
            del self.list[0]
        self.list.append(1)
        with self.assertRaises(IndexError):
            del self.list[1]
        self.list.append(2)
        del self.list[0]
        del self.list[0]
        with self.assertRaises(IndexError):
            del self.list[0]

    def test_append_all(self):
        self.list.append_all([])
        self.assertEqual(0, len(self.list))

        self.list.append_all([1, 2, 3])
        self.assertEqual(3, len(self.list))

    def test_prepend_all(self):
        self.list.prepend_all([])
        self.assertEqual(0, len(self.list))

        self.list.prepend_all([1, 2, 3])
        self.assertEqual(3, len(self.list))

    def test_set_item(self):
        with self.assertRaises(IndexError):
            self.list[0] = 1
        self.list.append(1)
        self.list[0] = 2
        self.assertEqual(2, self.list[0])
        with self.assertRaises(IndexError):
            self.list[1] = 3

    def test_iter(self):
        self.list.append_all([1, 2, 3, 4])
        values = [x for x in self.list]
        self.assertEqual([1, 2, 3, 4], values)


class LinkedListTest(ListTest, unittest.TestCase):
    def get_list(self) -> List:
        return LinkedList()


class DoublyLinkedListTest(ListTest, unittest.TestCase):
    def get_list(self) -> List:
        return DoublyLinkedList()
