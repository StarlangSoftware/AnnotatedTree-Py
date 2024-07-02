from PropBank.Argument import Argument

from AnnotatedTree.Layer.SingleWordMultiItemLayer import SingleWordMultiItemLayer


class EnglishPropbankLayer(SingleWordMultiItemLayer):

    def __init__(self, layerValue: str):
        """
        Constructor for the propbank layer for English language.
        :param layerValue: Value for the English propbank layer.
        """
        self.layer_name = "englishPropbank"
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        """
        Sets the value for the propbank layer in a node. Value may consist of multiple propbank information separated via
        '#' character. Each propbank value consists of argumentType and id info separated via '$' character.
        :param layerValue: New layer info
        """
        self.items = []
        self.layer_value = layerValue
        if layerValue is not None:
            split_words = layerValue.split("#")
            for word in split_words:
                self.items.append(Argument(word))
