from WordNet.WordNet import WordNet

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsVerbNode import IsVerbNode


class IsPredicateVerbNode(IsVerbNode):

    def __init__(self, wordNet: WordNet):
        super().__init__(wordNet)

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        layerInfo = parseNode.getLayerInfo()
        return super().satisfies(parseNode) and layerInfo is not None and layerInfo.getArgument() is not None \
               and layerInfo.getArgument().getArgumentType() == "PREDICATE"
