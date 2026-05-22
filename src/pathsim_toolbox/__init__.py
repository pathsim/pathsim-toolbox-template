"""
PathSim-Toolbox: A toolbox for PathSim

Specialized simulation blocks for the PathSim framework. All blocks follow
the standard PathSim block interface and can be connected into simulation
diagrams.
"""

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

from .example_block import FirstOrderLag

__all__ = ["__version__", "FirstOrderLag"]
