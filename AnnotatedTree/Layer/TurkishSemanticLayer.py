from AnnotatedTree.Layer.MultiWordLayer import MultiWordLayer


class TurkishSemanticLayer(MultiWordLayer):

    def __init__(self, layerValue: str):
        self.layer_name = "semantics"
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        self.items = []
        self.layer_value = layerValue
        if layerValue is not None:
            split_meanings = layerValue.split("\\$")
            self.items.extend(split_meanings)
