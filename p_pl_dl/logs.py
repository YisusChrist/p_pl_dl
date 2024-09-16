"""Logging configuration."""

from logging import Logger

from core_helpers.logs import setup_logger

from .consts import DEBUG, LOG_FILE, PACKAGE

logger: Logger = setup_logger(PACKAGE, LOG_FILE, DEBUG)
