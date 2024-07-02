from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode


class IsNodeWithSynSetId(IsLeafNode):

    __id: str

    def __init__(self, id: str):
        """
        Stores the synset id to check.
        :param id: Synset id to check
        """
        self.__id = id

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        """
        Checks if at least one of the semantic ids of the parse node is equal to the given id.
        :param parseNode: Parse node to check.
        :return: True if at least one of the semantic ids of the parse node is equal to the given id, false otherwise.
        """
        if super().satisfies(parseNode):
            layer_info = parseNode.getLayerInfo()
            for i in range(layer_info.getNumberOfMeanings()):
                syn_set_id = layer_info.getSemanticAt(i)
                if syn_set_id == self.__id:
                    return True
        return False
