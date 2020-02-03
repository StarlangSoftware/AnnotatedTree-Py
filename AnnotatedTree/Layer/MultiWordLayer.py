from abc import abstractmethod
from AnnotatedTree.Layer.WordLayer import WordLayer


class MultiWordLayer(WordLayer):

    items: list

    def getItemAt(self, index: int) -> object:
        if index < len(self.items):
            return self.items[index]
        else:
            return None

    def size(self) -> int:
        return len(self.items)

    @abstractmethod
    def setLayerValue(self, layerValue: str):
        pass
