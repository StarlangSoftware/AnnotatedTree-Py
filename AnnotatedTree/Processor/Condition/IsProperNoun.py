from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode


class IsProperNoun(IsLeafNode):

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        if super().satisfies(parseNode):
            parent_data = parseNode.getParent().getData().getName()
            return parent_data == "NNP" or parent_data == "NNPS"
        return False
