class WordLayer:

    layerValue: str
    layerName: str

    def getLayerValue(self) -> str:
        return self.layerValue

    def getLayerName(self) -> str:
        return self.layerName

    def getLayerDescription(self) -> str:
        return "{" + self.layerName + "=" + self.layerValue + "}"
