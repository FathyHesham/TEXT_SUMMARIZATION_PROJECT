from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from custom_logger.custom_logging import CustomLogger
from utils.config_loader import ConfigLoader
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class Summarization:

    def __init__(self):
        
        self.config = ConfigLoader.load_config(file_name = "config.yaml")
        if self.config is None:
            raise ValueError("Failed to load configuration for model name.")
        
        self.model_name = self.config.get("model_name")
        self.tokenizer = None
        self.model = None
        self.logger = CustomLogger.get_logger("SummarizerModel")


    def load_model(self):
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
            self.model = self.model.to(device)
            self.logger.info(f"Model {self.model_name} loaded successfully.")
        except Exception as e:
            self.logger.error(f"Failed to load model: {e}")
            self.tokenizer = None
            self.model = None
            raise


    def summarize_text(self, text):
        
        if self.tokenizer is None or self.model is None:
            self.logger.error("Model or tokenizer is not loaded.")
            return None
        
        try:
            # using for loop to convert the text to number "Encoder", get the encoder to summarize and finally decode embedding
            # encode form text to number
            inputs = self.tokenizer(text, return_tensors = "pt", truncation = True, padding = "longest").to(device)

            # generate summary for 
            summary_id = self.model.generate(
                inputs["input_ids"],
                min_length = self.config.get("min_length", 60),
                max_length = self.config.get("max_length", 100),
                num_beams = self.config.get("num_beams", 6),    
                early_stopping = True
            )

            # decode and store each summary
            outputs = self.tokenizer.decode(summary_id[0], skip_special_tokens = True)
            self.logger.info("Summary generated successfully.") 
            # return summaries list
            return outputs
        
        except Exception as e:
            self.logger.error(f"Summarization failed: {e}")
            return None
            


