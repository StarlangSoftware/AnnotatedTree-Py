from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsNodeWithSynSetId import IsNodeWithSynSetId


class IsNodeWithPredicate(IsNodeWithSynSetId):

    def __init__(self, _id: str):
        super().__init__(_id)

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        layerInfo = parseNode.getLayerInfo()
        return super().satisfies(parseNode) and layerInfo is not None and \
               layerInfo.getLayerData(ViewLayerType.PROPBANK) is not None and \
               layerInfo.getLayerData(ViewLayerType.PROPBANK) == "PREDICATE"
