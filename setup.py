from setuptools import setup

setup(
    name='NlpToolkit-AnnotatedTree',
    version='1.0.8',
    packages=['AnnotatedTree', 'AnnotatedTree.Layer', 'AnnotatedTree.Processor', 'AnnotatedTree.Processor.Condition',
              'AnnotatedTree.Processor.LayerExist', 'AnnotatedTree.Processor.LeafConverter',
              'AnnotatedTree.Processor.NodeModification', 'AnnotatedTree.AutoProcessor',
              'AnnotatedTree.AutoProcessor.AutoNER', 'AnnotatedTree.AutoProcessor.AutoArgument',
              'AnnotatedTree.AutoProcessor.AutoSemantic', 'AnnotatedTree.AutoProcessor.AutoMetaMorphemeMovement'],
    url='https://github.com/olcaytaner/AnnotatedTree-Py',
    license='',
    author='olcaytaner',
    author_email='olcaytaner@isikun.edu.tr',
    description='Annotated constituency treebank library',
    install_requires = ['NlpToolkit-AnnotatedSentence', 'NlpToolkit-ParseTree']
)
