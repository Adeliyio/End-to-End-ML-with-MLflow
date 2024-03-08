import os
import sys
import logging

# Define logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define directory and file path for logs
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Log to file
        logging.StreamHandler(sys.stdout)   # Log to stdout
    ]
)

# Get logger instance
logger = logging.getLogger("mlProjectLogger")
