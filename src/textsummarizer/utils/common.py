import os
from box.exceptions import BoxValueError
import yaml
from textsummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml:Path) ->  ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input
        
    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    
    try:
        with open(path_to_yaml) as f:
            yaml_data = yaml.safe_load(f)
            logger.info(f"yaml file: {path_to_yaml} loaded Successfully")
            config_box = ConfigBox(yaml_data)
            return config_box
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """creates directories

    Args:
        path_to_directories (list): list of paths of directories
        verbose (bool, optional): Ignore if multiple dirs is to be created. Default is False
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created Directory at: {path}")


@ensure_annotations
def get_file_size(file_path: Path) -> str:
    """gets size of file in bytes

    Args:
        file_path (Path): path of file

    Returns:
        str: size of file in KB
    """
    
    size_in_kb = round(os.path.getsize(file_path)/1024)
    return f"~{size_in_kb} KB"