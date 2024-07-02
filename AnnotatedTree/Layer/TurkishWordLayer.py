from AnnotatedTree.Layer.TargetLanguageWordLayer import TargetLanguageWordLayer


class TurkishWordLayer(TargetLanguageWordLayer):

    def __init__(self, layerValue: str):
        """
        Constructor for the word layer for Turkish language. Sets the surface form.
        :param layerValue: Value for the word layer.
        """
        super().__init__(layerValue)
        self.layer_name = "turkish"
