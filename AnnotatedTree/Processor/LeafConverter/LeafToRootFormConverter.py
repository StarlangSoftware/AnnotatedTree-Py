from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.LeafConverter.LeafToStringConverter import LeafToStringConverter


class LeafToRootFormConverter(LeafToStringConverter):

    def leafConverter(self, parseNodeDrawable: ParseNodeDrawable) -> str:
        """
        Converts the data in the leaf node to string. If there are multiple words in the leaf node, they are concatenated
        with space.
        :param parseNodeDrawable: Node to be converted to string.
        :return: String form of the data. If there are multiple words in the leaf node, they are concatenated
        with space.
        """
        layer_info = parseNodeDrawable.getLayerInfo()
        root_words = " "
        for i in range(layer_info.getNumberOfWords()):
            root = layer_info.getMorphologicalParseAt(i).getWord().getName()
            if root is not None and len(root) != 0:
                root_words += " " + root
        return root_words
