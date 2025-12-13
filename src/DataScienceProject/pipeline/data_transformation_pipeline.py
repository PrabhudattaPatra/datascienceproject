from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.data_transformation import Datatransformation
from src.DataScienceProject import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"


class DatatransformationTranningPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            # 1️⃣ Read validation status file
            status_file = Path("artifacts/data_validation/status.txt")

            with open(status_file, "r") as f:
                lines = f.readlines()

            column_status = None
            datatype_status = None

            # 2️⃣ Parse validation statuses
            for line in lines:
                if "Column Validation Status" in line:
                    column_status = line.split(":")[-1].strip() == "True"
                elif "Datatype Validation Status" in line:
                    datatype_status = line.split(":")[-1].strip() == "True"

            # 3️⃣ Validate presence of both statuses
            if column_status is None or datatype_status is None:
                raise Exception(
                    "Validation status file is malformed or missing required entries."
                )

            # 4️⃣ Raise specific errors if validation fails
            if not column_status and not datatype_status:
                raise Exception(
                    "Data Validation Failed: "
                    "Column Validation Status = False, "
                    "Datatype Validation Status = False"
                )

            if not column_status:
                raise Exception("Data Validation Failed: Column Validation Status = False")

            if not datatype_status:
                raise Exception("Data Validation Failed: Datatype Validation Status = False")

            # 5️⃣ If both True → proceed
            logger.info(
                "Data Validation Passed: Column Validation = True, Datatype Validation = True"
            )

            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()

            data_transformation = Datatransformation(
                config=data_transformation_config
            )
            data_transformation.train_test_splitting()

        except Exception:
            logger.exception("Error during Data Transformation stage")
            raise

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DatatransformationTranningPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception:
        logger.exception(f"Error in stage {STAGE_NAME}")
        raise
