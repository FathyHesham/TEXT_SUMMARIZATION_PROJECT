import logging 

class CustomLogger:

    @staticmethod
    def get_logger(name = "summarizer"):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)


        # consale handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # file handler
        fh = logging.FileHandler("summarizer.log")
        fh.setLevel(logging.DEBUG)


        # formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # add handler
        logger.addHandler(ch)
        logger.addHandler(fh)

        return logger