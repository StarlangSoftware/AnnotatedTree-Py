from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsNodeWithSynSetId import IsNodeWithSynSetId


class IsNodeWithPredicate(IsNodeWithSynSetId):

    def __init__(self, _id: str):
        """
        Stores the synset id to check.
        :param _id: Synset id to check
        """
        super().__init__(_id)

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        """
        Checks if at least one of the semantic ids of the parse node is equal to the given id and also the node is
        annotated as PREDICATE with semantic role.
        :param parseNode: Parse node to check.
        :return: True if at least one of the semantic ids of the parse node is equal to the given id and also the node is
        annotated as PREDICATE with semantic role, false otherwise.
        """
        layerInfo = parseNode.getLayerInfo()
        return super().satisfies(parseNode) and layerInfo is not None and \
               layerInfo.getLayerData(ViewLayerType.PROPBANK) is not None and \
               layerInfo.getLayerData(ViewLayerType.PROPBANK) == "PREDICATE"
