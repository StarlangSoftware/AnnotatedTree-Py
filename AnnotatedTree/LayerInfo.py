import re

from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from AnnotatedSentence.ViewLayerType import ViewLayerType
from MorphologicalAnalysis.MetamorphicParse import MetamorphicParse
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse
from PropBank.Argument import Argument

from AnnotatedTree.Layer.DependencyLayer import DependencyLayer
from AnnotatedTree.Layer.EnglishPropbankLayer import EnglishPropbankLayer
from AnnotatedTree.Layer.EnglishSemanticLayer import EnglishSemanticLayer
from AnnotatedTree.Layer.EnglishWordLayer import EnglishWordLayer
from AnnotatedTree.Layer.MetaMorphemeLayer import MetaMorphemeLayer
from AnnotatedTree.Layer.MetaMorphemesMovedLayer import MetaMorphemesMovedLayer
from AnnotatedTree.Layer.MorphologicalAnalysisLayer import MorphologicalAnalysisLayer
from AnnotatedTree.Layer.MultiWordLayer import MultiWordLayer
from AnnotatedTree.Layer.MultiWordMultiItemLayer import MultiWordMultiItemLayer
from AnnotatedTree.Layer.NERLayer import NERLayer
from AnnotatedTree.Layer.PersianWordLayer import PersianWordLayer
from AnnotatedTree.Layer.ShallowParseLayer import ShallowParseLayer
from AnnotatedTree.Layer.SingleWordMultiItemLayer import SingleWordMultiItemLayer
from AnnotatedTree.Layer.TurkishPropbankLayer import TurkishPropbankLayer
from AnnotatedTree.Layer.TurkishSemanticLayer import TurkishSemanticLayer
from AnnotatedTree.Layer.TurkishWordLayer import TurkishWordLayer


