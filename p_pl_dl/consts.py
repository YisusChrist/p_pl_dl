"""Constants for the project."""

from pathlib import Path

from core_helpers.xdg_paths import get_user_path, PathType

try:
    from importlib import metadata
except ImportError:  # for Python < 3.8
    import importlib_metadata as metadata  # type: ignore

metadata_info = metadata.metadata(__package__ or __name__)
__version__ = metadata.version(__package__ or __name__)
__desc__ = metadata_info["Summary"]
PACKAGE = metadata_info["Name"]
GITHUB = metadata_info["Home-page"]
AUTHOR = metadata_info["Author"]

LOG_PATH: Path = get_user_path(PACKAGE, PathType.LOG)
LOG_FILE: Path = LOG_PATH / f"{PACKAGE}.log"

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

DEBUG = False
