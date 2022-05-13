import unittest

from AnnotatedTree.ParallelTreeBankDrawable import ParallelTreeBankDrawable


class ParallelTreeBankDrawableTest(unittest.TestCase):

    def test_ParallelTreeBankDrawable(self):
        parallelTreeBank = ParallelTreeBankDrawable("../trees", "../trees2")
        self.assertEqual(10, parallelTreeBank.size())


if __name__ == '__main__':
    unittest.main()
