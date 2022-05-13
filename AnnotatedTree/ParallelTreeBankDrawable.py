from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable
from AnnotatedTree.TreeBankDrawable import TreeBankDrawable
from ParseTree.ParallelTreeBank import ParallelTreeBank


class ParallelTreeBankDrawable(ParallelTreeBank):

    def __init__(self, folder1: str, folder2: str, pattern: str = None):
        self.fromTreeBank = TreeBankDrawable(folder1, pattern)
        self.toTreeBank = TreeBankDrawable(folder2, pattern)
        self.removeDifferentTrees()

    def fromTree(self, index: int) -> ParseTreeDrawable:
        return self.fromTreeBank.get(index)

    def toTree(self, index: int) -> ParseTreeDrawable:
        return self.toTreeBank.get(index)

    def fromTreeBank(self) -> TreeBankDrawable:
        return self.fromTreeBank

    def toTreeBank(self) -> TreeBankDrawable:
        return self.toTreeBank
