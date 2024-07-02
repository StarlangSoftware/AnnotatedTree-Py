from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.Processor.LeafConverter.LeafToLanguageConverter import LeafToLanguageConverter


class LeafToPersian(LeafToLanguageConverter):

    def __init__(self):
        """
        Constructor for LeafToPersian. Sets viewLayerType to PERSIAN.
        """
        self.view_layer_type = ViewLayerType.PERSIAN_WORD
