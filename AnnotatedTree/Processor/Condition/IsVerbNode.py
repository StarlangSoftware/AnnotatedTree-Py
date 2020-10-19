from AnnotatedSentence.ViewLayerType import ViewLayerType
from Dictionary.Pos import Pos
from WordNet.WordNet import WordNet

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode


class IsVerbNode(IsLeafNode):

    __wordNet: WordNet

    def __init__(self, wordNet: WordNet):
        self.__wordNet = wordNet

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        layerInfo = parseNode.getLayerInfo()
        if super().satisfies(parseNode) and layerInfo is not None and \
            layerInfo.getLayerData(ViewLayerType.SEMANTICS) is not None:
            for i in range(layerInfo.getNumberOfMeanings()):
                synSetId = layerInfo.getSemanticAt(i)
                if self.__wordNet.getSynSetWithId(synSetId) is not None and \
                        self.__wordNet.getSynSetWithId(synSetId).getPos() == Pos.VERB:
                    return True
        return False
