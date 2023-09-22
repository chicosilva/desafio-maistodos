import logging

from gunicorn import glogging
from loguru import logger


class InterceptHandler(logging.Handler):
    """Handler for intercepting records and outputting to loguru."""

    def emit(self, record: logging.LogRecord):
        """Intercepts log messages.
        Intercepts log records sent to the handler, adds additional context to
        the records, and outputs the record to the default loguru logger.

        :param: record: The log record
        """
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        frame, depth = logging.currentframe(), 2

        while frame.f_code.co_filename == logging.__file__:
            if frame.f_back:
                frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


class Logger(glogging.Logger):
    """Implements and overrides the gunicorn logging interface.

    This class inherits from the standard gunicorn logger and overrides it by
    replacing the handlers with `InterceptHandler` in order to route the
    gunicorn logs to loguru.
    """

    def __init__(self, cfg):
        super().__init__(cfg)
        logging.getLogger("gunicorn.error").handlers = [InterceptHandler()]
        logging.getLogger("gunicorn.access").handlers = [InterceptHandler()]
