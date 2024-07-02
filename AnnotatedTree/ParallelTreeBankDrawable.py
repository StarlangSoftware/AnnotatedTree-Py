from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable
from AnnotatedTree.TreeBankDrawable import TreeBankDrawable
from ParseTree.ParallelTreeBank import ParallelTreeBank


class ParallelTreeBankDrawable(ParallelTreeBank):

    def __init__(self,
                 folder1: str,
                 folder2: str,
                 pattern: str = None):
        """
        Constructor for two parallel treebanks.
        :param folder1: Folder containing the parse tree for the first tree bank.
        :param folder2: Folder containing the parse tree for the second tree bank.
        :param pattern: File name pattern for the files.
        """
        self.from_tree_bank = TreeBankDrawable(folder1, pattern)
        self.to_tree_bank = TreeBankDrawable(folder2, pattern)
        self.removeDifferentTrees()

    def fromTree(self, index: int) -> ParseTreeDrawable:
        """
        Accessor for the parse tree of the first tree bank.
        :param index: Position of the parse tree for the first tree bank.
        :return: The parse tree of the first tree bank at position index.
        """
        return self.from_tree_bank.get(index)

    def toTree(self, index: int) -> ParseTreeDrawable:
        """
        Accessor for the parse tree of the second tree bank.
        :param index: Position of the parse tree for the second tree bank.
        :return: The parse tree of the second tree bank at position index.
        """
        return self.to_tree_bank.get(index)

    def fromTreeBank(self) -> TreeBankDrawable:
        """
        Accessor for the first tree bank.
        :return: First tree bank.
        """
        return self.from_tree_bank

    def toTreeBank(self) -> TreeBankDrawable:
        """
        Accessor for the second tree bank.
        :return: Second tree bank.
        """
        return self.to_tree_bank
