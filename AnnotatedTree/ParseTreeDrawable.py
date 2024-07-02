import os

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from AnnotatedSentence.ViewLayerType import ViewLayerType
from Corpus.FileDescription import FileDescription
from ParseTree.ParseNode import ParseNode
from ParseTree.ParseTree import ParseTree
from WordNet.WordNet import WordNet

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsEnglishLeafNode import IsEnglishLeafNode
from AnnotatedTree.Processor.Condition.IsPredicateVerbNode import IsPredicateVerbNode
from AnnotatedTree.Processor.Condition.IsTurkishLeafNode import IsTurkishLeafNode
from AnnotatedTree.Processor.Condition.IsVerbNode import IsVerbNode
from AnnotatedTree.Processor.NodeDrawableCollector import NodeDrawableCollector


class ParseTreeDrawable(ParseTree):
    __file_description: FileDescription

    def __init__(self,
                 fileDescription,
                 path: str = None):
        """
        Another constructor for the ParseTreeDrawable. Sets the file description and reads the tree from the file
        description.
        :param fileDescription: File description that contains the path, index and extension information.
        :param path: Path of the tree
        """
        if path is None:
            if isinstance(fileDescription, FileDescription):
                self.__file_description = fileDescription
                self.name = fileDescription.getRawFileName()
                self.readFromFile(self.__file_description.getFileName(fileDescription.getPath()))
            elif isinstance(fileDescription, str):
                self.name = os.path.split(fileDescription)[1]
                self.readFromFile(fileDescription)
        else:
            self.__file_description = FileDescription(path, fileDescription.getExtension(), fileDescription.getIndex())
            self.name = self.__file_description.getRawFileName()
            self.readFromFile(self.__file_description.getFileName(fileDescription.getPath()))

    def setFileDescription(self, fileDescription: FileDescription):
        """
        Mutator method for the fileDescription attribute.
        :param fileDescription: New fileDescription value.
        """
        self.__file_description = fileDescription

    def getFileDescription(self) -> FileDescription:
        """
        Accessor method for the fileDescription attribute.
        :return: FileDescription attribute.
        """
        return self.__file_description

    def reload(self):
        """
        Reloads the tree from the input file.
        """
        self.readFromFile(self.__file_description.getFileName(self.__file_description.getPath()))

    def readFromFile(self, fileName: str):
        """
        Reads the parse tree from the given line. It sets the root node which calls ParseNodeDrawable constructor
        recursively.
        :param fileName: Name of the file containing the definition of the tree.
        """
        input_file = open(fileName, encoding="utf8")
        line = input_file.readline().strip()
        if "(" in line and ")" in line:
            line = line[line.index("(") + 1:line.rindex(")")].strip()
            self.root = ParseNodeDrawable(None, line, False, 0)
        else:
            self.root = None
        input_file.close()

    def nextTree(self, count: int):
        """
        Loads the next tree according to the index of the parse tree. For example, if the current
        tree fileName is 0123.train, after the call of nextTree(3), the method will load 0126.train. If the next tree
        does not exist, nothing will happen.
        :param count: Number of trees to go forward
        """
        if self.__file_description.nextFileExists(count):
            self.__file_description.addToIndex(count)
            self.reload()

    def previousTree(self, count: int):
        """
        Loads the previous tree according to the index of the parse tree. For example, if the current
        tree fileName is 0123.train, after the call of previousTree(4), the method will load 0119.train. If the
        previous tree does not exist, nothing will happen.
        :param count: Number of trees to go backward
        """
        if self.__file_description.previousFileExists(count):
            self.__file_description.addToIndex(-count)
            self.reload()

    def save(self):
        """
        Saves current tree.
        """
        output_file = open(self.__file_description.getFileName(), mode='w', encoding="utf8")
        output_file.write("( " + self.__str__() + " )\n")
        output_file.close()

    def saveWithPath(self, newPath: str):
        """
        Saves current tree to the newPath with other file properties staying the same.
        :param newPath: Path to which tree will be saved
        """
        output_file = open(self.__file_description.getFileName(newPath), mode='w', encoding="utf8")
        output_file.write("( " + self.__str__() + " )\n")
        output_file.close()

    def maxDepth(self) -> int:
        """
        Calculates the maximum depth of the tree.
        :return: The maximum depth of the tree.
        """
        if isinstance(self.root, ParseNodeDrawable):
            return self.root.maxDepth()

    def moveLeft(self, node: ParseNode):
        if self.root != node:
            self.root.moveLeft(node)

    def moveRight(self, node: ParseNode):
        if self.root != node:
            self.root.moveRight(node)

    def layerExists(self, viewLayerType: ViewLayerType) -> bool:
        """
        The method checks if all nodes in the tree has the annotation in the given layer.
        :param viewLayerType: Layer name
        :return: True if all nodes in the tree has the annotation in the given layer, false otherwise.
        """
        if self.root is not None and isinstance(self.root, ParseNodeDrawable):
            return self.root.layerExists(viewLayerType)
        else:
            return False

    def layerAll(self, viewLayerType: ViewLayerType) -> bool:
        """
        Checks if all nodes in the tree has annotation with the given layer.
        :param viewLayerType: Layer name
        :return: True if all nodes in the tree has annotation with the given layer, false otherwise.
        """
        if self.root is not None and isinstance(self.root, ParseNodeDrawable):
            return self.root.layerAll(viewLayerType)
        else:
            return False

    def clearLayer(self, viewLayerType: ViewLayerType):
        """
        Clears the given layer for all nodes in the tree
        :param viewLayerType: Layer name
        """
        if self.root is not None and isinstance(self.root, ParseNodeDrawable):
            self.root.clearLayer(viewLayerType)

    def generateAnnotatedSentence(self, language: str = None) -> AnnotatedSentence:
        """
        Constructs an AnnotatedSentence object from the Turkish tree. Collects all leaf nodes, then for each leaf node
        converts layer info of all words at that node to AnnotatedWords. Layers are converted to the counterparts in the
        AnnotatedWord.
        :param language: Language of the parse tree.
        :return: AnnotatedSentence counterpart of the English / Persian tree
        """
        sentence = AnnotatedSentence()
        if language is None:
            node_drawable_collector = NodeDrawableCollector(self.root, IsTurkishLeafNode())
            leaf_list = node_drawable_collector.collect()
            for parse_node in leaf_list:
                if isinstance(parse_node, ParseNodeDrawable):
                    layers = parse_node.getLayerInfo()
                    for i in range(layers.getNumberOfWords()):
                        sentence.addWord(layers.toAnnotatedWord(i))
        else:
            node_drawable_collector = NodeDrawableCollector(self.root, IsEnglishLeafNode())
            leaf_list = node_drawable_collector.collect()
            for parse_node in leaf_list:
                if isinstance(parse_node, ParseNodeDrawable):
                    newWord = AnnotatedWord("{" + language + "=" + parse_node.getData().getName() + "}{posTag="
                                            + parse_node.getParent().getData().getName() + "}")
                    sentence.addWord(newWord)
        return sentence

    def generateParseTree(self, surfaceForm: bool) -> ParseTree:
        """
        Recursive method that generates a new parse tree by replacing the tag information of the all parse nodes (with all
        its descendants) with respect to the morphological annotation of all parse nodes (with all its descendants)
        of the current parse tree.
        :param surfaceForm: If true, tag will be replaced with the surface form annotation.
        :return: A new parse tree generated by replacing the tag information of the all parse nodes (with all
        its descendants) with respect to the morphological annotation of all parse nodes (with all its descendants)
        of the current parse tree.
        """
        result = ParseTree(ParseNode(self.root.getData()))
        self.root.generateParseNode(result.getRoot(), surfaceForm)
        return result

    def extractNodesWithVerbs(self, wordNet: WordNet) -> list:
        node_drawable_collector = NodeDrawableCollector(self.root, IsVerbNode(wordNet))
        return node_drawable_collector.collect()

    def extractNodesWithPredicateVerbs(self, wordNet: WordNet) -> list:
        node_drawable_collector = NodeDrawableCollector(self.root, IsPredicateVerbNode(wordNet))
        return node_drawable_collector.collect()
