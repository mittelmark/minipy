"""
The minipy package.

This is the "minipy" package a simple example for 
a very small module which can be used as template for creating your own Python
package. The following examples can be checked with:
`python -m doctest -v minipy.py`.


Example:
    >>> import minipy
    >>> minipy.add(1,2)
    3
    >>> minipy.add(1,2,3)
    6
"""
from .add import add

__version__ = "0.1"
__author__  = "Detlef Groth, University of Potsdam"
__license__ = "MIT"
