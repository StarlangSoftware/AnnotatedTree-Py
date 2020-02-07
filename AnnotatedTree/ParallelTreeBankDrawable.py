from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable
from AnnotatedTree.TreeBankDrawable import TreeBankDrawable


class ParallelTreeBankDrawable:

    __fromTreeBank: TreeBankDrawable
    __toTreeBank: TreeBankDrawable

    def __init__(self, folder1: str, folder2: str, pattern: str = None):
        self.__fromTreeBank = TreeBankDrawable(folder1, pattern)
        self.__toTreeBank = TreeBankDrawable(folder2, pattern)
        self.removeDifferentTrees()

    def removeDifferentTrees(self):
        i = 0
        j = 0
        while i < self.__fromTreeBank.size() and j < self.__toTreeBank.size():
            if self.__fromTreeBank.get(i).getName() < self.__toTreeBank.get(j).getName():
                self.__fromTreeBank.removeTree(i)
            elif self.__fromTreeBank.get(i).getName() > self.__toTreeBank.get(j).getName():
                self.__toTreeBank.removeTree(j)
            else:
                i = i + 1
                j = j + 1
        while i < self.__fromTreeBank.size():
            self.__fromTreeBank.removeTree(i)
        while j < self.__toTreeBank.size():
            self.__toTreeBank.removeTree(j)

    def size(self) -> int:
        return self.__fromTreeBank.size()

    def fromTree(self, index: int) -> ParseTreeDrawable:
        return self.__fromTreeBank.get(index)

    def toTree(self, index: int) -> ParseTreeDrawable:
        return self.__toTreeBank.get(index)

    def fromTreeBank(self) -> TreeBankDrawable:
        return self.__fromTreeBank

    def toTreeBank(self) -> TreeBankDrawable:
        return self.__toTreeBank
