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

	TreeBankDrawable(File folder, String pattern)
	a = new TreeBankDrawable(new File("/Turkish-Phrase"), ".train")

	TreeBankDrawable(File folder)
	a = new TreeBankDrawable(new File("/Turkish-Phrase"))

	TreeBankDrawable(File folder, String pattern, int from, int to)
	a = new TreeBankDrawable(new File("/Turkish-Phrase"), ".train", 1, 500)

Bir TreeBankDrawable'daki tüm ağaçlara erişmek için

	for (int i = 0; i < a.sentenceCount(); i++){
		ParseTreeDrawable parseTree = (ParseTreeDrawable) a.get(i);
		....
	}

## ParseTreeDrawable

Kaydedilmiş bir ParseTreeDrawable'yi yüklemek için

	ParseTreeDrawable(FileInputStream file)
	
kullanılır. Genel olarak tek tek ParseTree yüklemek yerine yukarıda anlatıldığı gibi bir TreeBankDrawable yüklemek daha mantıklıdır.

Bir ParseTreeDrawable'nin düğüm sayısını

	int nodeCount()
	
yaprak sayısını 

	int leafCount()
	
içinde yer alan kelime sayısını da

	int wordCount(boolean excludeStopWords)
	
metodları ile bulabiliriz.

## LayerInfo

İşaretlenmiş bir kelimenin bilgileri LayerInfo sınıfında tutulur. İşaretlenmiş kelimenin morfolojik
analizi

	MorphologicalParse getMorphologicalParseAt(int index)

İşaretlenmiş kelimenin anlamı

	String getSemanticAt(int index)

İşaretlenmiş kelimenin özne, dolaylı tümleç, vs. shallow parse tagı

	String getShallowParseAt(int index)

İşaretlenmiş kelimenin argüman tagı

	Argument getArgumentAt(int index)
	
Bir düğümdeki kelime sayısı

	int getNumberOfWords()

## Automatic Annotation

Bir cümlenin argümanlarını otomatik olarak belirlemek için

	TurkishAutoArgument()

sınıfı kullanılır. 

	void autoArgument(ParseTreeDrawable parseTree, Frameset frameset);

ile ağacın argümanları otomatik olarak işaretlenir.

Bir cümlede otomatik olarak morfolojik belirsizlik gidermek için

	TurkishTreeAutoDisambiguator(RootWordStatistics rootWordStatistics)
								  
sınıfı kullanılır. Örneğin,

	a = TurkishTreeAutoDisambiguator(new RootWordStatistics());
	a.autoDisambiguate(parseTree);

ile ağacın morfolojik belirsizlik gidermesi otomatik olarak yapılır.

Bir cümlede adlandırılmış varlık tanıma yapmak için

	TurkishSentenceAutoNER()

sınıfı kullanılır. Örneğin,

	a = TurkishTreeAutoNER();
	a.autoNER(parseTree);

ile ağacın varlık tanıma otomatik olarak yapılır.

Bir cümlede anlamsal işaretleme için

	TurkishTreeAutoSemantic()

sınıfı kullanılır. Örneğin,

	a = TurkishTreeAutoSemantic();
	a.autoSemantic(parseTree);

ile ağacın anlamsal işaretleme otomatik olarak yapılır.
