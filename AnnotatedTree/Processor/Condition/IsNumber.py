import re

from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode


class IsNumber(IsLeafNode):

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        """
        Checks if the node is a leaf node and contains numerals as the data and its parent has the tag CD.
        :param parseNode: Parse node to check.
        :return: True if the node is a leaf node and contains numerals as the data and its parent has the tag CD, false
        otherwise.
        """
        if super().satisfies(parseNode):
            data = parseNode.getLayerData(ViewLayerType.ENGLISH_WORD)
            parent_data = parseNode.getParent().getData().getName()
            return parent_data == "CD" and re.fullmatch("[0-9,.]+", data) is not None
        return False
