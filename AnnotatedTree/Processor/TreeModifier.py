from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable
from AnnotatedTree.Processor.NodeModification.NodeModifier import NodeModifier


class TreeModifier:

    __parseTree: ParseTreeDrawable
    __nodeModifier: NodeModifier

    def nodeModify(self, parseNode: ParseNodeDrawable):
        self.__nodeModifier.modifier(parseNode)
        for i in range(parseNode.numberOfChildren()):
            self.nodeModify(parseNode.getChild(i))

    def modify(self):
        self.nodeModify(self.__parseTree.getRoot())

    def __init__(self, parseTree: ParseTreeDrawable, nodeModifier: NodeModifier):
        self.__parseTree = parseTree
        self.__nodeModifier = nodeModifier
