from AnnotatedSentence.ViewLayerType import ViewLayerType
from MorphologicalAnalysis.MetamorphicParse import MetamorphicParse

from AnnotatedTree.Layer.MetaMorphemesMovedLayer import MetaMorphemesMovedLayer


class MetaMorphemeLayer(MetaMorphemesMovedLayer):

    def __init__(self, layerValue: str):
        super().__init__(layerValue)
        self.layerName = "metaMorphemes"

    def setLayerValueWithMetamorphicParse(self, layerValue: MetamorphicParse):
        if isinstance(layerValue, MetamorphicParse):
            parse = layerValue
            self.layerValue = parse.__str__()
            self.items = []
            if layerValue is not None:
                splitWords = self.layerValue.split(" ")
                for word in splitWords:
                    self.items.append(MetamorphicParse(word))

    def getLayerInfoFrom(self, index: int) -> str:
        size = 0
        for parse in self.items:
            if isinstance(parse, MetamorphicParse) and index < size + parse.size():
                result = parse.getMetaMorpheme(index - size)
                index = index + 1
                while index < size + parse.size():
                    result = result + "+" + parse.getMetaMorpheme(index - size)
                    index = index + 1
                return result
            size += parse.size()
        return None

    def metaMorphemeRemoveFromIndex(self, index: int) -> MetamorphicParse:
        if 0 <= index < self.getLayerSize(ViewLayerType.META_MORPHEME):
            size = 0
            for parse in self.items:
                if isinstance(parse, MetamorphicParse) and index < size + parse.size():
                    parse.removeMetaMorphemeFromIndex(index - size)
                    return parse
            size += parse.size()
        return None
