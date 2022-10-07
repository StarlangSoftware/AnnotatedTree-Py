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
                 path: str=None):
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
        self.__file_description = fileDescription

    def getFileDescription(self) -> FileDescription:
        return self.__file_description

    def reload(self):
        self.readFromFile(self.__file_description.getFileName(self.__file_description.getPath()))

    def readFromFile(self, fileName: str):
        input_file = open(fileName, encoding="utf8")
        line = input_file.readline().strip()
        if "(" in line and ")" in line:
            line = line[line.index("(") + 1:line.rindex(")")].strip()
            self.root = ParseNodeDrawable(None, line, False, 0)
        else:
            self.root = None
        input_file.close()

    def nextTree(self, count: int):
        if self.__file_description.nextFileExists(count):
            self.__file_description.addToIndex(count)
            self.reload()

    def previousTree(self, count: int):
        if self.__file_description.previousFileExists(count):
            self.__file_description.addToIndex(-count)
            self.reload()

    def save(self):
        output_file = open(self.__file_description.getFileName(), mode='w', encoding="utf8")
        output_file.write("( " + self.__str__() + " )\n")
        output_file.close()

    def saveWithPath(self, newPath: str):
        output_file = open(self.__file_description.getFileName(newPath), mode='w', encoding="utf8")
        output_file.write("( " + self.__str__() + " )\n")
        output_file.close()

    def maxDepth(self) -> int:
        if isinstance(self.root, ParseNodeDrawable):
            return self.root.maxDepth()

    def moveLeft(self, node: ParseNode):
        if self.root != node:
            self.root.moveLeft(node)

    def moveRight(self, node: ParseNode):
        if self.root != node:
            self.root.moveRight(node)

    def layerExists(self, viewLayerType: ViewLayerType) -> bool:
        if self.root is not None and isinstance(self.root, ParseNodeDrawable):
            return self.root.layerExists(viewLayerType)
        else:
            return False

    def layerAll(self, viewLayerType: ViewLayerType) -> bool:
        if self.root is not None and isinstance(self.root, ParseNodeDrawable):
            return self.root.layerAll(viewLayerType)
        else:
            return False

    def clearLayer(self, viewLayerType: ViewLayerType):
        if self.root is not None and isinstance(self.root, ParseNodeDrawable):
            self.root.clearLayer(viewLayerType)

    def generateAnnotatedSentence(self, language: str=None) -> AnnotatedSentence:
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
        result = ParseTree(ParseNode(self.root.getData()))
        self.root.generateParseNode(result.getRoot(), surfaceForm)
        return result

    def extractNodesWithVerbs(self, wordNet: WordNet) -> list:
        node_drawable_collector = NodeDrawableCollector(self.root, IsVerbNode(wordNet))
        return node_drawable_collector.collect()

    def extractNodesWithPredicateVerbs(self, wordNet: WordNet) -> list:
        node_drawable_collector = NodeDrawableCollector(self.root, IsPredicateVerbNode(wordNet))
        return node_drawable_collector.collect()
