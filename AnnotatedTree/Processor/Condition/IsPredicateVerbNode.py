from WordNet.WordNet import WordNet

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsVerbNode import IsVerbNode


class IsPredicateVerbNode(IsVerbNode):

    def __init__(self, wordNet: WordNet):
        """
        Stores the wordnet for checking the pos tag of the synset.
        :param wordNet: Wordnet used for checking the pos tag of the synset.
        """
        super().__init__(wordNet)

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        """
        Checks if the node is a leaf node and at least one of the semantic ids of the parse node belong to a verb synset,
        and the semantic role of the node is PREDICATE.
        :param parseNode: Parse node to check.
        :return: True if the node is a leaf node and at least one of the semantic ids of the parse node belong to a verb
              synset and the semantic role of the node is PREDICATE, false otherwise.
        """
        layer_info = parseNode.getLayerInfo()
        return super().satisfies(parseNode) and layer_info is not None and layer_info.getArgument() is not None \
               and layer_info.getArgument().getArgumentType() == "PREDICATE"
