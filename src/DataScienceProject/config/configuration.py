from pathlib import Path
from src.DataScienceProject.constants import *
from src.DataScienceProject.utils.common import read_yaml, create_directories
from src.DataScienceProject.entity.config_entity import (DataIngestionConfig)
from src.DataScienceProject.entity.config_entity import (DataValidationConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_file_path=CONFIG_FILE_PATH,
        params_file_path=PARAMS_FILE_PATH,
        schema_file_path=SCHEMA_FILE_PATH,
    ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        # create artifact root
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion     # Accessing data_ingestion section from config.yaml
        
        create_directories([Path(config.root_dir)])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation     # Accessing data_validation section from config.yaml
        schema = self.schema.COLUMNS

        create_directories([Path(config.root_dir)])

        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            STATUS_FILE=Path(config.STATUS_FILE),
            unzip_data_dir=Path(config.unzip_data_dir),
            all_schema=schema,
        )

        return data_validation_config
