from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode


class IsNoneNode(IsLeafNode):

    __second_language: ViewLayerType

    def __init__(self, secondLanguage: ViewLayerType):
        self.__second_language = secondLanguage

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        """
        Checks if the data of the parse node is '*NONE*'.
        :param parseNode: Parse node to check.
        :return: True if the data of the parse node is '*NONE*', false otherwise.
        """
        if super().satisfies(parseNode):
            data = parseNode.getLayerData(self.__second_language)
            return data is not None and data == "*NONE*"
        return False
