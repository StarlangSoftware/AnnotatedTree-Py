import unittest

from AnnotatedTree.TreeBankDrawable import TreeBankDrawable


class TreeBankDrawableTest(unittest.TestCase):

    def test_TreeBankDrawable(self):
        treeBank1 = TreeBankDrawable("../trees")
        self.assertEqual(10, treeBank1.size())
        treeBank2 = TreeBankDrawable("../trees2")
        self.assertEqual(10, treeBank2.size())


if __name__ == '__main__':
    unittest.main()
