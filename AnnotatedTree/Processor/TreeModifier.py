from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable
from AnnotatedTree.Processor.NodeModification.NodeModifier import NodeModifier


class TreeModifier:

    __parse_tree: ParseTreeDrawable
    __node_modifier: NodeModifier

    def nodeModify(self, parseNode: ParseNodeDrawable):
        self.__node_modifier.modifier(parseNode)
        for i in range(parseNode.numberOfChildren()):
            self.nodeModify(parseNode.getChild(i))

    def modify(self):
        self.nodeModify(self.__parse_tree.getRoot())

    def __init__(self, parseTree: ParseTreeDrawable, nodeModifier: NodeModifier):
        self.__parse_tree = parseTree
        self.__node_modifier = nodeModifier
