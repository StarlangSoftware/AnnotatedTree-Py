from __future__ import annotations

from AnnotatedSentence.ViewLayerType import ViewLayerType
from NamedEntityRecognition.Gazetteer import Gazetteer
from ParseTree.ParseNode import ParseNode
from ParseTree.Symbol import Symbol

from AnnotatedTree.LayerInfo import LayerInfo


class ParseNodeDrawable(ParseNode):

    layers: LayerInfo
    depth: int

    def __init__(self,
                 parent: ParseNodeDrawable,
                 line: str,
                 isLeaf: bool,
                 depth: int):
        """
        Constructs a ParseNodeDrawable from a single line. If the node is a leaf node, it only sets the data. Otherwise,
        splits the line w.r.t. spaces and parenthesis and calls itself recursively to generate its child parseNodes.
        :param parent: The parent node of this node.
        :param line: The input line to create this parseNode.
        :param isLeaf: True, if this node is a leaf node; false otherwise.
        :param depth: Depth of the node.
        """
        self.children = []
        self.parent = parent
        self.layers = None
        self.data = None
        self.depth = depth
        parenthesis_count = 0
        child_line = ""
        if isLeaf:
            if "{" not in line:
                self.data = Symbol(line)
            else:
                self.layers = LayerInfo(line)
        else:
            self.data = Symbol(line[1: line.index(" ")])
            if line.index(")") == line.rindex(")"):
                self.children.append(ParseNodeDrawable(self, line[line.index(" ") + 1: line.index(")")],
                                                       True, depth + 1))
            else:
                for i in range(line.index(" ") + 1, len(line)):
                    if line[i] != " " or parenthesis_count > 0:
                        child_line = child_line + line[i]
                    if line[i] == "(":
                        parenthesis_count = parenthesis_count + 1
                    elif line[i] == ")":
                        parenthesis_count = parenthesis_count - 1
                    if parenthesis_count == 0 and len(child_line) != 0:
                        self.children.append(ParseNodeDrawable(self, child_line.strip(), False, depth + 1))
                        child_line = ""

    def getLayerInfo(self) -> LayerInfo:
        """
        Accessor for layers attribute
        :return: Layers attribute
        """
        return self.layers

    def getData(self) -> Symbol:
        """
        Returns the data. Either the node is a leaf node, in which case English word layer is returned; or the node is
        a nonleaf node, in which case the node tag is returned.
        :return: English word for leaf node, constituency tag for non-leaf node.
        """
        if self.layers is None:
            return super().getData()
        else:
            return Symbol(self.getLayerData(ViewLayerType.ENGLISH_WORD))

    def clearLayers(self):
        """
        Clears the layers hash map.
        """
        self.layers = LayerInfo()

    def clearLayer(self, layerType: ViewLayerType):
        """
        Recursive method to clear a given layer.
        :param layerType: Name of the layer to be cleared
        """
        if len(self.children) == 0 and self.layerExists(layerType):
            self.layers.removeLayer(layerType)
        for child in self.children:
            if isinstance(child, ParseNodeDrawable):
                child.clearLayer(layerType)

    def clearData(self):
        """
        Clears the node tag.
        """
        self.data = None

    def setDataAndClearLayers(self, data: Symbol):
        """
        Setter for the data attribute and also clears all layers.
        :param data: New data field.
        """
        super().setData(data)
        self.layers = None

    def setData(self, data: Symbol):
        """
        Mutator for the data field. If the layers is null, its sets the data field, otherwise it sets the English layer
        to the given value.
        :param data: Data to be set.
        """
        if self.layers is None:
            super().setData(data)
        else:
            self.layers.setLayerData(ViewLayerType.ENGLISH_WORD, self.data.getName())

    def headWord(self, viewLayerType: ViewLayerType) -> str:
        """
        Returns the layer value of the head child of this node.
        :param viewLayerType: Layer name
        :return: Layer value of the head child of this node.
        """
        if len(self.children) > 0:
            return self.headChild().headWord(viewLayerType)
        else:
            return self.getLayerData(viewLayerType)

    def getLayerData(self, viewLayer: ViewLayerType = None) -> str:
        """
        Returns the layer value of a given layer.
        :param viewLayer: Layer name
        :return: Value of the given layer
        """
        if viewLayer is None:
            if self.data is not None:
                return self.data.getName()
            return self.layers.getLayerDescription()
        else:
            if viewLayer == ViewLayerType.WORD or self.layers is None:
                return self.data.getName()
            else:
                return self.layers.getLayerData(viewLayer)

    def getDepth(self):
        """
        Accessor for the depth attribute
        :return: Depth attribute
        """
        return self.depth

    def updateDepths(self, depth: int):
        """
        Recursive method which updates the depth attribute
        :param depth: Current depth to set.
        """
        self.depth = depth
        for child in self.children:
            if isinstance(child, ParseNodeDrawable):
                child.updateDepths(depth + 1)

    def maxDepth(self) -> int:
        """
        Calculates the maximum depth of the subtree rooted from this node.
        :return: The maximum depth of the subtree rooted from this node.
        """
        depth = self.depth
        for child in self.children:
            if isinstance(child, ParseNodeDrawable):
                if child.maxDepth() > depth:
                    depth = child.maxDepth()
        return depth

    def ancestorString(self) -> str:
        """
        Recursive method that returns the concatenation of all pos tags of all descendants of this node.
        :return: The concatenation of all pos tags of all descendants of this node.
        """
        if self.parent is None:
            return self.data.getName()
        else:
            if self.layers is None:
                return self.parent.ancestorString() + self.data.getName()
            else:
                return self.parent.ancestorString() + self.layers.getLayerData(ViewLayerType.ENGLISH_WORD)

    def layerExists(self, viewLayerType: ViewLayerType) -> bool:
        """
        Recursive method that checks if all nodes in the subtree rooted with this node has the annotation in the given
        layer.
        :param viewLayerType: Layer name
        :return: True if all nodes in the subtree rooted with this node has the annotation in the given layer, false
        otherwise.
        """
        if len(self.children) == 0:
            if self.getLayerData() is not None:
                return True
        else:
            for child in self.children:
                if isinstance(child, ParseNodeDrawable):
                    return True
        return False

    def isDummyNode(self) -> bool:
        """
        Checks if the current node is a dummy node or not. A node is a dummy node if its data contains '*', or its
        data is '0' and its parent is '-NONE-'.
        :return: True if the current node is a dummy node, false otherwise.
        """
        data = self.getLayerData(ViewLayerType.ENGLISH_WORD)
        if isinstance(self.parent, ParseNodeDrawable):
            parent_data = self.parent.getLayerData(ViewLayerType.ENGLISH_WORD)
        else:
            parent_data = None
        target_data = self.getLayerData(ViewLayerType.TURKISH_WORD)
        if data is not None and parent_data is not None:
            if target_data is not None and "*" in target_data:
                return True
            return "*" in data or (data == "0" and parent_data == "-NONE-")
        else:
            return False

    def layerAll(self, viewLayerType) -> bool:
        """
        Checks if all nodes in the subtree rooted with this node has annotation with the given layer.
        :param viewLayerType: Layer name
        :return: True if all nodes in the subtree rooted with this node has annotation with the given layer, false
        otherwise.
        """
        if len(self.children) == 0:
            if self.getLayerData(viewLayerType) is None and not self.isDummyNode():
                return False
        else:
            for child in self.children:
                if isinstance(child, ParseNodeDrawable):
                    if not child.layerAll(viewLayerType):
                        return False
        return True

    def toTurkishSentence(self) -> str:
        """
        Recursive method to convert the subtree rooted with this node to a string. All parenthesis types are converted to
        their regular forms.
        :return: String version of the subtree rooted with this node.
        """
        if len(self.children) == 0:
            if self.getLayerData(ViewLayerType.TURKISH_WORD) is not None and not self.isDummyNode():
                return " " + self.getLayerData(ViewLayerType.TURKISH_WORD).replace("-LRB-", "(").\
                    replace("-RRB-", ")").replace("-LSB-", "[").replace("-RSB-", "]").replace("-LCB-", "{").\
                    replace("-RCB-", "}").replace("-lrb-", "(").replace("-rrb-", ")").replace("-lsb-", "[").\
                    replace("-rsb-", "]").replace("-lcb", "{").replace("-rcb-", "}")
            else:
                return " "
        else:
            st = ""
            for child in self.children:
                if isinstance(child, ParseNodeDrawable):
                    st += child.toSentence()
            return st

    def checkGazetteer(self,
                       gazetteer: Gazetteer,
                       word: str):
        """
        Sets the NER layer according to the tag of the parent node and the word in the node. The word is searched in the
        gazetteer, if it exists, the NER info is replaced with the NER tag in the gazetter.
        :param gazetteer: Gazetteer where we search the word
        :param word: Word to be searched in the gazetteer
        """
        if gazetteer.contains(word) and self.getParent().getData().getName() == "NNP":
            self.getLayerInfo().setLayerData(ViewLayerType.NER, gazetteer.getName())
        if "'" in word and gazetteer.contains(word[:word.index("'")]) and self.getParent().getData().getName() == "NNP":
            self.getLayerInfo().setLayerData(ViewLayerType.NER, gazetteer.getName())

    def generateParseNode(self,
                          parseNode: ParseNode,
                          surfaceForm: bool):
        """
        Recursive method that sets the tag information of the given parse node with all descendants with respect to the
        morphological annotation of the current node with all descendants.
        :param parseNode: Parse node whose tag information will be changed.
        :param surfaceForm: If true, tag will be replaced with the surface form annotation.
        """
        if len(self.children) == 0:
            if surfaceForm:
                parseNode.setData(Symbol(self.getLayerData(ViewLayerType.TURKISH_WORD)))
            else:
                parseNode.setData(Symbol(self.getLayerInfo().getMorphologicalParseAt(0).getWord().getName()))
        else:
            parseNode.setData(self.data)
            for child in self.children:
                new_child = ParseNode("")
                parseNode.addChild(new_child)
                child.generateParseNode(new_child, surfaceForm)

    def __str__(self) -> str:
        if len(self.children) < 2:
            if len(self.children) < 1:
                return self.getLayerData()
            else:
                return "(" + self.data.getName() + " " + self.children[0].__str__() + ")"
        else:
            st = "(" + self.data.getName()
            for child in self.children:
                st = st + " " + child.__str__()
            return st + ") "
