from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.NodeDrawableCondition import NodeDrawableCondition


class IsNodeWithSymbol(NodeDrawableCondition):

    __symbol: str

    def __init__(self, symbol: str):
        self.__symbol = symbol

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        if parseNode.numberOfChildren() > 0:
            return parseNode.getData().__str__() == self.__symbol
        else:
            return False
