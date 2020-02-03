from PropBank.Argument import Argument

from AnnotatedTree.Layer.SingleWordLayer import SingleWordLayer


class TurkishPropbankLayer(SingleWordLayer):

    __propbank: Argument

    def __init__(self, layerValue: str):
        self.layerName = "propbank"
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        self.layerValue = layerValue
        self.__propbank = Argument(layerValue)

    def getArgument(self) -> Argument:
        return self.__propbank

    def getLayerValue(self) -> str:
        return self.__propbank.getArgumentType() + "$" + self.__propbank.getId()
