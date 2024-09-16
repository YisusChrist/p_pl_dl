"""Constants for the project."""

from pathlib import Path

from platformdirs import user_config_dir, user_log_dir

try:
    from importlib import metadata
except ImportError:  # for Python < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__package__ or __name__)
__desc__ = metadata.metadata(__package__ or __name__)["Summary"]
PACKAGE = metadata.metadata(__package__ or __name__)["Name"]

CONFIG_PATH = user_config_dir(appname=PACKAGE, ensure_exists=True)
LOG_PATH = user_log_dir(appname=PACKAGE, ensure_exists=True)
LOG_FILE = Path(LOG_PATH).resolve() / f"{PACKAGE}.log"
VERSION = __version__
DESC = __desc__

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

DEBUG = False
PROFILE = False
