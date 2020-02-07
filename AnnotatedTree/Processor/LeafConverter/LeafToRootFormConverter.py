from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.LeafConverter.LeafToStringConverter import LeafToStringConverter


class LeafToRootFormConverter(LeafToStringConverter):

    def leafConverter(self, parseNodeDrawable: ParseNodeDrawable) -> str:
        layerInfo = parseNodeDrawable.getLayerInfo()
        rootWords = " "
        for i in range(layerInfo.getNumberOfWords()):
            root = layerInfo.getMorphologicalParseAt(i).getWord().getName()
            if root is not None and len(root) != 0:
                rootWords += " " + root
        return rootWords
