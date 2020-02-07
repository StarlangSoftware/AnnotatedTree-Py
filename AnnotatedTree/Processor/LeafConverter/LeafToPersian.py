from AnnotatedSentence.ViewLayerType import ViewLayerType

from AnnotatedTree.Processor.LeafConverter.LeafToLanguageConverter import LeafToLanguageConverter


class LeafToPersian(LeafToLanguageConverter):

    def __init__(self):
        self.viewLayerType = ViewLayerType.PERSIAN_WORD
