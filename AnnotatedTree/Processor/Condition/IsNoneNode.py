from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode


class IsNoneNode(IsLeafNode):

    __secondLanguage: ViewLayerType

    def __init__(self, secondLanguage: ViewLayerType):
        self.__secondLanguage = secondLanguage

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        if super().satisfies(parseNode):
            data = parseNode.getLayerData(self.__secondLanguage)
            return data is not None and data == "*NONE*"
        return False
