from AnnotatedSentence.ViewLayerType import ViewLayerType
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse

from AnnotatedTree.Layer.MultiWordMultiItemLayer import MultiWordMultiItemLayer


class MorphologicalAnalysisLayer(MultiWordMultiItemLayer):

    def __init__(self, layerValue: str):
        self.layer_name = "morphologicalAnalysis"
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        self.items = []
        if isinstance(layerValue, str):
            self.layer_value = layerValue
            if layerValue is not None:
                split_words = self.layer_value.split(" ")
                for word in split_words:
                    self.items.append(MorphologicalParse(word))
        elif isinstance(layerValue, MorphologicalParse):
            parse = layerValue
            self.layer_value = parse.getTransitionList()
            self.items.append(parse)

    def getLayerSize(self, viewLayer: ViewLayerType) -> int:
        size = 0
        if viewLayer == ViewLayerType.PART_OF_SPEECH:
            for parse in self.items:
                if isinstance(parse, MorphologicalParse):
                    size += parse.tagSize()
        elif viewLayer == ViewLayerType.INFLECTIONAL_GROUP:
            for parse in self.items:
                if isinstance(parse, MorphologicalParse):
                    size += parse.size()
        return size

    def getLayerInfoAt(self, viewLayer: ViewLayerType, index: int) -> str:
        size = 0
        if viewLayer == ViewLayerType.PART_OF_SPEECH:
            for parse in self.items:
                if isinstance(parse, MorphologicalParse) and index < size + parse.tagSize():
                    return parse.getTag(index - size)
                size += parse.tagSize()
            return None
        elif viewLayer == ViewLayerType.INFLECTIONAL_GROUP:
            for parse in self.items:
                if isinstance(parse, MorphologicalParse) and index < size + parse.size():
                    return parse.getInflectionalGroupString(index - size)
                size += parse.size()
            return None
        return None
