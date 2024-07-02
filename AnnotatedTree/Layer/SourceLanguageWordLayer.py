from AnnotatedTree.Layer.SingleWordLayer import SingleWordLayer


class SourceLanguageWordLayer(SingleWordLayer):

    def __init__(self, layerValue: str):
        """
        Sets the name of the word
        :param layerValue: Name of the word
        """
        self.setLayerValue(layerValue)
