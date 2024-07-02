from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable
from AnnotatedTree.Processor.LeafConverter.LeafToStringConverter import LeafToStringConverter


class TreeToStringConverter:

    __converter: LeafToStringConverter
    __parse_tree: ParseTreeDrawable

    def __init__(self, parseTree: ParseTreeDrawable, converter: LeafToStringConverter):
        """
        Constructor of the TreeToStringConverter class. Sets the attributes.
        :param parseTree: Parse tree to be converted.
        :param converter: Node to string converter interface.
        """
        self.__converter = converter
        self.__parse_tree = parseTree

    def convertToString(self, parseNode: ParseNodeDrawable):
        """
        Converts recursively a parse node to a string. If it is a leaf node, calls the converter's leafConverter method,
        otherwise concatenates the converted strings of its children.
        :param parseNode: Parse node to convert to string.
        :return: String form of the parse node and all of its descendants.
        """
        if parseNode.isLeaf():
            return self.__converter.leafConverter(parseNode)
        else:
            st = ""
            for i in range(parseNode.numberOfChildren()):
                st += self.convertToString(parseNode.getChild(i))
            return st

    def convert(self) -> str:
        """
        Calls the convertToString method with root of the tree to convert the parse tree to string.
        :return: String form of the parse tree.
        """
        return self.convertToString(self.__parse_tree.getRoot())
