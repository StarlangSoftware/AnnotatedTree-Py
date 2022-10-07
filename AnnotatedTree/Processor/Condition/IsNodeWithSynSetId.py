from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode


class IsNodeWithSynSetId(IsLeafNode):

    __id: str

    def __init__(self, id: str):
        self.__id = id

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        if super().satisfies(parseNode):
            layer_info = parseNode.getLayerInfo()
            for i in range(layer_info.getNumberOfMeanings()):
                syn_set_id = layer_info.getSemanticAt(i)
                if syn_set_id == self.__id:
                    return True
        return False
