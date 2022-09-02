import logging
import os
from distutils.log import INFO
from datetime import datetime

### Declaring variables for logging
LOG_DIR='logs'
CURRENT_TIME_STAMP=f"{datetime.now().strftime('%Y-%m-%d_%h-%M-%S')}"
LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"

#Log Folder creation if folder is not present
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE_PATH= os.path.join(LOG_DIR, LOG_FILE_NAME)

## Setting log configuraitons
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='w',
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level= logging.INFO
)