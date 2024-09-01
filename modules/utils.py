# utils.py

import os
import configparser
import random
import logging
import numpy as np


#####################
# INSTANTIATE LOGGER
#####################

# Create a logger object
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create a file handler
file_handler = logging.FileHandler("logs/voice_recorder_transcribe.log", mode="a")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# Ensure logs directory exists
def read_config():
    """
    Read and return configuration settings from "config.ini".
    """
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config


def create_directories():
    directories = ["logs", "mp3s", "output"]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
