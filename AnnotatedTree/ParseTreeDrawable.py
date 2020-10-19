from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.ViewLayerType import ViewLayerType
from Corpus.FileDescription import FileDescription
from ParseTree.ParseNode import ParseNode
from ParseTree.ParseTree import ParseTree
from WordNet.WordNet import WordNet

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.Condition.IsPredicateVerbNode import IsPredicateVerbNode
from AnnotatedTree.Processor.Condition.IsTurkishLeafNode import IsTurkishLeafNode
from AnnotatedTree.Processor.Condition.IsVerbNode import IsVerbNode
from AnnotatedTree.Processor.NodeDrawableCollector import NodeDrawableCollector


class ParseTreeDrawable(ParseTree):

    __fileDescription: FileDescription
    __name: str

    def __init__(self, fileDescription, path: str=None):
        if path is None:
            if isinstance(fileDescription, FileDescription):
                self.__fileDescription = fileDescription
                self.readFromFile(self.__fileDescription.getFileName(fileDescription.getPath()))
            elif isinstance(fileDescription, str):
                self.readFromFile(fileDescription)
        else:
            self.__fileDescription = FileDescription(path, fileDescription.getExtension(), fileDescription.getIndex())
            self.readFromFile(self.__fileDescription.getFileName(fileDescription.getPath()))

    def setFileDescription(self, fileDescription: FileDescription):
        self.__fileDescription = fileDescription

    def getFileDescription(self) -> FileDescription:
        return self.__fileDescription

    def reload(self):
        self.readFromFile(self.__fileDescription.getFileName(self.__fileDescription.getPath()))

    def readFromFile(self, fileName: str):
        inputFile = open(fileName, encoding="utf8")
        line = inputFile.readline().strip()
        if "(" in line and ")" in line:
            line = line[line.index("(") + 1:line.rindex(")")].strip()
            self.root = ParseNodeDrawable(None, line, False, 0)
        else:
            self.root = None
        inputFile.close()

    def setName(self, name: str):
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def nextTree(self, count: int):
        if self.__fileDescription.nextFileExists(count):
            self.__fileDescription.addToIndex(count)
            self.reload()

    def previousTree(self, count: int):
        if self.__fileDescription.previousFileExists(count):
            self.__fileDescription.addToIndex(-count)
            self.reload()

    def save(self):
        outputFile = open(self.__fileDescription.getFileName(), encoding="utf8")
        outputFile.write("(" + self.__str__() + ")\n")
        outputFile.close()

    def saveWithPath(self, newPath: str):
        outputFile = open(self.__fileDescription.getFileName(newPath), encoding="utf8")
        outputFile.write("(" + self.__str__() + ")\n")
        outputFile.close()

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

    def generateAnnotatedSentence(self) -> AnnotatedSentence:
        sentence = AnnotatedSentence()
        nodeDrawableCollector = NodeDrawableCollector(self.root, IsTurkishLeafNode())
        leafList = nodeDrawableCollector.collect()
        for parseNode in leafList:
            if isinstance(parseNode, ParseNodeDrawable):
                layers = parseNode.getLayerInfo()
                for i in range(layers.getNumberOfWords()):
                    sentence.addWord(layers.toAnnotatedWord(i))
        return sentence

    def extractNodesWithVerbs(self, wordNet: WordNet) -> list:
        nodeDrawableCollector = NodeDrawableCollector(self.root, IsVerbNode(wordNet))
        return nodeDrawableCollector.collect()

    def extractNodesWithPredicateVerbs(self, wordNet: WordNet) -> list:
        nodeDrawableCollector = NodeDrawableCollector(self.root, IsPredicateVerbNode(wordNet))
        return nodeDrawableCollector.collect()
