from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.NodeModification.NodeModifier import NodeModifier


class ConvertToLayeredFormat(NodeModifier):

    def modifier(self, parseNode: ParseNodeDrawable):
        if parseNode.isLeaf():
            name = parseNode.getData().getName()
            parseNode.clearLayers()
            parseNode.getLayerInfo().setLayerData(ViewLayerType.ENGLISH_WORD, name)
            parseNode.clearData()
