from setuptools import setup

setup(
    name='NlpToolkit-AnnotatedTree',
    version='1.0.14',
    packages=['AnnotatedTree', 'AnnotatedTree.Layer', 'AnnotatedTree.Processor', 'AnnotatedTree.Processor.Condition',
              'AnnotatedTree.Processor.LayerExist', 'AnnotatedTree.Processor.LeafConverter',
              'AnnotatedTree.Processor.NodeModification'],
    url='https://github.com/StarlangSoftware/AnnotatedTree-Py',
    license='',
    author='olcaytaner',
    author_email='olcaytaner@isikun.edu.tr',
    description='Annotated constituency treebank library',
    install_requires = ['NlpToolkit-AnnotatedSentence', 'NlpToolkit-ParseTree']
)
