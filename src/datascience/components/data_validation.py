import os
from src.datascience import logger
import pandas as pd

from src.datascience.entity.config_entity import DataValidationConfig


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            logger.info(f"CSV Columns: {all_cols}")
            logger.info(f"Schema Columns: {list(all_schema)}")
            
            for col in all_cols:
                if col not in all_schema:
                    logger.error(f"Column '{col}' NOT found in schema!")
                    validation_status = False
                    break
                else:
                    logger.info(f"Column '{col}' found in schema")
                    validation_status = True
            
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            logger.info(f"Final validation status: {validation_status}")
            return validation_status
        
        except Exception as e:
            raise e

    

