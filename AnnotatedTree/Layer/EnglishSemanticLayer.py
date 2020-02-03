from AnnotatedTree.Layer.SingleWordLayer import SingleWordLayer


class EnglishSemanticLayer(SingleWordLayer):

    def __init__(self, layerValue: str):
        self.layerName = "englishSemantics"
        self.setLayerValue(layerValue)
