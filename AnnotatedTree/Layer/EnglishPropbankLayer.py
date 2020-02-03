from PropBank.Argument import Argument

from AnnotatedTree.Layer.SingleWordMultiItemLayer import SingleWordMultiItemLayer


class EnglishPropbankLayer(SingleWordMultiItemLayer):

    def __init__(self, layerValue: str):
        self.layerName = "englishPropbank"
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        self.items = []
        self.layerValue = layerValue
        if layerValue is not None:
            splitWords = layerValue.split("#")
            for word in splitWords:
                self.items.append(Argument(word))
