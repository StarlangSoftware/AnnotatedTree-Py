from abc import abstractmethod

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable


class NodeModifier:

    @abstractmethod
    def modifier(self, parseNode: ParseNodeDrawable):
        pass
