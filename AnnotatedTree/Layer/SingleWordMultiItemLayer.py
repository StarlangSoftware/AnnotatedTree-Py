from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.Layer.SingleWordLayer import SingleWordLayer


class SingleWordMultiItemLayer(SingleWordLayer):

    items: list

    def getItemAt(self, index: int) -> object:
        """
        Returns the property at position index for the word.
        :param index: Position of the property
        """
        if index < len(self.items):
            return self.items[index]
        else:
            return None

    def getLayerSize(self, viewLayer: ViewLayerType):
        """
        Returns the total number of properties for the word in the node.
        :param viewLayer: Not used.
        :return: Total number of properties for the word in the node.
        """
        return len(self.items)
