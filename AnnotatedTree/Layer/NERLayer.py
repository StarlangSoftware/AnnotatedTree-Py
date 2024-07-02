from NamedEntityRecognition.NamedEntityType import NamedEntityType

from AnnotatedTree.Layer.SingleWordLayer import SingleWordLayer


class NERLayer(SingleWordLayer):

    __named_entity: NamedEntityType

    def __init__(self, layerValue: str):
        """
        Constructor for the named entity layer. Sets single named entity information for multiple words in
        the node.
        :param layerValue: Layer value for the named entity information. Consists of single named entity information
                       of multiple words.
        """
        self.layer_name = "namedEntity"
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        """
        Sets the layer value for Named Entity layer. Converts the string form to a named entity.
        :param layerValue: New value for Named Entity layer.
        """
        self.layer_value = layerValue
        self.__named_entity = NamedEntityType.getNamedEntityType(layerValue)

    def getLayerValue(self) -> str:
        """
        Get the string form of the named entity value. Converts named entity type to string form.
        :return: String form of the named entity value.
        """
        return NamedEntityType.getNamedEntityString(self.__named_entity)
