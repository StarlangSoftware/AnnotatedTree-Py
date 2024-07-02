from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsTurkishLeafNode import IsTurkishLeafNode
from AnnotatedTree.Processor.LayerExist.LeafListCondition import LeafListCondition


class ContainsLayerInformation(LeafListCondition):

    __view_layer_type: ViewLayerType

    def __init__(self, viewLayerType: ViewLayerType):
        """
        Constructor for ContainsLayerInformation class. Sets the viewLayerType attribute.
        :param viewLayerType: Layer for which check is done.
        """
        self.__view_layer_type = viewLayerType

    def satisfies(self, leafList: list) -> bool:
        """
        Checks if all leaf nodes in the leafList contains the given layer information.
        :param leafList: Array list storing the leaf nodes.
        :return: True if all leaf nodes in the leafList contains the given layer information, false otherwise.
        """
        for parse_node in leafList:
            if isinstance(parse_node, ParseNodeDrawable) and "*" \
                    not in parse_node.getLayerData(ViewLayerType.ENGLISH_WORD):
                if self.__view_layer_type == ViewLayerType.TURKISH_WORD:
                    if parse_node.getLayerData(self.__view_layer_type) is None:
                        return False
                elif self.__view_layer_type == ViewLayerType.PART_OF_SPEECH or \
                        self.__view_layer_type == ViewLayerType.INFLECTIONAL_GROUP or \
                        self.__view_layer_type == ViewLayerType.NER or self.__view_layer_type == ViewLayerType.SEMANTICS or\
                        self.__view_layer_type == ViewLayerType.PROPBANK:
                    if parse_node.getLayerData(self.__view_layer_type) is None and \
                            IsTurkishLeafNode().satisfies(parse_node):
                        return False
        return True
