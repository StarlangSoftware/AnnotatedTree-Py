from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.NodeDrawableCondition import NodeDrawableCondition


class IsLeafNode(NodeDrawableCondition):

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        """
        Checks if the parse node is a leaf node, i.e., it has no child.
        :param parseNode: Parse node to check.
        :return: True if the parse node is a leaf node, false otherwise.
        """
        return parseNode.numberOfChildren() == 0
