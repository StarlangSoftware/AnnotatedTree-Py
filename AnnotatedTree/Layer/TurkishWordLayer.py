from AnnotatedTree.Layer.TargetLanguageWordLayer import TargetLanguageWordLayer


class TurkishWordLayer(TargetLanguageWordLayer):

    def __init__(self, layerValue: str):
        super().TargetLanguageWordLayer(layerValue)
        self.layerName = "turkish"
