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
    layers: map

    def __init__(self, info: str = None):
        if info is None:
            self.layers = {}
        else:
            self.layers = {}
            splitLayers = re.split("[{}]", info)
            for layer in splitLayers:
                if len(layer) == 0:
                    continue
                layerType = layer[:layer.index("=")]
                layerValue = layer[layer.index("=") + 1:]
                if layerType == "turkish":
                    self.layers[ViewLayerType.TURKISH_WORD] = TurkishWordLayer(layerValue)
                elif layerType == "persian":
                    self.layers[ViewLayerType.PERSIAN_WORD] = PersianWordLayer(layerValue)
                elif layerType == "english":
                    self.layers[ViewLayerType.ENGLISH_WORD] = EnglishWordLayer(layerValue)
                elif layerType == "morphologicalAnalysis":
                    self.layers[ViewLayerType.INFLECTIONAL_GROUP] = MorphologicalAnalysisLayer(layerValue)
                    self.layers[ViewLayerType.PART_OF_SPEECH] = MorphologicalAnalysisLayer(layerValue)
                elif layerType == "metaMorphemes":
                    self.layers[ViewLayerType.META_MORPHEME] = MetaMorphemeLayer(layerValue)
                elif layerType == "metaMorphemesMoved":
                    self.layers[ViewLayerType.META_MORPHEME_MOVED] = MetaMorphemesMovedLayer(layerValue)
                elif layerType == "dependency":
                    self.layers[ViewLayerType.DEPENDENCY] = DependencyLayer(layerValue)
                elif layerType == "semantics":
                    self.layers[ViewLayerType.SEMANTICS] = TurkishSemanticLayer(layerValue)
                elif layerType == "namedEntity":
                    self.layers[ViewLayerType.NER] = NERLayer(layerValue)
                elif layerType == "propBank":
                    self.layers[ViewLayerType.PROPBANK] = TurkishPropbankLayer(layerValue)
                elif layerType == "englishPropbank":
                    self.layers[ViewLayerType.ENGLISH_PROPBANK] = EnglishPropbankLayer(layerValue)
                elif layerType == "englishSemantics":
                    self.layers[ViewLayerType.ENGLISH_SEMANTICS] = EnglishSemanticLayer(layerValue)

    def setLayerData(self, viewLayer: ViewLayerType, layerValue: str):
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
        self.layers[ViewLayerType.INFLECTIONAL_GROUP] = MorphologicalAnalysisLayer(parse.__str__())
        self.layers[ViewLayerType.PART_OF_SPEECH] = MorphologicalAnalysisLayer(parse.__str__())

    def setMetaMorphemes(self, parse: MetamorphicParse):
        self.layers[ViewLayerType.META_MORPHEME] = MetaMorphemeLayer(parse.__str__())

    def layerExists(self, viewLayerType: ViewLayerType) -> bool:
        return viewLayerType in self.layers

    def checkLayer(self, viewLayer: ViewLayerType) -> ViewLayerType:
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
        if ViewLayerType.TURKISH_WORD in self.layers:
            return self.layers[ViewLayerType.TURKISH_WORD].size()
        elif ViewLayerType.PERSIAN_WORD in self.layers:
            return self.layers[ViewLayerType.PERSIAN_WORD].size()

    def getMultiWordAt(self, viewLayerType: ViewLayerType, index: int, layerName: str) -> str:
        if viewLayerType in self.layers:
            if isinstance(self.layers[viewLayerType], MultiWordLayer):
                multiWordLayer = self.layers[viewLayerType]
                if 0 <= index < multiWordLayer.size():
                    return multiWordLayer.getItemAt(index)
                else:
                    if viewLayerType == ViewLayerType.SEMANTICS:
                        return multiWordLayer.getItemAt(multiWordLayer.size() - 1)

    def getTurkishWordAt(self, index: int) -> str:
        return self.getMultiWordAt(ViewLayerType.TURKISH_WORD, index, "turkish")

    def getNumberOfMeanings(self) -> int:
        if ViewLayerType.SEMANTICS in self.layers:
            return self.layers[ViewLayerType.SEMANTICS].size()
        else:
            return 0

    def getSemanticAt(self, index: int) -> str:
        return self.getMultiWordAt(ViewLayerType.SEMANTICS, index, "semantics")

    def getShallowParseAt(self, index: int) -> str:
        return self.getMultiWordAt(ViewLayerType.SHALLOW_PARSE, index, "shallowParse")

    def getArgument(self) -> Argument:
        if ViewLayerType.PROPBANK in self.layers:
            if isinstance(self.layers[ViewLayerType.PROPBANK], TurkishPropbankLayer):
                argumentLayer = self.layers[ViewLayerType.PROPBANK]
                return argumentLayer.getArgument()
            else:
                return None
        else:
            return None

    def getArgumentAt(self, index: int) -> Argument:
        if ViewLayerType.ENGLISH_PROPBANK in self.layers:
            if isinstance(self.layers[ViewLayerType.ENGLISH_PROPBANK], SingleWordMultiItemLayer):
                multiArgumentLayer = self.layers[ViewLayerType.ENGLISH_PROPBANK]
                return multiArgumentLayer.getItemAt(index)

    def getMorphologicalParseAt(self, index: int) -> MorphologicalParse:
        if ViewLayerType.INFLECTIONAL_GROUP in self.layers:
            if isinstance(self.layers[ViewLayerType.INFLECTIONAL_GROUP], MultiWordLayer):
                multiWordLayer = self.layers[ViewLayerType.INFLECTIONAL_GROUP]
                if 0 <= index < multiWordLayer.size():
                    return multiWordLayer.getItemAt(index)

    def getMetamorphicParseAt(self, index: int) -> MetamorphicParse:
        if ViewLayerType.META_MORPHEME in self.layers:
            if isinstance(self.layers[ViewLayerType.META_MORPHEME], MultiWordLayer):
                multiWordLayer = self.layers[ViewLayerType.META_MORPHEME]
                if 0 <= index < multiWordLayer.size():
                    return multiWordLayer.getItemAt(index)

    def getMetaMorphemeAtIndex(self, index: int) -> str:
        if ViewLayerType.META_MORPHEME in self.layers:
            if isinstance(self.layers[ViewLayerType.META_MORPHEME], MetaMorphemeLayer):
                metaMorphemeLayer = self.layers[ViewLayerType.META_MORPHEME]
                if 0 <= index < metaMorphemeLayer.getLayerSize(ViewLayerType.META_MORPHEME):
                    return metaMorphemeLayer.getLayerInfoAt(ViewLayerType.META_MORPHEME, index)

    def getMetaMorphemeFromIndex(self, index: int) -> str:
        if ViewLayerType.META_MORPHEME in self.layers:
            if isinstance(self.layers[ViewLayerType.META_MORPHEME], MetaMorphemeLayer):
                metaMorphemeLayer = self.layers[ViewLayerType.META_MORPHEME]
                if 0 <= index < metaMorphemeLayer.getLayerSize(ViewLayerType.META_MORPHEME):
                    return metaMorphemeLayer.getLayerInfoFrom(index)

    def getLayerSize(self, viewLayer: ViewLayerType) -> int:
        if isinstance(self.layers[viewLayer], MultiWordMultiItemLayer):
            return self.layers[viewLayer].getLayerSize(viewLayer)
        elif isinstance(self.layers[viewLayer], SingleWordMultiItemLayer):
            return self.layers[viewLayer].getLayerSize(viewLayer)

    def getLayerInfoAt(self, viewLayer: ViewLayerType, index: int) -> str:
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
        result = ""
        for viewLayerType in self.layers.keys():
            if viewLayerType != ViewLayerType.PART_OF_SPEECH:
                result += self.layers[viewLayerType].getLayerDescription()
        return result

    def getLayerData(self, viewLayer: ViewLayerType) -> str:
        if viewLayer in self.layers:
            return self.layers[viewLayer].getLayerValue()
        else:
            return None

    def getRobustLayerData(self, viewLayer: ViewLayerType) -> str:
        viewLayer = self.checkLayer(viewLayer)
        return self.getLayerData(viewLayer)

    def updateMetaMorphemesMoved(self):
        if ViewLayerType.META_MORPHEME in self.layers:
            metaMorphemeLayer = self.layers[ViewLayerType.META_MORPHEME]
            if metaMorphemeLayer.size() > 0:
                result = metaMorphemeLayer.getItemAt(0).__str__()
                for i in range(1, metaMorphemeLayer.size()):
                    result += " " + metaMorphemeLayer.getItemAt(i).__str__()
                self.layers[ViewLayerType.META_MORPHEME_MOVED] = MetaMorphemesMovedLayer(result)

    def removeLayer(self, layerType: ViewLayerType):
        self.layers.pop(layerType)

    def metaMorphemeClear(self):
        self.layers.pop(ViewLayerType.META_MORPHEME)
        self.layers.pop(ViewLayerType.META_MORPHEME_MOVED)

    def englishClear(self):
        self.layers.pop(ViewLayerType.ENGLISH_WORD)

    def dependencyLayer(self):
        self.layers.pop(ViewLayerType.DEPENDENCY)

    def metaMorphemesMovedClear(self):
        self.layers.pop(ViewLayerType.META_MORPHEME_MOVED)

    def semanticClear(self):
        self.layers.pop(ViewLayerType.SEMANTICS)

    def englishSemanticClear(self):
        self.layers.pop(ViewLayerType.ENGLISH_SEMANTICS)

    def morphologicalAnalysisClear(self):
        self.layers.pop(ViewLayerType.INFLECTIONAL_GROUP)
        self.layers.pop(ViewLayerType.PART_OF_SPEECH)
        self.layers.pop(ViewLayerType.META_MORPHEME)
        self.layers.pop(ViewLayerType.META_MORPHEME_MOVED)

    def metaMorphemeRemove(self, index: int) -> MetamorphicParse:
        if ViewLayerType.META_MORPHEME in self.layers:
            metaMorphemeLayer = self.layers[ViewLayerType.META_MORPHEME]
            if 0 <= index < metaMorphemeLayer.getLayerSize(ViewLayerType.META_MORPHEME):
                removedParse = metaMorphemeLayer.metaMorphemeRemoveFromIndex(index)
                self.updateMetaMorphemesMoved()
        return removedParse

    def divideIntoWords(self):
        result = []
        for i in range(self.getNumberOfWords()):
            layerInfo = LayerInfo()
            layerInfo.setLayerData(ViewLayerType.TURKISH_WORD, self.getTurkishWordAt(i))
            layerInfo.setLayerData(ViewLayerType.ENGLISH_WORD, self.getLayerData(ViewLayerType.ENGLISH_WORD))
            if self.layerExists(ViewLayerType.INFLECTIONAL_GROUP):
                layerInfo.setMorphologicalAnalysis(self.getMorphologicalParseAt(i))
            if self.layerExists(ViewLayerType.META_MORPHEME):
                layerInfo.setMetaMorphemes(self.getMetamorphicParseAt(i))
            if self.layerExists(ViewLayerType.ENGLISH_PROPBANK):
                layerInfo.setLayerData(ViewLayerType.ENGLISH_PROPBANK, self.getLayerData(ViewLayerType.ENGLISH_PROPBANK))
            if self.layerExists(ViewLayerType.ENGLISH_SEMANTICS):
                layerInfo.setLayerData(ViewLayerType.ENGLISH_SEMANTICS, self.getLayerData(ViewLayerType.ENGLISH_SEMANTICS))
            if self.layerExists(ViewLayerType.NER):
                layerInfo.setLayerData(ViewLayerType.NER, self.getLayerData(ViewLayerType.NER))
            if self.layerExists(ViewLayerType.SEMANTICS):
                layerInfo.setLayerData(ViewLayerType.SEMANTICS, self.getSemanticAt(i))
            if self.layerExists(ViewLayerType.PROPBANK):
                layerInfo.setLayerData(ViewLayerType.PROPBANK, self.getArgument().__str__())
            if self.layerExists(ViewLayerType.SHALLOW_PARSE):
                layerInfo.setLayerData(ViewLayerType.SHALLOW_PARSE, self.getShallowParseAt(i))
            result.append(layerInfo)
        return result

    def toAnnotatedWord(self, wordIndex: int) -> AnnotatedWord:
        annotatedWord = AnnotatedWord(self.getTurkishWordAt(wordIndex))
        if self.layerExists(ViewLayerType.INFLECTIONAL_GROUP):
            annotatedWord.setParse(self.getMorphologicalParseAt(wordIndex).__str__())
        if self.layerExists(ViewLayerType.META_MORPHEME):
            annotatedWord.setMetamorphicParse(self.getMetamorphicParseAt(wordIndex).__str__())
        if self.layerExists(ViewLayerType.SEMANTICS):
            annotatedWord.setSemantic(self.getSemanticAt(wordIndex))
        if self.layerExists(ViewLayerType.NER):
            annotatedWord.setNamedEntityType(self.getLayerData(ViewLayerType.NER))
        if self.layerExists(ViewLayerType.PROPBANK):
            annotatedWord.setArgument(self.getArgument().__str__())
        if self.layerExists(ViewLayerType.SHALLOW_PARSE):
            annotatedWord.setShallowParse(self.getShallowParseAt(wordIndex))
        return annotatedWord
