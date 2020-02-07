from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.Processor.LeafConverter.LeafToLanguageConverter import LeafToLanguageConverter


class LeafToEnglish(LeafToLanguageConverter):

    def __init__(self):
        self.viewLayerType = ViewLayerType.ENGLISH_WORD
