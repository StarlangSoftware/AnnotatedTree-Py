from abc import abstractmethod

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable


class NodeDrawableCondition:

    @abstractmethod
    def satisfies(self, parseNode: ParseNodeDrawable) -> bool:
        pass
