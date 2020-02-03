from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.Layer.SingleWordLayer import SingleWordLayer


class SingleWordMultiItemLayer(SingleWordLayer):

    items: list

    def getItemAt(self, index: int) -> object:
        if index < len(self.items):
            return self.items[index]
        else:
            return None

    def getLayerSize(self, viewLayer: ViewLayerType):
        return len(self.items)
