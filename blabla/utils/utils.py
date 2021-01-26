"""A file containing helper functions"""

from nltk.tree import Tree
from typing import Any


def get_nltk_tree(parse_tree: Any) -> Tree:
    """Given a parse_tree obtained from CoreNLP, this function recursively generates an NLTK
    Tree based on the parse_tree information.
    Args:
        parse_tree (CoreNLP_pb2.ParseTree): The CoreNLP formatted parse tree
    Returns:
        (Tree): The parse tree converted into NLTK format
    """
    return Tree(
        parse_tree.value,
        [get_nltk_tree(child) for child in parse_tree.child]
    ) if parse_tree.child else parse_tree.value