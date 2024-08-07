from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.Processor.LeafConverter.LeafToLanguageConverter import LeafToLanguageConverter


class LeafToTurkish(LeafToLanguageConverter):

    def __init__(self):
        """
        Constructor for LeafToTurkish. Sets viewLayerType to TURKISH.
        """
        self.view_layer_type = ViewLayerType.TURKISH_WORD
