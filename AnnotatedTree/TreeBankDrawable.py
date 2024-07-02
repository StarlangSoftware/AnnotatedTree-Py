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
        """
        A constructor of {@link TreeBankDrawable} class which reads all {@link ParseTreeDrawable} files inside the given
        folder. For each file inside that folder, the constructor creates a ParseTreeDrawable and puts in inside the list
        parseTrees.
        :param folder: Folder where all parseTrees reside.
        """
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
        """
        Accessor for the parseTrees attribute
        :return: ParseTrees attribute
        """
        return self.parse_trees

    def get(self, index: int) -> ParseTreeDrawable:
        """
        Accessor for a specific tree with the given position in the array.
        :param index: Index of the parseTree.
        :return: Tree that is in the position index
        """
        return self.parse_trees[index]

    def clearLayer(self, layerType: ViewLayerType):
        """
        Clears the given layer for all nodes in all trees
        :param layerType: Layer name
        """
        for tree in self.parse_trees:
            if isinstance(tree, ParseTreeDrawable):
                tree.clearLayer(layerType)
                tree.save()

    def removeTree(self, index: int):
        """
        Removes a tree with the given position from the treebank.
        :param index: Position of the tree to be removed.
        """
        self.parse_trees.pop(index)
