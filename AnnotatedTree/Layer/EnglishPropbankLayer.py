from PropBank.Argument import Argument

from AnnotatedTree.Layer.SingleWordMultiItemLayer import SingleWordMultiItemLayer


class EnglishPropbankLayer(SingleWordMultiItemLayer):

    def __init__(self, layerValue: str):
        self.layer_name = "englishPropbank"
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        self.items = []
        self.layer_value = layerValue
        if layerValue is not None:
            split_words = layerValue.split("#")
            for word in split_words:
                self.items.append(Argument(word))
