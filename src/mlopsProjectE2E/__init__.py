import os
import sys
import logging

# Define the format of the log messages including time, log level, module name, and message content
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Specify the directory where log files will be stored
log_dir = "logs"
# Create the full filepath for the log file within the specified directory
log_filepath = os.path.join(log_dir, "running_logs.log")
# Ensure the directory exists; create it if it does not
os.makedirs(log_dir, exist_ok=True)

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO (also captures levels above INFO)
    format=logging_str,  # Use the previously defined log message format

    # Set the handlers that determine where logs are output
    handlers=[
        logging.FileHandler(log_filepath),  # Log messages are written to a file
        logging.StreamHandler(sys.stdout)   # Log messages are also output to the console
    ]
)

# Create a logger object to be used throughout the project
logger = logging.getLogger("mlopsProjectE2ELogger")