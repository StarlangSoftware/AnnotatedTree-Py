from AnnotatedSentence.ViewLayerType import ViewLayerType
from Dictionary.Word import Word

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode


class IsPunctuationNode(IsLeafNode):

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        """
        Checks if the node is a leaf node and contains punctuation as the data.
        :param parseNode: Parse node to check.
        :return: True if the node is a leaf node and contains punctuation as the data, false otherwise.
        """
        if super().satisfies(parseNode):
            data = parseNode.getLayerData(ViewLayerType.ENGLISH_WORD)
            return Word.isPunctuationSymbol(data) and data != "$"
        return False
