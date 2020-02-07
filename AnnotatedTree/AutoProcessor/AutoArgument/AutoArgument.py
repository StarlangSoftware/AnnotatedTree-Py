from abc import abstractmethod

from AnnotatedSentence.ViewLayerType import ViewLayerType
from Dictionary.Word import Word
from PropBank.ArgumentType import ArgumentType
from PropBank.Frameset import Frameset

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.ParseTreeDrawable import ParseTreeDrawable
from AnnotatedTree.Processor.Condition.IsTransferable import IsTransferable
from AnnotatedTree.Processor.NodeDrawableCollector import NodeDrawableCollector


class AutoArgument:

    secondLanguage: ViewLayerType

    @abstractmethod
    def autoDetectArgument(self, parseNode: ParseNodeDrawable, argumentType: ArgumentType) -> bool:
        pass

    def __init__(self, secondLanguage: ViewLayerType):
        self.secondLanguage = secondLanguage

    def autoArgument(self, parseTree: ParseTreeDrawable, frameset: Frameset):
        nodeDrawableCollector = NodeDrawableCollector(parseTree.getRoot(), IsTransferable(self.secondLanguage))
        leafList = nodeDrawableCollector.collect()
        for parseNode in leafList:
            if isinstance(parseNode, ParseNodeDrawable) and parseNode.getLayerData(ViewLayerType.PROPBANK) is None:
                for argumentType in ArgumentType:
                    if frameset.containsArgument(argumentType) and self.autoDetectArgument(parseNode, argumentType):
                        parseNode.getLayerInfo().setLayerData(ViewLayerType.PROPBANK,
                                                              ArgumentType.getPropbankType(argumentType))
                if Word.isPunctuationSymbol(parseNode.getLayerData(self.secondLanguage)):
                    parseNode.getLayerInfo().setLayerData(ViewLayerType.PROPBANK, "NONE")
        parseTree.save()
