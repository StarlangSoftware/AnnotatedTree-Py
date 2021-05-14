from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.NodeDrawableCondition import NodeDrawableCondition


class NodeDrawableCollector:

    __condition: NodeDrawableCondition
    __rootNode: ParseNodeDrawable

    def __init__(self, rootNode: ParseNodeDrawable, condition: NodeDrawableCondition):
        self.__rootNode = rootNode
        self.__condition = condition

    def collectNodes(self, parseNode: ParseNodeDrawable, collected: list):
        if self.__condition is None or self.__condition.satisfies(parseNode):
            collected.append(parseNode)
        for i in range(parseNode.numberOfChildren()):
            self.collectNodes(parseNode.getChild(i), collected)

    def collect(self) -> list:
        result = []
        self.collectNodes(self.__rootNode, result)
        return result
