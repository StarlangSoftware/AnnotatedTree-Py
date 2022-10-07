from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable
from AnnotatedTree.Processor.LeafConverter.LeafToStringConverter import LeafToStringConverter


class TreeToStringConverter:

    __converter: LeafToStringConverter
    __parse_tree: ParseTreeDrawable

    def __init__(self, parseTree: ParseTreeDrawable, converter: LeafToStringConverter):
        self.__converter = converter
        self.__parse_tree = parseTree

    def convertToString(self, parseNode: ParseNodeDrawable):
        if parseNode.isLeaf():
            return self.__converter.leafConverter(parseNode)
        else:
            st = ""
            for i in range(parseNode.numberOfChildren()):
                st += self.convertToString(parseNode.getChild(i))
            return st

    def convert(self) -> str:
        return self.convertToString(self.__parse_tree.getRoot())
