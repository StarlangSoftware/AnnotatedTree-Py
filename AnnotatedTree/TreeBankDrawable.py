import os
import re

from AnnotatedSentence.ViewLayerType import ViewLayerType
from Corpus.FileDescription import FileDescription
from ParseTree.TreeBank import TreeBank

from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable


class TreeBankDrawable(TreeBank):

    def __init__(self,
                 folder: str = None,
                 pattern: str = None):
        self.parse_trees = []
        if folder is not None:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    fileName = os.path.join(root, file)
                    if (pattern is None or pattern in fileName) and re.match("\\d+\\.", file):
                        parse_tree = ParseTreeDrawable(fileName)
                        if parse_tree.getRoot() is not None:
                            parse_tree.setFileDescription(FileDescription(root, file))
                            self.parse_trees.append(parse_tree)

    def getParseTrees(self) -> list:
        return self.parse_trees

    def get(self, index: int) -> ParseTreeDrawable:
        return self.parse_trees[index]

    def clearLayer(self, layerType: ViewLayerType):
        for tree in self.parse_trees:
            if isinstance(tree, ParseTreeDrawable):
                tree.clearLayer(layerType)
                tree.save()

    def removeTree(self, index: int):
        self.parse_trees.pop(index)
