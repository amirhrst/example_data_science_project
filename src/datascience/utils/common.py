import os 
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError, BoxKeyError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a Box object

    Args:
        path_to_yaml (Path): Path to the yaml file

    Returns:
        Box: Box object containing the yaml data
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error reading YAML file: {path_to_yaml} - {e}")
        raise e
    
@ensure_annotations
def save_json(path: Path, data: Any) -> None:
    """Saves data to a json file

    Args:
        path (Path): Path to the json file
        data (Any): Data to be saved
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f"Data successfully saved to JSON file: {path}")
    except Exception as e:
        logger.error(f"Error saving data to JSON file: {path} - {e}")
        raise e
    
@ensure_annotations
def load_json(path: Path) -> Any:
    """Loads data from a json file

    Args:
        path (Path): Path to the json file

    Returns:
        Any: Data loaded from the json file
    """
    try:
        with open(path, 'r') as json_file:
            data = json.load(json_file)
            logger.info(f"Data successfully loaded from JSON file: {path}")
            return data
    except Exception as e:
        logger.error(f"Error loading data from JSON file: {path} - {e}")
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
def save_bin(data:Any, path:Path) -> None:
    """Saves data to a binary file using joblib

    Args:
        data (Any): Data to be saved
        path (Path): Path to the binary file
    """
    try:
        joblib.dump(data, path)
        logger.info(f"Data successfully saved to binary file: {path}")
    except Exception as e:
        logger.error(f"Error saving data to binary file: {path} - {e}")
        raise e
    
