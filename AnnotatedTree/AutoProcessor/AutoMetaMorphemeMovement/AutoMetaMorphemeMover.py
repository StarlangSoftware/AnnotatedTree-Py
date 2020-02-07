from abc import abstractmethod

from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable


class AutoMetaMorphemeMover:

    @abstractmethod
    def metaMorphemeMoveWithRules(self, parseTree: ParseTreeDrawable):
        pass

    def autoPosMove(self, parseTree: ParseTreeDrawable):
        self.metaMorphemeMoveWithRules(parseTree)
        parseTree.save()
