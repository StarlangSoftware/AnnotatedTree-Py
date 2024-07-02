from AnnotatedTree.Layer.SourceLanguageWordLayer import SourceLanguageWordLayer


class EnglishWordLayer(SourceLanguageWordLayer):

    def __init__(self, layerValue: str):
        """
        Constructor for the word layer for English language. Sets the surface form.
        :param layerValue: Value for the word layer.
        """
        super().__init__(layerValue)
        self.layer_name = "english"
