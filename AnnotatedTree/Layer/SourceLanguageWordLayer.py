from AnnotatedTree.Layer.SingleWordLayer import SingleWordLayer


class SourceLanguageWordLayer(SingleWordLayer):

    def __init__(self, layerValue: str):
        self.setLayerValue(layerValue)
