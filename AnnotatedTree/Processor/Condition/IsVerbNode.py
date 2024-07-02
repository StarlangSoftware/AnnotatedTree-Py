from AnnotatedSentence.ViewLayerType import ViewLayerType
from Dictionary.Pos import Pos
from WordNet.WordNet import WordNet

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode


class IsVerbNode(IsLeafNode):

    __word_net: WordNet

    def __init__(self, wordNet: WordNet):
        """
        Stores the wordnet for checking the pos tag of the synset.
        :param wordNet: Wordnet used for checking the pos tag of the synset.
        """
        self.__word_net = wordNet

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        """
        Checks if the node is a leaf node and at least one of the semantic ids of the parse node belong to a verb synset.
        :param parseNode: Parse node to check.
        :return: True if the node is a leaf node and at least one of the semantic ids of the parse node belong to a verb
        synset, false otherwise.
        """
        layer_info = parseNode.getLayerInfo()
        if super().satisfies(parseNode) and layer_info is not None and \
            layer_info.getLayerData(ViewLayerType.SEMANTICS) is not None:
            for i in range(layer_info.getNumberOfMeanings()):
                syn_set_id = layer_info.getSemanticAt(i)
                if self.__word_net.getSynSetWithId(syn_set_id) is not None and \
                        self.__word_net.getSynSetWithId(syn_set_id).getPos() == Pos.VERB:
                    return True
        return False
