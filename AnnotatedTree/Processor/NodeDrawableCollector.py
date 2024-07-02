from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.NodeDrawableCondition import NodeDrawableCondition


class NodeDrawableCollector:

    __condition: NodeDrawableCondition
    __root_node: ParseNodeDrawable

    def __init__(self, rootNode: ParseNodeDrawable, condition: NodeDrawableCondition):
        """
        Constructor for the NodeDrawableCollector class. NodeDrawableCollector's main aim is to collect a set of
        ParseNode's from a subtree rooted at rootNode, where the ParseNode's satisfy a given NodeCondition, which is
        implemented by other interface class.
        :param rootNode: Root node of the subtree
        :param condition: The condition interface for which all nodes in the subtree rooted at rootNode will be checked
        """
        self.__root_node = rootNode
        self.__condition = condition

    def collectNodes(self, parseNode: ParseNodeDrawable, collected: list):
        """
        Private recursive method to check all descendants of the parseNode, if they ever satisfy the given node condition
        :param parseNode: Root node of the subtree
        :param collected: The {@link ArrayList} where the collected ParseNode's will be stored.
        :return:
        """
        if self.__condition is None or self.__condition.satisfies(parseNode):
            collected.append(parseNode)
        for i in range(parseNode.numberOfChildren()):
            self.collectNodes(parseNode.getChild(i), collected)

    def collect(self) -> list:
        """
        Collects and returns all ParseNodes satisfying the node condition.
        :return: All ParseNodes satisfying the node condition.
        """
        result = []
        self.collectNodes(self.__root_node, result)
        return result
