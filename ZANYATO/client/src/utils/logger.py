import logging
import sys
from datetime import datetime
import os

class GameLogger:
    def __init__(self, name: str = "GameLogger"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        #форматтер для логов
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        #консольный обработчик

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        log_dir = 'logs'
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, f"game{datetime.now().strftime('%Y%m%d-%H%M%S')}.log")

        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        #добавляем обработчики к логгеру
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def info(self, msg: str):
        self.logger.info(msg)
    def debug(self, msg: str):
        self.logger.debug(msg)
    def warning(self, msg: str):
        self.logger.warning(msg)
    def error(self, msg: str):
        self.logger.error(msg)

