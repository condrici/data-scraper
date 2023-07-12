from configparser import ConfigParser
import logging
import json


def get_logfile_path() -> str:
    config_object = ConfigParser()
    config_object.read("config.ini")
    return config_object["SERVER"]["logfile"]


def initiate_logging() -> None:
    logging.root.setLevel(logging.NOTSET)
    logging.basicConfig(filename=get_logfile_path())


def log(message: str, level: int) -> None:
    logging.log(level=level, msg=message)


def get_json_from_file(filepath: str) -> json:
    with open(filepath) as user_file:
        file_contents = user_file.read()

    return json.loads(file_contents)
