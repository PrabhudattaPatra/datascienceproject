import os
from src.DataScienceProject import logger
import pandas as pd
from src.DataScienceProject.entity.config_entity import (DataValidationConfig)

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_data(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = data.columns.tolist()
            schema_columns = self.config.all_schema.keys()

            validation_status = True

            for col in all_columns:
                if col not in schema_columns:
                    validation_status = False
                    logger.error(f"Column '{col}' is NOT present in schema")
                else:
                    logger.info(f"Column '{col}' is present in schema")

            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Column Validation Status: {validation_status}\n")

            return validation_status

        except Exception as e:
            logger.error(f"Error during column validation: {e}")
            raise e
 
    def validate_all_datatypes(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            datatype_status = True

            for col, expected_dtype in self.config.all_schema.items():
                if col not in data.columns:
                    datatype_status = False
                    logger.error(f"Column '{col}' missing for datatype validation")
                    continue

                actual_dtype = str(data[col].dtype)

                if actual_dtype != expected_dtype:
                    datatype_status = False
                    logger.error(
                        f"Datatype mismatch for '{col}': expected {expected_dtype}, got {actual_dtype}"
                    )
                else:
                    logger.info(f"Datatype matched for '{col}': {expected_dtype}")

            with open(self.config.STATUS_FILE, "a") as f:
                f.write(f"Datatype Validation Status: {datatype_status}\n")

            return datatype_status

        except Exception as e:
            logger.error(f"Error during datatype validation: {e}")
            raise e
