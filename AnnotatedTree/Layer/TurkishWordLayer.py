from AnnotatedTree.Layer.TargetLanguageWordLayer import TargetLanguageWordLayer


class TurkishWordLayer(TargetLanguageWordLayer):

    def __init__(self, layerValue: str):
        super().__init__(layerValue)
        self.layer_name = "turkish"
