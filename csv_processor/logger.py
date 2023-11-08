import logging

class logger:
    @staticmethod
    def setup_logging():
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(processName)s %(message)s',
            handlers=[
                logging.FileHandler("processing.log"),
                logging.StreamHandler()
            ]
        )
    @staticmethod
    def get_logger():
        return logging.getLogger()
