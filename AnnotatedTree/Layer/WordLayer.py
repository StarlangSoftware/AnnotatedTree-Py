class WordLayer:

    layer_value: str
    layer_name: str

    def getLayerValue(self) -> str:
        return self.layer_value

    def getLayerName(self) -> str:
        return self.layer_name

    def getLayerDescription(self) -> str:
        return "{" + self.layer_name + "=" + self.layer_value + "}"
