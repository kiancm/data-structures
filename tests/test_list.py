import unittest
from abc import ABC

from data_structures.linked_list import LinkedList
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

class LinkedListTest(ListTest, unittest.TestCase):
    def get_list(self) -> List:
        return LinkedList()
