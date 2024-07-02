class WordLayer:

    layer_value: str
    layer_name: str

    def getLayerValue(self) -> str:
        """
        Accessor for the layerValue attribute.
        :return: LayerValue attribute.
        """
        return self.layer_value

    def getLayerName(self) -> str:
        """
        Accessor for the layerName attribute.
        :return: LayerName attribute.
        """
        return self.layer_name

    def getLayerDescription(self) -> str:
        """
        Returns string form of the word layer.
        :return: String form of the word layer.
        """
        return "{" + self.layer_name + "=" + self.layer_value + "}"
