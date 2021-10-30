from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='NlpToolkit-AnnotatedTree',
    version='1.0.17',
    packages=['AnnotatedTree', 'AnnotatedTree.Layer', 'AnnotatedTree.Processor', 'AnnotatedTree.Processor.Condition',
              'AnnotatedTree.Processor.LayerExist', 'AnnotatedTree.Processor.LeafConverter',
              'AnnotatedTree.Processor.NodeModification'],
    url='https://github.com/StarlangSoftware/AnnotatedTree-Py',
    license='',
    author='olcaytaner',
    author_email='olcaytaner@isikun.edu.tr',
    description='Annotated constituency treebank library',
    install_requires = ['NlpToolkit-AnnotatedSentence', 'NlpToolkit-ParseTree'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
