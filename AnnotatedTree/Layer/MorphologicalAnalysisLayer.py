from AnnotatedSentence.ViewLayerType import ViewLayerType
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse

from AnnotatedTree.Layer.MultiWordMultiItemLayer import MultiWordMultiItemLayer


class MorphologicalAnalysisLayer(MultiWordMultiItemLayer):

    def __init__(self, layerValue: str):
        """
        Constructor for the morphological analysis layer. Sets the morphological parse information for multiple words in
        the node.
        :param layerValue: Layer value for the morphological parse information. Consists of morphological parse information
                       of multiple words separated via space character.
        """
        self.layer_name = "morphologicalAnalysis"
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        """
        Sets the layer value to the string form of the given morphological parse.
        :param layerValue: New morphological parse.
        """
        self.items = []
        if isinstance(layerValue, str):
            self.layer_value = layerValue
            if layerValue is not None:
                split_words = self.layer_value.split(" ")
                for word in split_words:
                    self.items.append(MorphologicalParse(word))
        elif isinstance(layerValue, MorphologicalParse):
            parse = layerValue
            self.layer_value = parse.getTransitionList()
            self.items.append(parse)

    def getLayerSize(self, viewLayer: ViewLayerType) -> int:
        """
        Returns the total number of morphological tags (for PART_OF_SPEECH) or inflectional groups
        (for INFLECTIONAL_GROUP) in the words in the node.
        :param viewLayer: Layer type.
        :return: Total number of morphological tags (for PART_OF_SPEECH) or inflectional groups (for INFLECTIONAL_GROUP)
        in the words in the node.
        """
        size = 0
        if viewLayer == ViewLayerType.PART_OF_SPEECH:
            for parse in self.items:
                if isinstance(parse, MorphologicalParse):
                    size += parse.tagSize()
        elif viewLayer == ViewLayerType.INFLECTIONAL_GROUP:
            for parse in self.items:
                if isinstance(parse, MorphologicalParse):
                    size += parse.size()
        return size

    def getLayerInfoAt(self, viewLayer: ViewLayerType, index: int) -> str:
        """
        Returns the morphological tag (for PART_OF_SPEECH) or inflectional group (for INFLECTIONAL_GROUP) at position
        index.
        :param viewLayer: Layer type.
        :param index: Position of the morphological tag (for PART_OF_SPEECH) or inflectional group
        (for INFLECTIONAL_GROUP)
        :return: The morphological tag (for PART_OF_SPEECH) or inflectional group (for INFLECTIONAL_GROUP)
        """
        size = 0
        if viewLayer == ViewLayerType.PART_OF_SPEECH:
            for parse in self.items:
                if isinstance(parse, MorphologicalParse) and index < size + parse.tagSize():
                    return parse.getTag(index - size)
                size += parse.tagSize()
            return None
        elif viewLayer == ViewLayerType.INFLECTIONAL_GROUP:
            for parse in self.items:
                if isinstance(parse, MorphologicalParse) and index < size + parse.size():
                    return parse.getInflectionalGroupString(index - size)
                size += parse.size()
            return None
        return None
