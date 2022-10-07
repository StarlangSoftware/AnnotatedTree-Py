from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable
from AnnotatedTree.TreeBankDrawable import TreeBankDrawable
from ParseTree.ParallelTreeBank import ParallelTreeBank


class ParallelTreeBankDrawable(ParallelTreeBank):

    def __init__(self,
                 folder1: str,
                 folder2: str,
                 pattern: str = None):
        self.from_tree_bank = TreeBankDrawable(folder1, pattern)
        self.to_tree_bank = TreeBankDrawable(folder2, pattern)
        self.removeDifferentTrees()

    def fromTree(self, index: int) -> ParseTreeDrawable:
        return self.from_tree_bank.get(index)

    def toTree(self, index: int) -> ParseTreeDrawable:
        return self.to_tree_bank.get(index)

    def fromTreeBank(self) -> TreeBankDrawable:
        return self.from_tree_bank

    def toTreeBank(self) -> TreeBankDrawable:
        return self.to_tree_bank
