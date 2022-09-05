import os, sys
from credit.exception import CreditException
from credit.logger import logging
import yaml


def read_yaml_file(file_path:str)->dict:
    """Converts yaml to dictionary to access in code.

    Args:
        file_path (str): file path where yaml file is present

    Returns:
        dict: data dictionary where yaml is present
    """
    try:
        with open(file_path, "rb") as config:
            logging.info(f"yaml has been created")
            return yaml.safe_load(config)
    except Exception as e:
        raise CreditException(e, sys) from e
        