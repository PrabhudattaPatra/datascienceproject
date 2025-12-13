import os
import logging
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath= os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath), # log to a file(running_logs.log)
        logging.StreamHandler(sys.stdout)  # log to console (standard output)
    ])

logger = logging.getLogger("datasciencelogger")

