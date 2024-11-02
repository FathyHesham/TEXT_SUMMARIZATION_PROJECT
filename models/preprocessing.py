# import library 
import re
from custom_logger.custom_logging import CustomLogger

logger = CustomLogger.get_logger("TextPreprocessor")



class PreProcessing:
    @staticmethod
    # create function "preprocessing"
    def preprocessing_func(text):
        try:   
            # convert text to lowercase
            # lower_case = text.lower()
            # remove special characters (ie. "?/,)
            remove_special_char = re.sub(r"[\",?;]", "", text)
            # return processed_text
            logger.info("Text preprocessed successfully.")
            return remove_special_char
        except Exception as e:
            logger.error(f"Error during preprocessing: {e}")
            return ''