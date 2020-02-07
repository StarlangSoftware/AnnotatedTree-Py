from AnnotatedSentence.ViewLayerType import ViewLayerType
from AnnotatedTree.ParseNodeDrawable import ParseNodeDrawable
from AnnotatedTree.Processor.LeafConverter.LeafToStringConverter import LeafToStringConverter


class LeafToLanguageConverter(LeafToStringConverter):

    viewLayerType: ViewLayerType

    def leafConverter(self, leafNode: ParseNodeDrawable) -> str:
        layerData = leafNode.getLayerData(self.viewLayerType)
        parentLayerData = leafNode.getParent().getLayerData(self.viewLayerType)
        if layerData is not None:
            if "*" in layerData or (layerData == "0" and parentLayerData == "-NONE-"):
                return ""
            else:
                return " " + layerData.replace("-LRB-", "(").replace("-RRB-", ")").replace("-LSB-", "[").\
                    replace("-RSB-", "]").replace("-LCB-", "{").replace("-RCB-", "}").replace("-lrb-", "(").\
                    replace("-rrb-", ")").replace("-lsb-", "[").replace("-rsb-", "]").replace("-lcb", "{").\
                    replace("-rcb-", "}")
        else:
            return ""
