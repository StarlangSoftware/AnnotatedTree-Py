from abc import abstractmethod

from AnnotatedSentence.ViewLayerType import ViewLayerType
from NamedEntityRecognition.AutoNER import AutoNER

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable
from AnnotatedTree.Processor.Condition.IsTransferable import IsTransferable
from AnnotatedTree.Processor.NodeDrawableCollector import NodeDrawableCollector


class TreeAutoNER(AutoNER):

    secondLanguage: ViewLayerType

    @abstractmethod
    def autoDetectPerson(self, parseTree: ParseTreeDrawable):
        pass

    @abstractmethod
    def autoDetectLocation(self, parseTree: ParseTreeDrawable):
        pass

    @abstractmethod
    def autoDetectOrganization(self, parseTree: ParseTreeDrawable):
        pass

    @abstractmethod
    def autoDetectMoney(self, parseTree: ParseTreeDrawable):
        pass

    @abstractmethod
    def autoDetectTime(self, parseTree: ParseTreeDrawable):
        pass

    def __init__(self, secondLanguage: ViewLayerType):
        self.secondLanguage = secondLanguage

    def autoNER(self, parseTree: ParseTreeDrawable):
        self.autoDetectPerson(parseTree)
        self.autoDetectLocation(parseTree)
        self.autoDetectOrganization(parseTree)
        self.autoDetectMoney(parseTree)
        self.autoDetectTime(parseTree)
        nodeDrawableCollector = NodeDrawableCollector(parseTree.getRoot(), IsTransferable(self.secondLanguage))
        leafList = nodeDrawableCollector.collect()
        for parseNode in leafList:
            if isinstance(parseNode, ParseNodeDrawable) and not parseNode.layerExists(ViewLayerType.NER):
                parseNode.getLayerInfo().setLayerData(ViewLayerType.NER, "NONE")
        parseTree.save()
