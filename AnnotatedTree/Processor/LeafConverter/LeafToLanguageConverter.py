from AnnotatedSentence.ViewLayerType import ViewLayerType
from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.LeafConverter.LeafToStringConverter import LeafToStringConverter


class LeafToLanguageConverter(LeafToStringConverter):

    view_layer_type: ViewLayerType

    def leafConverter(self, leafNode: ParseNodeDrawable) -> str:
        """
        Converts the data in the leaf node to string, except shortcuts to parentheses are converted to its normal forms,
        '*', '0', '-NONE-' are converted to empty string.
        :param leafNode: Node to be converted to string.
        :return: String form of the data, except shortcuts to parentheses are converted to its normal forms,
        '*', '0', '-NONE-' are converted to empty string.
        """
        layer_data = leafNode.getLayerData(self.view_layer_type)
        parent_layer_data = leafNode.getParent().getLayerData(self.view_layer_type)
        if layer_data is not None:
            if "*" in layer_data or (layer_data == "0" and parent_layer_data == "-NONE-"):
                return ""
            else:
                return " " + layer_data.replace("-LRB-", "(").replace("-RRB-", ")").replace("-LSB-", "[").\
                    replace("-RSB-", "]").replace("-LCB-", "{").replace("-RCB-", "}").replace("-lrb-", "(").\
                    replace("-rrb-", ")").replace("-lsb-", "[").replace("-rsb-", "]").replace("-lcb", "{").\
                    replace("-rcb-", "}")
        else:
            return ""
