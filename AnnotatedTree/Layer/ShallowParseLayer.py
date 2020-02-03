from AnnotatedTree.Layer.MultiWordLayer import MultiWordLayer


class ShallowParseLayer(MultiWordLayer):

    def __init__(self, layerValue: str):
        self.layerName = "shallowParse"
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        self.items = []
        self.layerValue = layerValue
        if layerValue is not None:
            splitParse = layerValue.split(" ")
            self.items.extend(splitParse)
