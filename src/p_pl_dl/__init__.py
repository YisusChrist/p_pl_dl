"""Init file for the package."""
try:
    from importlib import metadata
except ImportError:  # for Python < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__package__ or __name__)
__desc__ = metadata.metadata(__package__ or __name__)["Summary"]
PACKAGE = metadata.metadata(__package__ or __name__)["Name"]

__all__ = ["__version__", "__desc__", "PACKAGE"]