class LayerInfo:
    layers: dict

    def __init__(self, info: str = None):
        """
        Constructs the layer information from the given string. Layers are represented as
        {layername1=layervalue1}{layername2=layervalue2}...{layernamek=layervaluek} where layer name is one of the
        following: turkish, persian, english, morphologicalAnalysis, metaMorphemes, metaMorphemesMoved, dependency,
        semantics, namedEntity, propBank, englishPropbank, englishSemantics, shallowParse. Splits the string w.r.t.
        parentheses and constructs layer objects and put them layers map accordingly.
        :param info: Line consisting of layer info.
        """
        if info is None:
            self.layers = {}
        else:
            self.layers = {}
            split_layers = re.split("[{}]", info)
            for layer in split_layers:
                if len(layer) == 0:
                    continue
                layer_type = layer[:layer.index("=")]
                layer_value = layer[layer.index("=") + 1:]
                if layer_type == "turkish":
                    self.layers[ViewLayerType.TURKISH_WORD] = TurkishWordLayer(layer_value)
                elif layer_type == "persian":
                    self.layers[ViewLayerType.PERSIAN_WORD] = PersianWordLayer(layer_value)
                elif layer_type == "english":
                    self.layers[ViewLayerType.ENGLISH_WORD] = EnglishWordLayer(layer_value)
                elif layer_type == "morphologicalAnalysis":
                    self.layers[ViewLayerType.INFLECTIONAL_GROUP] = MorphologicalAnalysisLayer(layer_value)
                    self.layers[ViewLayerType.PART_OF_SPEECH] = MorphologicalAnalysisLayer(layer_value)
                elif layer_type == "metaMorphemes":
                    self.layers[ViewLayerType.META_MORPHEME] = MetaMorphemeLayer(layer_value)
                elif layer_type == "metaMorphemesMoved":
                    self.layers[ViewLayerType.META_MORPHEME_MOVED] = MetaMorphemesMovedLayer(layer_value)
                elif layer_type == "dependency":
                    self.layers[ViewLayerType.DEPENDENCY] = DependencyLayer(layer_value)
                elif layer_type == "semantics":
                    self.layers[ViewLayerType.SEMANTICS] = TurkishSemanticLayer(layer_value)
                elif layer_type == "namedEntity":
                    self.layers[ViewLayerType.NER] = NERLayer(layer_value)
                elif layer_type == "propBank":
                    self.layers[ViewLayerType.PROPBANK] = TurkishPropbankLayer(layer_value)
                elif layer_type == "englishPropbank":
                    self.layers[ViewLayerType.ENGLISH_PROPBANK] = EnglishPropbankLayer(layer_value)
                elif layer_type == "englishSemantics":
                    self.layers[ViewLayerType.ENGLISH_SEMANTICS] = EnglishSemanticLayer(layer_value)

    def setLayerData(self,
                     viewLayer: ViewLayerType,
                     layerValue: str):
        """
        Changes the given layer info with the given string layer value. For all layers new layer object is created and
        replaces the original object. For turkish layer, it also destroys inflectional_group, part_of_speech,
        meta_morpheme, meta_morpheme_moved and semantics layers. For persian layer, it also destroys the semantics layer.
        :param viewLayer: Layer name.
        :param layerValue: New layer value.
        """
        if viewLayer == ViewLayerType.PERSIAN_WORD:
            self.layers[ViewLayerType.PERSIAN_WORD] = PersianWordLayer(layerValue)
            self.layers.pop(ViewLayerType.PERSIAN_WORD)
        elif viewLayer == ViewLayerType.TURKISH_WORD:
            self.layers[ViewLayerType.TURKISH_WORD] = TurkishWordLayer(layerValue)
            self.layers.pop(ViewLayerType.INFLECTIONAL_GROUP)
            self.layers.pop(ViewLayerType.PART_OF_SPEECH)
            self.layers.pop(ViewLayerType.META_MORPHEME)
            self.layers.pop(ViewLayerType.META_MORPHEME_MOVED)
            self.layers.pop(ViewLayerType.SEMANTICS)
        elif viewLayer == ViewLayerType.ENGLISH_WORD:
            self.layers[ViewLayerType.ENGLISH_WORD] = EnglishWordLayer(layerValue)
        elif viewLayer == ViewLayerType.PART_OF_SPEECH or viewLayer == ViewLayerType.INFLECTIONAL_GROUP:
            self.layers[ViewLayerType.INFLECTIONAL_GROUP] = MorphologicalAnalysisLayer(layerValue)
            self.layers[ViewLayerType.PART_OF_SPEECH] = MorphologicalAnalysisLayer(layerValue)
            self.layers.pop(ViewLayerType.META_MORPHEME_MOVED)
        elif viewLayer == ViewLayerType.META_MORPHEME:
            self.layers[ViewLayerType.META_MORPHEME] = MetaMorphemeLayer(layerValue)
        elif viewLayer == ViewLayerType.META_MORPHEME_MOVED:
            self.layers[ViewLayerType.META_MORPHEME_MOVED] = MetaMorphemesMovedLayer(layerValue)
        elif viewLayer == ViewLayerType.DEPENDENCY:
            self.layers[ViewLayerType.DEPENDENCY] = DependencyLayer(layerValue)
        elif viewLayer == ViewLayerType.SEMANTICS:
            self.layers[ViewLayerType.SEMANTICS] = TurkishSemanticLayer(layerValue)
        elif viewLayer == ViewLayerType.ENGLISH_SEMANTICS:
            self.layers[ViewLayerType.ENGLISH_SEMANTICS] = EnglishSemanticLayer(layerValue)
        elif viewLayer == ViewLayerType.NER:
            self.layers[ViewLayerType.NER] = NERLayer(layerValue)
        elif viewLayer == ViewLayerType.PROPBANK:
            self.layers[ViewLayerType.PROPBANK] = TurkishPropbankLayer(layerValue)
        elif viewLayer == ViewLayerType.ENGLISH_PROPBANK:
            self.layers[ViewLayerType.ENGLISH_PROPBANK] = EnglishPropbankLayer(layerValue)
        elif viewLayer == ViewLayerType.SHALLOW_PARSE:
            self.layers[ViewLayerType.SHALLOW_PARSE] = ShallowParseLayer(layerValue)

    def setMorphologicalAnalysis(self, parse: MorphologicalParse):
        """
        Updates the inflectional_group and part_of_speech layers according to the given parse.
        :param parse: New parse to update layers.
        """
        self.layers[ViewLayerType.INFLECTIONAL_GROUP] = MorphologicalAnalysisLayer(parse.__str__())
        self.layers[ViewLayerType.PART_OF_SPEECH] = MorphologicalAnalysisLayer(parse.__str__())

    def setMetaMorphemes(self, parse: MetamorphicParse):
        """
        Updates the metamorpheme layer according to the given parse.
        :param parse: New parse to update layer.
        """
        self.layers[ViewLayerType.META_MORPHEME] = MetaMorphemeLayer(parse.__str__())

    def layerExists(self, viewLayerType: ViewLayerType) -> bool:
        """
        Checks if the given layer exists.
        :param viewLayerType: Layer name
        :return: True if the layer exists, false otherwise.
        """
        return viewLayerType in self.layers

    def checkLayer(self, viewLayer: ViewLayerType) -> ViewLayerType:
        """
        Two level layer check method. For turkish, persian and english_semantics layers, if the layer does not exist,
        returns english layer. For part_of_speech, inflectional_group, meta_morpheme, semantics, propbank, shallow_parse,
        english_propbank layers, if the layer does not exist, it checks turkish layer. For meta_morpheme_moved, if the
        layer does not exist, it checks meta_morpheme layer.
        :param viewLayer: Layer to be checked.
        :return: Returns the original layer if the layer exists. For turkish, persian and english_semantics layers, if the
        layer  does not exist, returns english layer. For part_of_speech, inflectional_group, meta_morpheme, semantics,
        propbank,  shallow_parse, english_propbank layers, if the layer does not exist, it checks turkish layer
        recursively. For meta_morpheme_moved, if the layer does not exist, it checks meta_morpheme layer recursively.
        """
        if viewLayer == ViewLayerType.TURKISH_WORD or viewLayer == ViewLayerType.PERSIAN_WORD or \
                viewLayer == ViewLayerType.ENGLISH_SEMANTICS:
            if viewLayer not in self.layers:
                return ViewLayerType.ENGLISH_WORD
        elif viewLayer == ViewLayerType.PART_OF_SPEECH or viewLayer == ViewLayerType.INFLECTIONAL_GROUP or \
                viewLayer == ViewLayerType.META_MORPHEME or viewLayer == ViewLayerType.SEMANTICS or \
                viewLayer == ViewLayerType.NER or viewLayer == ViewLayerType.PROPBANK or \
                viewLayer == ViewLayerType.SHALLOW_PARSE or viewLayer == ViewLayerType.ENGLISH_PROPBANK:
            if viewLayer not in self.layers:
                return ViewLayerType.TURKISH_WORD
        elif viewLayer == ViewLayerType.META_MORPHEME_MOVED:
            if viewLayer not in self.layers:
                return ViewLayerType.META_MORPHEME
        return viewLayer

    def getNumberOfWords(self) -> int:
        """
        Returns number of words in the Turkish or Persian layer, whichever exists.
        :return: Number of words in the Turkish or Persian layer, whichever exists.
        """
        if ViewLayerType.TURKISH_WORD in self.layers:
            return self.layers[ViewLayerType.TURKISH_WORD].size()
        elif ViewLayerType.PERSIAN_WORD in self.layers:
            return self.layers[ViewLayerType.PERSIAN_WORD].size()

    def getMultiWordAt(self,
                       viewLayerType: ViewLayerType,
                       index: int,
                       layerName: str) -> str:
        """
        Returns the layer value at the given index.
        :param viewLayerType: Layer for which the value at the given word index will be returned.
        :param index: Word Position of the layer value.
        :param layerName: Name of the layer.
        :return: Layer info at word position index for a multiword layer.
        """
        if viewLayerType in self.layers:
            if isinstance(self.layers[viewLayerType], MultiWordLayer):
                multi_word_layer = self.layers[viewLayerType]
                if 0 <= index < multi_word_layer.size():
                    return multi_word_layer.getItemAt(index)
                else:
                    if viewLayerType == ViewLayerType.SEMANTICS:
                        return multi_word_layer.getItemAt(multi_word_layer.size() - 1)

    def getTurkishWordAt(self, index: int) -> str:
        """
        Layers may contain multiple Turkish words. This method returns the Turkish word at position index.
        :param index: Position of the Turkish word.
        :return: The Turkish word at position index.
        """
        return self.getMultiWordAt(ViewLayerType.TURKISH_WORD, index, "turkish")

    def getNumberOfMeanings(self) -> int:
        """
        Returns number of meanings in the Turkish layer.
        :return: Number of meanings in the Turkish layer.
        """
        if ViewLayerType.SEMANTICS in self.layers:
            return self.layers[ViewLayerType.SEMANTICS].size()
        else:
            return 0

    def getSemanticAt(self, index: int) -> str:
        return self.getMultiWordAt(ViewLayerType.SEMANTICS, index, "semantics")

    def getShallowParseAt(self, index: int) -> str:
        """
        Layers may contain multiple shallow parse information corresponding to multiple Turkish words. This method
        returns the shallow parse tag at position index.
        :param index: Position of the Turkish word.
        :return: The shallow parse tag at position index.
        """
        return self.getMultiWordAt(ViewLayerType.SHALLOW_PARSE, index, "shallowParse")

    def getArgument(self) -> Argument:
        """
        Returns the Turkish PropBank argument info.
        :return: Turkish PropBank argument info.
        """
        if ViewLayerType.PROPBANK in self.layers:
            if isinstance(self.layers[ViewLayerType.PROPBANK], TurkishPropbankLayer):
                argument_layer = self.layers[ViewLayerType.PROPBANK]
                return argument_layer.getArgument()
            else:
                return None
        else:
            return None

    def getArgumentAt(self, index: int) -> Argument:
        """
        A word may have multiple English propbank info. This method returns the English PropBank argument info at
        position index.
        :param index: Position of the argument
        :return: English PropBank argument info at position index.
        """
        if ViewLayerType.ENGLISH_PROPBANK in self.layers:
            if isinstance(self.layers[ViewLayerType.ENGLISH_PROPBANK], SingleWordMultiItemLayer):
                multiArgumentLayer = self.layers[ViewLayerType.ENGLISH_PROPBANK]
                return multiArgumentLayer.getItemAt(index)

    def getMorphologicalParseAt(self, index: int) -> MorphologicalParse:
        """
        Layers may contain multiple morphological parse information corresponding to multiple Turkish words. This method
        returns the morphological parse at position index.
        :param index: Position of the Turkish word.
        :return: The morphological parse at position index.
        """
        if ViewLayerType.INFLECTIONAL_GROUP in self.layers:
            if isinstance(self.layers[ViewLayerType.INFLECTIONAL_GROUP], MultiWordLayer):
                multi_word_layer = self.layers[ViewLayerType.INFLECTIONAL_GROUP]
                if 0 <= index < multi_word_layer.size():
                    return multi_word_layer.getItemAt(index)

    def getMetamorphicParseAt(self, index: int) -> MetamorphicParse:
        """
        Layers may contain multiple metamorphic parse information corresponding to multiple Turkish words. This method
        returns the metamorphic parse at position index.
        :param index: Position of the Turkish word.
        :return: The metamorphic parse at position index.
        """
        if ViewLayerType.META_MORPHEME in self.layers:
            if isinstance(self.layers[ViewLayerType.META_MORPHEME], MultiWordLayer):
                multi_word_layer = self.layers[ViewLayerType.META_MORPHEME]
                if 0 <= index < multi_word_layer.size():
                    return multi_word_layer.getItemAt(index)

    def getMetaMorphemeAtIndex(self, index: int) -> str:
        """
        Layers may contain multiple metamorphemes corresponding to one or multiple Turkish words. This method
        returns the metamorpheme at position index.
        :param index: Position of the metamorpheme.
        :return: The metamorpheme at position index.
        """
        if ViewLayerType.META_MORPHEME in self.layers:
            if isinstance(self.layers[ViewLayerType.META_MORPHEME], MetaMorphemeLayer):
                meta_morpheme_layer = self.layers[ViewLayerType.META_MORPHEME]
                if 0 <= index < meta_morpheme_layer.getLayerSize(ViewLayerType.META_MORPHEME):
                    return meta_morpheme_layer.getLayerInfoAt(ViewLayerType.META_MORPHEME, index)

    def getMetaMorphemeFromIndex(self, index: int) -> str:
        """
        Layers may contain multiple metamorphemes corresponding to one or multiple Turkish words. This method
        returns all metamorphemes from position index.
        :param index: Start position of the metamorpheme.
        :return: All metamorphemes from position index.
        """
        if ViewLayerType.META_MORPHEME in self.layers:
            if isinstance(self.layers[ViewLayerType.META_MORPHEME], MetaMorphemeLayer):
                meta_morpheme_layer = self.layers[ViewLayerType.META_MORPHEME]
                if 0 <= index < meta_morpheme_layer.getLayerSize(ViewLayerType.META_MORPHEME):
                    return meta_morpheme_layer.getLayerInfoFrom(index)

    def getLayerSize(self, viewLayer: ViewLayerType) -> int:
        """
        For layers with multiple item information, this method returns total items in that layer.
        :param viewLayer: Layer name
        :return: Total items in the given layer.
        """
        if isinstance(self.layers[viewLayer], MultiWordMultiItemLayer):
            return self.layers[viewLayer].getLayerSize(viewLayer)
        elif isinstance(self.layers[viewLayer], SingleWordMultiItemLayer):
            return self.layers[viewLayer].getLayerSize(viewLayer)

    def getLayerInfoAt(self,
                       viewLayer: ViewLayerType,
                       index: int) -> str:
        """
        For layers with multiple item information, this method returns the item at position index.
        :param viewLayer: Layer name
        :param index: Position of the item.
        :return: The item at position index.
        """
        if viewLayer == ViewLayerType.META_MORPHEME_MOVED or viewLayer == ViewLayerType.PART_OF_SPEECH or \
                viewLayer == ViewLayerType.INFLECTIONAL_GROUP:
            if isinstance(self.layers[viewLayer], MultiWordMultiItemLayer):
                return self.layers[viewLayer].getLayerInfoAt(viewLayer, index)
        elif viewLayer == ViewLayerType.META_MORPHEME:
            return self.getMetaMorphemeAtIndex(index)
        elif viewLayer == ViewLayerType.ENGLISH_PROPBANK:
            return self.getArgumentAt(index).getArgumentType()
        else:
            return None

    def getLayerDescription(self) -> str:
        """
        Returns the string form of all layer information except part_of_speech layer.
        :return: The string form of all layer information except part_of_speech layer.
        """
        result = ""
        for view_layer_type in self.layers.keys():
            if view_layer_type != ViewLayerType.PART_OF_SPEECH:
                result += self.layers[view_layer_type].getLayerDescription()
        return result

    def getLayerData(self, viewLayer: ViewLayerType) -> str:
        """
        Returns the layer info for the given layer.
        :param viewLayer: Layer name.
        :return: Layer info for the given layer.
        """
        if viewLayer in self.layers:
            return self.layers[viewLayer].getLayerValue()
        else:
            return None

    def getRobustLayerData(self, viewLayer: ViewLayerType) -> str:
        """
        Returns the layer info for the given layer, if that layer exists. Otherwise, it returns the fallback layer info
        determined by the checkLayer.
        :param viewLayer: Layer name
        :return: Layer info for the given layer if it exists. Otherwise, it returns the fallback layer info determined by
        the checkLayer.
        """
        viewLayer = self.checkLayer(viewLayer)
        return self.getLayerData(viewLayer)

    def updateMetaMorphemesMoved(self):
        """
        Initializes the metamorphemesmoved layer with metamorpheme layer except the root word.
        """
        if ViewLayerType.META_MORPHEME in self.layers:
            meta_morpheme_layer = self.layers[ViewLayerType.META_MORPHEME]
            if meta_morpheme_layer.size() > 0:
                result = meta_morpheme_layer.getItemAt(0).__str__()
                for i in range(1, meta_morpheme_layer.size()):
                    result += " " + meta_morpheme_layer.getItemAt(i).__str__()
                self.layers[ViewLayerType.META_MORPHEME_MOVED] = MetaMorphemesMovedLayer(result)

    def removeLayer(self, layerType: ViewLayerType):
        """
        Removes the given layer from hash map.
        :param layerType: Layer to be removed.
        """
        self.layers.pop(layerType)

    def metaMorphemeClear(self):
        """
        Removes metamorpheme and metamorphemesmoved layers.
        """
        self.layers.pop(ViewLayerType.META_MORPHEME)
        self.layers.pop(ViewLayerType.META_MORPHEME_MOVED)

    def englishClear(self):
        """
        Removes English layer.
        """
        self.layers.pop(ViewLayerType.ENGLISH_WORD)

    def dependencyLayer(self):
        """
        Removes the dependency layer.
        """
        self.layers.pop(ViewLayerType.DEPENDENCY)

    def metaMorphemesMovedClear(self):
        """
        Removed metamorphemesmoved layer.
        """
        self.layers.pop(ViewLayerType.META_MORPHEME_MOVED)

    def semanticClear(self):
        """
        Removes the Turkish semantic layer.
        """
        self.layers.pop(ViewLayerType.SEMANTICS)

    def englishSemanticClear(self):
        """
        Removes the English semantic layer.
        """
        self.layers.pop(ViewLayerType.ENGLISH_SEMANTICS)

    def morphologicalAnalysisClear(self):
        """
        Removes the morphological analysis, part of speech, metamorpheme, and metamorphemesmoved layers.
        """
        self.layers.pop(ViewLayerType.INFLECTIONAL_GROUP)
        self.layers.pop(ViewLayerType.PART_OF_SPEECH)
        self.layers.pop(ViewLayerType.META_MORPHEME)
        self.layers.pop(ViewLayerType.META_MORPHEME_MOVED)

    def metaMorphemeRemove(self, index: int) -> MetamorphicParse:
        """
        Removes the metamorpheme at position index.
        :param index: Position of the metamorpheme to be removed.
        :return: Metamorphemes concatenated as a string after the removed metamorpheme.
        """
        if ViewLayerType.META_MORPHEME in self.layers:
            meta_morpheme_layer = self.layers[ViewLayerType.META_MORPHEME]
            if 0 <= index < meta_morpheme_layer.getLayerSize(ViewLayerType.META_MORPHEME):
                removed_parse = meta_morpheme_layer.metaMorphemeRemoveFromIndex(index)
                self.updateMetaMorphemesMoved()
        return removed_parse

    def divideIntoWords(self):
        result = []
        for i in range(self.getNumberOfWords()):
            layer_info = LayerInfo()
            layer_info.setLayerData(ViewLayerType.TURKISH_WORD, self.getTurkishWordAt(i))
            layer_info.setLayerData(ViewLayerType.ENGLISH_WORD, self.getLayerData(ViewLayerType.ENGLISH_WORD))
            if self.layerExists(ViewLayerType.INFLECTIONAL_GROUP):
                layer_info.setMorphologicalAnalysis(self.getMorphologicalParseAt(i))
            if self.layerExists(ViewLayerType.META_MORPHEME):
                layer_info.setMetaMorphemes(self.getMetamorphicParseAt(i))
            if self.layerExists(ViewLayerType.ENGLISH_PROPBANK):
                layer_info.setLayerData(ViewLayerType.ENGLISH_PROPBANK, self.getLayerData(ViewLayerType.ENGLISH_PROPBANK))
            if self.layerExists(ViewLayerType.ENGLISH_SEMANTICS):
                layer_info.setLayerData(ViewLayerType.ENGLISH_SEMANTICS, self.getLayerData(ViewLayerType.ENGLISH_SEMANTICS))
            if self.layerExists(ViewLayerType.NER):
                layer_info.setLayerData(ViewLayerType.NER, self.getLayerData(ViewLayerType.NER))
            if self.layerExists(ViewLayerType.SEMANTICS):
                layer_info.setLayerData(ViewLayerType.SEMANTICS, self.getSemanticAt(i))
            if self.layerExists(ViewLayerType.PROPBANK):
                layer_info.setLayerData(ViewLayerType.PROPBANK, self.getArgument().__str__())
            if self.layerExists(ViewLayerType.SHALLOW_PARSE):
                layer_info.setLayerData(ViewLayerType.SHALLOW_PARSE, self.getShallowParseAt(i))
            result.append(layer_info)
        return result

    def toAnnotatedWord(self, wordIndex: int) -> AnnotatedWord:
        """
        Converts layer info of the word at position wordIndex to an AnnotatedWord. Layers are converted to their
        counterparts in the AnnotatedWord.
        :param wordIndex: Index of the word to be converted.
        :return: Converted annotatedWord
        """
        annotated_word = AnnotatedWord(self.getTurkishWordAt(wordIndex))
        if self.layerExists(ViewLayerType.INFLECTIONAL_GROUP):
            annotated_word.setParse(self.getMorphologicalParseAt(wordIndex).__str__())
        if self.layerExists(ViewLayerType.META_MORPHEME):
            annotated_word.setMetamorphicParse(self.getMetamorphicParseAt(wordIndex).__str__())
        if self.layerExists(ViewLayerType.SEMANTICS):
            annotated_word.setSemantic(self.getSemanticAt(wordIndex))
        if self.layerExists(ViewLayerType.NER):
            annotated_word.setNamedEntityType(self.getLayerData(ViewLayerType.NER))
        if self.layerExists(ViewLayerType.PROPBANK):
            annotated_word.setArgumentList(self.getArgument().__str__())
        if self.layerExists(ViewLayerType.SHALLOW_PARSE):
            annotated_word.setShallowParse(self.getShallowParseAt(wordIndex))
        return annotated_word
