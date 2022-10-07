from AnnotatedTree.Layer.SingleWordLayer import SingleWordLayer


class EnglishSemanticLayer(SingleWordLayer):

    def __init__(self, layerValue: str):
        self.layer_name = "englishSemantics"
        self.setLayerValue(layerValue)
