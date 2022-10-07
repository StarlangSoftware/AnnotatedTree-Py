from AnnotatedTree.Layer.WordLayer import WordLayer


class SingleWordLayer(WordLayer):

    def setLayerValue(self, layerValue: str):
        self.layer_value = layerValue
