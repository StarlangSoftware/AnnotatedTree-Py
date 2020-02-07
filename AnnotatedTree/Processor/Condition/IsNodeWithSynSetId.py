from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode


class IsNodeWithSynSetId(IsLeafNode):

    __id: str

    def __init__(self, id: str):
        self.__id = id

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        if super().satisfies(parseNode):
            layerInfo = parseNode.getLayerInfo()
            for i in range(layerInfo.getNumberOfMeanings()):
                synSetId = layerInfo.getSemanticAt(i)
                if synSetId == self.__id:
                    return True
        return False
