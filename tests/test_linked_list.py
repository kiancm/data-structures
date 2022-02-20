import unittest

from data_structures.linked_list import LinkedList

class LinkedListTest(unittest.TestCase):
    def test_prepend(self):
        linked_list = LinkedList()
        linked_list.prepend(1)
        linked_list.prepend(2)
        linked_list.prepend(10)
        self.assertEqual(1, linked_list[2])
        self.assertEqual(2, linked_list[1])
        self.assertEqual(10, linked_list[0])

    def test_append(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(10)
        self.assertEqual(1, linked_list[0])
        self.assertEqual(2, linked_list[1])
        self.assertEqual(10, linked_list[2])

    def test_getitem_out_of_bounds(self):
        linked_list = LinkedList()
        linked_list.append(1)
        with self.assertRaises(IndexError):
            linked_list[1]
        with self.assertRaises(IndexError):
            linked_list[-1]

    def test_len(self):
        linked_list = LinkedList()
        self.assertEqual(0, len(linked_list))
        linked_list.append(1)
        self.assertEqual(1, len(linked_list))
        del linked_list[0]
        self.assertEqual(0, len(linked_list))


    def test_del_first(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        del linked_list[0]
        self.assertEqual(2, linked_list[0])
        self.assertEqual(3, linked_list[1])

    def test_del_last(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        del linked_list[2]
        self.assertEqual(1, linked_list[0])
        self.assertEqual(2, linked_list[1])

    def test_del_middle(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        del linked_list[1]
        self.assertEqual(1, linked_list[0])
        self.assertEqual(3, linked_list[1])

    def test_del_bounds(self):
        linked_list = LinkedList()
        with self.assertRaises(IndexError):
            del linked_list[0]
        linked_list.append(1)
        with self.assertRaises(IndexError):
            del linked_list[1]
        linked_list.append(2)
        del linked_list[0]
        del linked_list[0]
        with self.assertRaises(IndexError):
            del linked_list[0]
