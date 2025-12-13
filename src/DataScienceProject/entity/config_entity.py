from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig: 
    root_dir: Path        # Same as config.yaml
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path 
    STATUS_FILE: Path 
    unzip_data_dir: Path 
    all_schema: dict

@dataclass
class DatatrTransformationConfig:
    root_dir: Path 
    data_path: Path