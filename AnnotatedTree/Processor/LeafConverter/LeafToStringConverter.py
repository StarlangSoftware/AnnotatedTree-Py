from abc import abstractmethod

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable


class LeafToStringConverter:

    @abstractmethod
    def leafConverter(self, leafNode: ParseNodeDrawable) -> str:
        pass
