from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.Layer.MultiWordLayer import MultiWordLayer


class TargetLanguageWordLayer(MultiWordLayer):

    def __init__(self, layerValue: str):
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        self.items = []
        self.layer_value = layerValue
        if layerValue is not None:
            split_words = layerValue.split(" ")
            self.items.extend(split_words)

    def getLayerSize(self, viewLayer: ViewLayerType) -> int:
        return 0

    def getLayerInfoAt(self,
                       viewLayer: ViewLayerType,
                       index: int) -> str:
        return None
