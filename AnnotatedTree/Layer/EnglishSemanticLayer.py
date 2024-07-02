from AnnotatedTree.Layer.SingleWordLayer import SingleWordLayer


class EnglishSemanticLayer(SingleWordLayer):

    def __init__(self, layerValue: str):
        """
        Constructor for the semantic layer for English language. Sets the layer value to the synset id defined in English
        WordNet.
        :param layerValue: Value for the English semantic layer.
        """
        self.layer_name = "englishSemantics"
        self.setLayerValue(layerValue)
