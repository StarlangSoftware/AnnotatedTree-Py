from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.NodeDrawableCondition import NodeDrawableCondition


class IsVPNode(NodeDrawableCondition):

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        """
        Checks if the node is not a leaf node and its tag is VP.
        :param parseNode: Parse node to check.
        :return: True if the node is not a leaf node and its tag is VP, false otherwise.
        """
        return parseNode.numberOfChildren() > 0 and parseNode.getData().isVP()
