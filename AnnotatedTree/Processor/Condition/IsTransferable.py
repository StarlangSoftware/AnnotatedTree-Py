from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode
from AnnotatedTree.Processor.Condition.IsNoneNode import IsNoneNode
from AnnotatedTree.Processor.Condition.IsNullElement import IsNullElement


class IsTransferable(IsLeafNode):

    __second_language: ViewLayerType

    def __init__(self, secondLanguage: ViewLayerType):
        self.__second_language = secondLanguage

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        if super().satisfies(parseNode):
            if IsNoneNode(self.__second_language).satisfies(parseNode):
                return False
            return not IsNullElement().satisfies(parseNode)
        return False
