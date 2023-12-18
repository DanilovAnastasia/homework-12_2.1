import unittest
from utils import arrs
from utils import dicts


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([]),[])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4]), [1, 2, 3, 4])


    def test_get_val(self):
        data = {"vcs": "mercurial"}
        self.assertEqual(dicts.get_val(data, "vcs"), "mercurial")
        self.assertEqual(dicts.get_val(data, "vcs", "git"), "mercurial")
        data = {}
        self.assertEqual(dicts.get_val(data, "vcs", "git"), "git")
        self.assertEqual(dicts.get_val(data, "vcs", "bazaar"), "bazaar")


