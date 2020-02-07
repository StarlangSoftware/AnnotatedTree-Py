from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsTurkishLeafNode import IsTurkishLeafNode
from AnnotatedTree.Processor.LayerExist.LeafListCondition import LeafListCondition


class NotContainsLayerInformation(LeafListCondition):

    __viewLayerType: ViewLayerType

    def __init__(self, viewLayerType: ViewLayerType):
        self.__viewLayerType = viewLayerType

    def satisfies(self, leafList: list) -> bool:
        for parseNode in leafList:
            if isinstance(parseNode, ParseNodeDrawable) and "*" \
                    not in parseNode.getLayerData(ViewLayerType.ENGLISH_WORD):
                if self.__viewLayerType == ViewLayerType.TURKISH_WORD:
                    if parseNode.getLayerData(self.__viewLayerType) is not None:
                        return False
                elif self.__viewLayerType == ViewLayerType.PART_OF_SPEECH or \
                        self.__viewLayerType == ViewLayerType.INFLECTIONAL_GROUP or \
                        self.__viewLayerType == ViewLayerType.NER or self.__viewLayerType == ViewLayerType.SEMANTICS or\
                        self.__viewLayerType == ViewLayerType.PROPBANK:
                    if parseNode.getLayerData(self.__viewLayerType) is not None and \
                            IsTurkishLeafNode().satisfies(parseNode):
                        return False
        return True
