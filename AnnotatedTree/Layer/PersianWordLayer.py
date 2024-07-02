from AnnotatedTree.Layer.TargetLanguageWordLayer import TargetLanguageWordLayer


class PersianWordLayer(TargetLanguageWordLayer):

    def __init__(self, layerValue: str):
        """
        Constructor for the word layer for Persian language. Sets the surface form.
        :param layerValue: Value for the word layer.
        """
        super().__init__(layerValue)
        self.layer_name = "persian"
