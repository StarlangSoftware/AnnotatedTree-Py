from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsLeafNode import IsLeafNode
from AnnotatedTree.Processor.Condition.IsNullElement import IsNullElement


class IsEnglishLeafNode(IsLeafNode):

    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        if super().satisfies(parseNode):
            return not IsNullElement().satisfies(parseNode)
        return False
