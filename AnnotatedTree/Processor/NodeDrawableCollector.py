from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.NodeDrawableCondition import NodeDrawableCondition


class NodeDrawableCollector:

    __condition: NodeDrawableCondition
    __root_node: ParseNodeDrawable

    def __init__(self, rootNode: ParseNodeDrawable, condition: NodeDrawableCondition):
        self.__root_node = rootNode
        self.__condition = condition

    def collectNodes(self, parseNode: ParseNodeDrawable, collected: list):
        if self.__condition is None or self.__condition.satisfies(parseNode):
            collected.append(parseNode)
        for i in range(parseNode.numberOfChildren()):
            self.collectNodes(parseNode.getChild(i), collected)

    def collect(self) -> list:
        result = []
        self.collectNodes(self.__root_node, result)
        return result
