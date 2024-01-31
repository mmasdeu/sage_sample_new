r"""
Darmon Points package
=====================

This file is the main file of the package.

EXAMPLES::

sage: from darmonpoints.darmonpoint import darmon_point
sage: darmon_point()
42
"""
from darmonpoints.a_cython_file import cython_test


def darmon_point():
    r"""
    This is a placeholder for some documentation.

    EXAMPLES::

    sage: from darmonpoints.darmonpoint import darmon_point
    sage: darmon_point()
    42
    """
    assert cython_test() == 123
    return 42
