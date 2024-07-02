from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode
from AnnotatedTree.Processor.Condition.IsNullElement import IsNullElement


class IsEnglishLeafNode(IsLeafNode):

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        """
        Checks if the parse node is a leaf node and contains a valid English word in its data.
        :param parseNode: Parse node to check.
        :return: True if the parse node is a leaf node and contains a valid English word in its data; false otherwise.
        """
        if super().satisfies(parseNode):
            return not IsNullElement().satisfies(parseNode)
        return False
