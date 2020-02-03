from AnnotatedTree.Layer.MultiWordLayer import MultiWordLayer


class TurkishSemanticLayer(MultiWordLayer):

    def __init__(self, layerValue: str):
        self.layerName = "semantics"
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        self.items = []
        self.layerValue = layerValue
        if layerValue is not None:
            splitMeanings = layerValue.split("\\$")
            self.items.extend(splitMeanings)
