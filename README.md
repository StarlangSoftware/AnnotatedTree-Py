# AnnotatedTree-Py

For Developers
============
You can also see either [Java](https://github.com/olcaytaner/AnnotatedTree) 
or [C++](https://github.com/olcaytaner/AnnotatedTree-CPP) repository.
## Requirements

* [Python 3.7 or higher](#python)
* [Maven](#maven)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called DataStructure will be created. Or you can use below link for exploring the code:

	git clone https://github.com/olcaytaner/AnnotatedTree-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `AnnotatedTree-Py` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 

## Compile

**From IDE**

After being done with the downloading and Maven indexing, select **Build Project** option from **Build** menu. After compilation process, user can run AnnotatedTree-Py.

Detailed Description
============
+ [TreeBankDrawable](#treebankdrawable)
+ [ParseTreeDrawable](#parsetreedrawable)
+ [LayerInfo](#layerinfo)
+ [Automatic Annotation](#automatic-annotation)

## TreeBankDrawable

İşaretlenmiş TreeBank'ı yüklemek için

	TreeBankDrawable(folder: str, String pattern: str)
	a = TreeBankDrawable("/Turkish-Phrase", ".train")

	TreeBankDrawable(folder: str)
	a = new TreeBankDrawable("/Turkish-Phrase")

Bir TreeBankDrawable'daki tüm ağaçlara erişmek için

	for i in range(a.sentenceCount()):
		parseTree = a.get(i);
		....
	}

## ParseTreeDrawable

Kaydedilmiş bir ParseTreeDrawable'yi yüklemek için

	ParseTreeDrawable(file: str)
	
kullanılır. Genel olarak tek tek ParseTree yüklemek yerine yukarıda anlatıldığı gibi bir TreeBankDrawable yüklemek daha mantıklıdır.

Bir ParseTreeDrawable'nin düğüm sayısını

	nodeCount() -> int
	
yaprak sayısını 

	leafCount() -> int
	
içinde yer alan kelime sayısını da

	wordCount(excludeStopWords: bool) -> int
	
metodları ile bulabiliriz.

## LayerInfo

İşaretlenmiş bir kelimenin bilgileri LayerInfo sınıfında tutulur. İşaretlenmiş kelimenin morfolojik
analizi

	getMorphologicalParseAt(index: int) -> MorphologicalParse

İşaretlenmiş kelimenin anlamı

	getSemanticAt(self, index: int) -> str

İşaretlenmiş kelimenin özne, dolaylı tümleç, vs. shallow parse tagı

	getShallowParseAt(self, index: int) -> str

İşaretlenmiş kelimenin argüman tagı

	getArgumentAt(self, index: int) -> Argument
	
Bir düğümdeki kelime sayısı

	getNumberOfWords(self) -> int

## Automatic Annotation

Bir cümlenin argümanlarını otomatik olarak belirlemek için

	TurkishAutoArgument(self, secondLanguage: ViewLayerType)

sınıfı kullanılır. 

	autoArgument(self, parseTree: ParseTreeDrawable, frameset: Frameset)

ile ağacın argümanları otomatik olarak işaretlenir.

Bir cümlede adlandırılmış varlık tanıma yapmak için

	TurkishSentenceAutoNER(self, secondLanguage: ViewLayerType)

sınıfı kullanılır. Örneğin,

	a = TurkishTreeAutoNER()
	a.autoNER(parseTree)

ile ağacın varlık tanıma otomatik olarak yapılır.

Bir cümlede anlamsal işaretleme için

	TurkishTreeAutoSemantic()

sınıfı kullanılır. Örneğin,

	a = TurkishTreeAutoSemantic()
	a.autoSemantic(parseTree)

ile ağacın anlamsal işaretleme otomatik olarak yapılır.
