from abc import abstractmethod

from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable


class TreeAutoSemantic:

    @abstractmethod
    def autoLabelSingleSemantics(self, parseTree: ParseTreeDrawable):
        pass

    def autoSemantic(self, parseTree: ParseTreeDrawable):
        if self.autoLabelSingleSemantics(parseTree):
            parseTree.save()
