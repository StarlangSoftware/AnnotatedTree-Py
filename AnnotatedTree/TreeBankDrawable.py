import os
import re

from AnnotatedSentence.ViewLayerType import ViewLayerType
from Corpus.FileDescription import FileDescription
from ParseTree.TreeBank import TreeBank

from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable


class TreeBankDrawable(TreeBank):

    def __init__(self, folder: str = None, pattern: str = None):
        self.parseTrees = []
        if str is not None:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    fileName = os.path.join(root, file)
                    if (pattern is None or pattern in fileName) and re.match("\\d+\\.", file):
                        parseTree = ParseTreeDrawable(fileName)
                        if parseTree.getRoot() is not None:
                            parseTree.setName(fileName)
                            parseTree.setFileDescription(FileDescription(root, file))
                            self.parseTrees.append(parseTree)

    def getParseTrees(self) -> list:
        return self.parseTrees

    def get(self, index: int) -> ParseTreeDrawable:
        return self.parseTrees[index]

    def clearLayer(self, layerType: ViewLayerType):
        for tree in self.parseTrees:
            if isinstance(tree, ParseTreeDrawable):
                tree.clearLayer(layerType)
                tree.save()

    def removeTree(self, index: int):
        self.parseTrees.pop(index)
