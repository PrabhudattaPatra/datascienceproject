import os
import yaml
from src.DataScienceProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from box.exceptions import BoxValueError
from typing import Union
from pathlib import Path

@ensure_annotations
def read_yaml(path_to_yaml: Union[str, Path]) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (str): The file path to the YAML file.
    Raises:
        BoxValueError: If the YAML file is empty or has invalid format.
        Exception: For any other exceptions that occur during file reading.
    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """
    try: 
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
        logger.info(f"YAML file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError("YAML file is empty or has invalid format")
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: str, data: Any) -> None:
    """Saves data to a JSON file.

    Args:
        path (str): The file path where the JSON file will be saved.
        data (Any): The data to be saved in JSON format.
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        logger.info(f"Data successfully saved to JSON file at: {path}")
    except Exception as e:
        logger.error(f"Error saving data to JSON file: {e}")
        raise e
    
@ensure_annotations
def load_json(path: str) -> ConfigBox:
    """Loads data from a JSON file.

    Args:
        path (str): The file path to the JSON file.
    Returns:
        Any: The data loaded from the JSON file.    
    """
    try:
        with open(path, 'r') as json_file:
            data = json.load(json_file)
        logger.info(f"Data successfully loaded from JSON file at: {path}")
        return ConfigBox(data)
    except Exception as e:
        logger.error(f"Error loading data from JSON file: {e}")
        raise e
    
@ensure_annotations
def save_bin(path: str, obj: Any) -> None:
    """Saves an object to a binary file using joblib.

    Args:
        path (str): The file path where the binary file will be saved.
        obj (Any): The object to be saved.
    """
    try:
        with open(path, 'wb') as bin_file:
            joblib.dump(obj, bin_file)
        logger.info(f"Object successfully saved to binary file at: {path}")
    except Exception as e:
        logger.error(f"Error saving object to binary file: {e}")
        raise e
    
@ensure_annotations
def load_bin(path: str) -> Any:
    """Loads an object from a binary file using joblib.

    Args:
        path (str): The file path to the binary file.
    Returns:
        Any: The object loaded from the binary file.
    """
    try:
        with open(path, 'rb') as bin_file:
            obj = joblib.load(bin_file)
        logger.info(f"Object successfully loaded from binary file at: {path}")
        return obj
    except Exception as e:
        logger.error(f"Error loading object from binary file: {e}")
        raise e
    

