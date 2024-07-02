from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode


class IsNullElement(IsLeafNode):

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        """
        Checks if the parse node is a leaf node and its data is '*' and its parent's data is '-NONE-'.
        :param parseNode: Parse node to check.
        :return: True if the parse node is a leaf node and its data is '*' and its parent's data is '-NONE-', false
        otherwise.
        """
        if super().satisfies(parseNode):
            data = parseNode.getLayerData(ViewLayerType.ENGLISH_WORD)
            parent_data = parseNode.getParent().getData().getName()
            return "*" in data or (data == "0" and parent_data == "-NONE-")
        return False
