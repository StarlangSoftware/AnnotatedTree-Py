from AnnotatedTree.Layer.TargetLanguageWordLayer import TargetLanguageWordLayer


class PersianWordLayer(TargetLanguageWordLayer):

    def __init__(self, layerValue: str):
        super().TargetLanguageWordLayer(layerValue)
        self.layerName = "persian"
