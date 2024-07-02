from abc import abstractmethod
from AnnotatedTree.Layer.WordLayer import WordLayer


class MultiWordLayer(WordLayer):

    items: list

    def getItemAt(self, index: int) -> object:
        """
        Returns the item (word or its property) at position index.
        :param index: Position of the item (word or its property).
        :return: The item at position index.
        """
        if index < len(self.items):
            return self.items[index]
        else:
            return None

    def size(self) -> int:
        """
        Returns number of items (words) in the items array list.
        :return: Number of items (words) in the items array list.
        """
        return len(self.items)

    @abstractmethod
    def setLayerValue(self, layerValue: str):
        pass
