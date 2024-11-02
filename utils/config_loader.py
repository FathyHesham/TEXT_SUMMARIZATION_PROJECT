# Import the yaml library for working with yaml files
import yaml
from custom_logger.custom_logging import CustomLogger


logger = CustomLogger.get_logger("ConfigLoader")


# create class using to load configure
class ConfigLoader:
    @staticmethod
    # create function to load the file.yaml
    def load_config(file_name = "config.yaml"):
        # attempt to load the yaml.file
        try:
            with open(file_name, "r") as file: # open the file in read mode
                config = yaml.safe_load(file) # load and parse the yaml file
                logger.info("Config file loaded successfully.")
                return config  # return the parsed configuration
        # handle the exception if the file is not found
        except FileNotFoundError:
            logger.error(f"config file not found at {file_name}")
            return None
        # handle exceptions if there is an error in parsing the YAML file
        except yaml.YAMLError as e:
            logger.error(f"error parsing config file : {e}")
            return None