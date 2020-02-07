from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.Processor.LeafConverter.LeafToLanguageConverter import LeafToLanguageConverter


class LeafToTurkish(LeafToLanguageConverter):

    def __init__(self):
        self.viewLayerType = ViewLayerType.TURKISH_WORD
