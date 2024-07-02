from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode


class IsProperNoun(IsLeafNode):

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        """
        Checks if the node is a leaf node and its parent has the tag NNP or NNPS.
        :param parseNode: Parse node to check.
        :return: True if the node is a leaf node and its parent has the tag NNP or NNPS, false otherwise.
        """
        if super().satisfies(parseNode):
            parent_data = parseNode.getParent().getData().getName()
            return parent_data == "NNP" or parent_data == "NNPS"
        return False
