from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.Layer.MultiWordLayer import MultiWordLayer


class TargetLanguageWordLayer(MultiWordLayer):

    def __init__(self, layerValue: str):
        """
        Sets the surface form(s) of the word(s) possibly separated with space.
        :param layerValue: Surface form(s) of the word(s) possibly separated with space.
        """
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        """
        Sets the surface form(s) of the word(s). Value may consist of multiple surface form(s)
        :param layerValue: New layer info
        """
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
