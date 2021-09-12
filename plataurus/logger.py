import logging
import sys

FORMAT_DEFAULT = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"


def get_file_handler(filename: str, level=logging.INFO, fmt=FORMAT_DEFAULT) -> logging.FileHandler:
    """
    Get a FileHandler to set it further as handler in the getLogger function of the logging module.
    Parameters
    ----------
    filename : string
        The name of a file where logs will be write to.
    level : levels of the logging module (logging.INFO, logging.DEBUG, etc.)
        A level of handling.
    fmt : string
        A format of messages which will be received from a logger.
    Return
    ------
    file_handler : logging.FileHandler
        A FileHandler object of the logging module.
    """
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(level)
    file_handler.setFormatter(logging.Formatter(fmt))

    return file_handler


def get_stream_handler(stream=sys.stdout, level=logging.INFO, fmt=FORMAT_DEFAULT) -> logging.StreamHandler:
    """
    Get a StreamHandler to set it further as handler in the getLogger function of the logging module.
    Parameters
    ----------
    stream : TextIO, default=sys.stdout
        A stream where logs will be written to.
    level : levels of the logging module (logging.INFO, logging.DEBUG, etc.), default=logging.DEBUG
        A level of handling.
    fmt : string, default=logger.FORMAT_DEFAULT
        A format of messages which will be received from a logger.
    Return
    ------
    stream_handler : logging.StreamHandler
        A StreamHandler object of the logging module.
    """
    stream_handler = logging.StreamHandler(stream)
    stream_handler.setLevel(level)
    stream_handler.setFormatter(logging.Formatter(fmt))

    return stream_handler


def get_logger(name, level=logging.DEBUG, handlers: list = None) -> logging.Logger:
    """
    Get logger and setup his level and handlers.
    Parameters
    ----------
    name : string
        The name of a logger.
    level : levels of the logging module (logging.INFO, logging.DEBUG, etc.), default=logging.DEBUG
        A level of handling.
    handlers : list of logging.Handler, default=None
        This is a list that will be set as handlers to the logger.
    Return
    ------
    logger : logging.Logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not handlers:
        handlers = [get_stream_handler()]

    for handler in handlers:
        logger.addHandler(handler)

    return logger
