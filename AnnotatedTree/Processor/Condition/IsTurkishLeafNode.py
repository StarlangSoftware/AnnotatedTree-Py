from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode


class IsTurkishLeafNode(IsLeafNode):

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        """
        Checks if the parse node is a leaf node and contains a valid Turkish word in its data.
        :param parseNode: Parse node to check.
        :return: True if the parse node is a leaf node and contains a valid Turkish word in its data; false otherwise.
        """
        if super().satisfies(parseNode):
            data = parseNode.getLayerData(ViewLayerType.TURKISH_WORD)
            parent_data = parseNode.getParent().getData().getName()
            return data is not None and "*" not in data and (not (data == "0" and parent_data == "-NONE-"))
        return False
