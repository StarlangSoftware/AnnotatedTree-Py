from setuptools import setup

setup(
    name='NlpToolkit-AnnotatedTree',
    version='1.0.0',
    packages=['AnnotatedTree', 'AnnotatedTree.Layer', 'AnnotatedTree.Processor'],
    url='https://github.com/olcaytaner/AnnotatedTree-Py',
    license='',
    author='olcaytaner',
    author_email='olcaytaner@isikun.edu.tr',
    description='Annotated constituency treebank library',
    install_requires = ['NlpToolkit-AnnotatedSentence', 'NlpToolkit-ParseTree']
)
