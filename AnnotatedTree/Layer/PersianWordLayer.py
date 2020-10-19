from AnnotatedTree.Layer.TargetLanguageWordLayer import TargetLanguageWordLayer


class PersianWordLayer(TargetLanguageWordLayer):

    def __init__(self, layerValue: str):
        super().__init__(layerValue)
        self.layerName = "persian"
