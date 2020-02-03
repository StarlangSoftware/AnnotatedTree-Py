from NamedEntityRecognition.NamedEntityType import NamedEntityType

from AnnotatedTree.Layer.SingleWordLayer import SingleWordLayer


class NERLayer(SingleWordLayer):

    __namedEntity: NamedEntityType

    def __init__(self, layerValue: str):
        self.layerName = "namedEntity"
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        self.layerValue = layerValue
        self.__namedEntity = NamedEntityType.getNamedEntityType(layerValue)

    def getLayerValue(self) -> str:
        return NamedEntityType.getNamedEntityString(self.__namedEntity)
