from configparser import ConfigParser
import logging


def get_logfile_path() -> str:
    config_object = ConfigParser()
    config_object.read("config.ini")
    return config_object["SERVER"]["logfile"]


def initiate_logging() -> None:
    logging.root.setLevel(logging.NOTSET)
    logging.basicConfig(filename=get_logfile_path())


def log(message: str, level: int) -> None:
    logging.log(level=level, msg=message)
