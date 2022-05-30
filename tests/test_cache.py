import unittest

from data_structures.cache.cache import Cache, LRUCache


class LRUCacheTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cache: Cache = LRUCache(10)

    def test_get_after_put_under_capacity(self):
        self.cache.put("a", 1)
        self.assertEqual(1, self.cache.get("a"))
        self.cache.put("b", 2)
        self.assertEqual(2, self.cache.get("b"))
        self.assertEqual(1, self.cache.get("a"))

    def test_get_reflects_mutated_entry(self):
        self.cache.put("a", 1)
        self.cache.put("a", 10)
        self.assertEqual(10, self.cache.get("a"))

    def test_put_deletes_lru_when_full(self):
        self.cache.put(0, 0)
        for i in range(1, self.cache.capacity):
            self.cache.put(i, i)
            self.cache.get(i)

        self.cache.put(-1, -1)
        self.assertIsNone(self.cache.get(0))

    def test_get_or_compute(self):
        self.assertEqual(10, self.cache.get_or_compute("a", lambda k: 10))
        self.cache.put("a", 1)
        self.assertEqual(1, self.cache.get_or_compute("a", lambda k: 10))
