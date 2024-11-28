import logging
import os
from datetime import datetime

# Generate log filename based on current timestamp
LOG_FILE = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'

# Set up logs folder path
logs_folder = os.path.join(os.getcwd(), 'logs')

# Create the 'logs' folder if it doesn't exist
os.makedirs(logs_folder, exist_ok=True)

# Set the full log file path
LOG_FILE_PATH = os.path.join(logs_folder, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
