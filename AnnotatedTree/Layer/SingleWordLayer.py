from AnnotatedTree.Layer.WordLayer import WordLayer


class SingleWordLayer(WordLayer):

    def setLayerValue(self, layerValue: str):
        """
        Sets the property of the word
        :param layerValue: Layer info
        """
        self.layer_value = layerValue
