"""Constants for the project."""

from pathlib import Path
from typing import Any

from core_helpers.xdg_paths import get_user_path

try:
    from importlib import metadata
except ImportError:  # for Python < 3.8
    import importlib_metadata as metadata  # type: ignore

__version__: str | Any = metadata.version(__package__ or __name__)
__desc__: str | Any = metadata.metadata(__package__ or __name__)["Summary"]
PACKAGE: str | Any = metadata.metadata(__package__ or __name__)["Name"]

CONFIG_PATH: Path = get_user_path(PACKAGE, "config")
LOG_PATH: Path = get_user_path(PACKAGE, "log")
LOG_FILE: Path = LOG_PATH / f"{PACKAGE}.log"
VERSION: str | Any = __version__
DESC: str | Any = __desc__

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

DEBUG = False
