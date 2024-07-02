from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.NodeDrawableCondition import NodeDrawableCondition


class IsNodeWithSymbol(NodeDrawableCondition):

    __symbol: str

    def __init__(self, symbol: str):
        """
        Stores the symbol to check.
        :param symbol: Symbol to check
        """
        self.__symbol = symbol

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        """
        Checks if the tag of the parse node is equal to the given symbol.
        :param parseNode: Parse node to check.
        :return: True if the tag of the parse node is equal to the given symbol, false otherwise.
        """
        if parseNode.numberOfChildren() > 0:
            return parseNode.getData().__str__() == self.__symbol
        else:
            return False
