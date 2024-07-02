from AnnotatedSentence.ViewLayerType import ViewLayerType
from MorphologicalAnalysis.MetamorphicParse import MetamorphicParse

from AnnotatedTree.Layer.MultiWordMultiItemLayer import MultiWordMultiItemLayer


class MetaMorphemesMovedLayer(MultiWordMultiItemLayer):

    def __init__(self, layerValue: str):
        """
        Constructor for the metaMorphemesMoved layer. Sets the metamorpheme information for multiple words in the node.
        :param layerValue: Layer value for the metaMorphemesMoved information. Consists of metamorpheme information of
                       multiple words separated via space character.
        """
        self.layer_name = "metaMorphemesMoved"
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        """
        Sets the layer value to the string form of the given parse.
        :param layerValue: New metamorphic parse.
        """
        self.items = []
        self.layer_value = layerValue
        if layerValue is not None:
            split_words = layerValue.split(" ")
            for word in split_words:
                self.items.append(MetamorphicParse(word))

    def getLayerSize(self, viewLayer: ViewLayerType) -> int:
        """
        Returns the total number of metamorphemes in the words in the node.
        :param viewLayer: Not used.
        :return: Total number of metamorphemes in the words in the node.
        """
        size = 0
        for parse in self.items:
            if isinstance(parse, MetamorphicParse):
                size += parse.size()
        return size

    def getLayerInfoAt(self, viewLayer: ViewLayerType, index: int) -> str:
        """
        Returns the metamorpheme at position index in the metamorpheme list.
        :param viewLayer: Not used.
        :param index: Position in the metamorpheme list.
        :return: The metamorpheme at position index in the metamorpheme list.
        """
        size = 0
        for parse in self.items:
            if isinstance(parse, MetamorphicParse) and index < size + parse.size():
                return parse.getMetaMorpheme(index - size)
            size += parse.size()
        return None
