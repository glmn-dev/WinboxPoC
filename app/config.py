from sys import stdout

from loguru import logger


def logger_setup(path: str):
    logger.remove()
    logger.add(path, level="DEBUG", rotation="100 MB")
    logger.add(
        stdout,
        colorize=True,
        format="<green>{time}</green> <level>{message}</level>",
        level="DEBUG",
    )
