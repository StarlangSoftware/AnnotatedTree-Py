from AnnotatedSentence.ViewLayerType import ViewLayerType
from MorphologicalAnalysis.MetamorphicParse import MetamorphicParse

from AnnotatedTree.Layer.MultiWordMultiItemLayer import MultiWordMultiItemLayer


class MetaMorphemesMovedLayer(MultiWordMultiItemLayer):

    def __init__(self, layerValue: str):
        self.layerName = "metaMorphemesMoved"
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        self.items = []
        self.layerValue = layerValue
        if layerValue is not None:
            splitWords = layerValue.split(" ")
            for word in splitWords:
                self.items.append(MetamorphicParse(word))

    def getLayerSize(self, viewLayer: ViewLayerType) -> int:
        size = 0
        for parse in self.items:
            if isinstance(parse, MetamorphicParse):
                size += parse.size()
        return size

    def getLayerInfoAt(self, viewLayer: ViewLayerType, index: int) -> str:
        size = 0
        for parse in self.items:
            if isinstance(parse, MetamorphicParse) and index < size + parse.size():
                return parse.getMetaMorpheme(index - size)
            size += parse.size()
        return None
