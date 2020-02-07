import re

from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode


class IsNumber(IsLeafNode):

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        if super().satisfies(parseNode):
            data = parseNode.getLayerData(ViewLayerType.ENGLISH_WORD)
            parentData = parseNode.getParent().getData().getName()
            return parentData == "CD" and re.fullmatch("[0-9,.]+", data) is not None
        return False
