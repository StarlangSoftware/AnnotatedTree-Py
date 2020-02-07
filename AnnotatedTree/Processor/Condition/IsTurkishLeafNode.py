from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode


class IsTurkishLeafNode(IsLeafNode):

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        if super().satisfies(parseNode):
            data = parseNode.getLayerData(ViewLayerType.TURKISH_WORD)
            parentData = parseNode.getParent().getData().getName()
            return data is not None and "*" not in data and (not (data == "0" and parentData == "-NONE-"))
        return False
