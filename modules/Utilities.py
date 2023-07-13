"""
Utilities
Generic module to temporarily store functionality that might be needed in multiple places
"""

from configparser import ConfigParser
import logging
import json

"""Get logfile path from the config.ini file"""


def get_logfile_path() -> str:
    config_object = ConfigParser()
    config_object.read("config.ini")
    return config_object["SERVER"]["logfile"]


"""Initiate logging and allow logs to be added on the fly"""


def initiate_logging() -> None:
    logging.root.setLevel(logging.NOTSET)
    logging.basicConfig(filename=get_logfile_path())


"""Log something on the fly"""


def log(message: str, level: int) -> None:
    logging.log(level=level, msg=message)


"""Retrieve jSON string from an external file"""


def get_json_from_file(filepath: str) -> json:
    with open(filepath) as user_file:
        file_contents = user_file.read()

    return json.loads(file_contents)
