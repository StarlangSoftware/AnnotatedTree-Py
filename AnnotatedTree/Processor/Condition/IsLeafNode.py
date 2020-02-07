from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.NodeDrawableCondition import NodeDrawableCondition


class IsLeafNode(NodeDrawableCondition):

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        return parseNode.numberOfChildren() == 0
