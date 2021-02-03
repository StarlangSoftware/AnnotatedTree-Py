For Developers
============

You can also see [Java](https://github.com/starlangsoftware/AnnotatedTree), [C++](https://github.com/starlangsoftware/AnnotatedTree-CPP), or [C#](https://github.com/starlangsoftware/AnnotatedTree-CS) repository.

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

	git clone https://github.com/starlangsoftware/AnnotatedTree-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `AnnotatedTree-Py` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 

Detailed Description
============

+ [TreeBankDrawable](#treebankdrawable)
+ [ParseTreeDrawable](#parsetreedrawable)
+ [LayerInfo](#layerinfo)
+ [Automatic Annotation](#automatic-annotation)

## TreeBankDrawable

To load an annotated TreeBank:

	TreeBankDrawable(folder: str, String pattern: str)
	a = TreeBankDrawable("/Turkish-Phrase", ".train")

	TreeBankDrawable(folder: str)
	a = new TreeBankDrawable("/Turkish-Phrase")

To access all the trees in a TreeBankDrawable:

	for i in range(a.sentenceCount()):
		parseTree = a.get(i);
		....
	}

## ParseTreeDrawable

To load a saved ParseTreeDrawable:

	ParseTreeDrawable(file: str)
	
is used. Usually it is more useful to load TreeBankDrawable as explained above than to load ParseTree one by one.

To find the node number of a ParseTreeDrawable:

	nodeCount() -> int
	
the leaf number of a ParseTreeDrawable:

	leafCount() -> int
	
the word count in a ParseTreeDrawable:

	wordCount(excludeStopWords: bool) -> int
	
above methods can be used.

## LayerInfo

Information of an annotated word is kept in LayerInfo class. To access the morphological analysis
of the annotated word:

	getMorphologicalParseAt(index: int) -> MorphologicalParse

meaning of an annotated word:

	getSemanticAt(self, index: int) -> str

the shallow parse tag (e.g., subject, indirect object etc.) of annotated word: 

	getShallowParseAt(self, index: int) -> str

the argument tag of the annotated word:

	getArgumentAt(self, index: int) -> Argument
	
the word count in a node:

	getNumberOfWords(self) -> int

## Automatic Annotation

To assign the arguments of a sentence automatically:

	TurkishAutoArgument(self, secondLanguage: ViewLayerType)

above class is used. 

	autoArgument(self, parseTree: ParseTreeDrawable, frameset: Frameset)

With above line, the arguments of the tree are annotated automatically.

To apply named entity recognition to a sentence:

	TurkishSentenceAutoNER(self, secondLanguage: ViewLayerType)

above class is used. For example,

	a = TurkishTreeAutoNER()
	a.autoNER(parseTree)

with the above code, automatic named entity recognition of a tree can be made.

To make semantic annotation in a sentence:

	TurkishTreeAutoSemantic()

above class can be used. For example,

	a = TurkishTreeAutoSemantic()
	a.autoSemantic(parseTree)

with above code, automatic semantic annotation of the tree can be made.

## Cite
If you use this resource on your research, please cite the following paper: 

```
@article{akcakaya,
  title={An all-words sense annotated {T}urkish corpus},
  author={S. Akçakaya and O. T. Y{\i}ld{\i}z},
  journal={2018 2nd International Conference on Natural Language and Speech Processing (ICNLSP)},
  year={2018},
  pages={1-6}
}

@inproceedings{arican,
  title={{E}nglish-{T}urkish Parallel Semantic Annotation of Penn-Treebank},
  author={ B. N. Ar{\i}can and {\"O}. Bakay and B. Avar and O. T. Y{\i}ld{\i}z and {\"O}. Ergelen},
  booktitle={Wordnet Conference},
  pages={298},
  year={2019}
}
