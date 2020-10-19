from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.Layer.MultiWordLayer import MultiWordLayer


class TargetLanguageWordLayer(MultiWordLayer):

    def __init__(self, layerValue: str):
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        self.items = []
        self.layerValue = layerValue
        if layerValue is not None:
            splitWords = layerValue.split(" ")
            self.items.extend(splitWords)

    def getLayerSize(self, viewLayer: ViewLayerType) -> int:
        return 0

    def getLayerInfoAt(self, viewLayer: ViewLayerType, index: int) -> str:
        return None
