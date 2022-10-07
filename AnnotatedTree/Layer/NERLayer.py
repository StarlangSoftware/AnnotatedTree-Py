from NamedEntityRecognition.NamedEntityType import NamedEntityType

from AnnotatedTree.Layer.SingleWordLayer import SingleWordLayer


class NERLayer(SingleWordLayer):

    __named_entity: NamedEntityType

    def __init__(self, layerValue: str):
        self.layer_name = "namedEntity"
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        self.layer_value = layerValue
        self.__named_entity = NamedEntityType.getNamedEntityType(layerValue)

    def getLayerValue(self) -> str:
        return NamedEntityType.getNamedEntityString(self.__named_entity)
