from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.Layer.MultiWordLayer import MultiWordLayer
from abc import abstractmethod


class MultiWordMultiItemLayer(MultiWordLayer):

    @abstractmethod
    def getLayerSize(self, viewLayer: ViewLayerType) -> int:
        pass

    def getLayerInfoAt(self, viewLayer: ViewLayerType, index: int) -> str:
        pass
