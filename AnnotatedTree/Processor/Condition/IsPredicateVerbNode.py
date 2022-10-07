from WordNet.WordNet import WordNet

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsVerbNode import IsVerbNode


class IsPredicateVerbNode(IsVerbNode):

    def __init__(self, wordNet: WordNet):
        super().__init__(wordNet)

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        layer_info = parseNode.getLayerInfo()
        return super().satisfies(parseNode) and layer_info is not None and layer_info.getArgument() is not None \
               and layer_info.getArgument().getArgumentType() == "PREDICATE"
