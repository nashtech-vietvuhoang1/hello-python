
import logging
import datetime
import os
import sys
from .info import API_ID

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
logger = logging.getLogger(f"{API_ID}")

def initliazlize_logger():
    logging.Formatter.formatTime = (lambda self, record, datefmt=None: datetime.datetime.fromtimestamp(record.created, datetime.timezone.utc).astimezone().isoformat(sep="T",timespec="milliseconds"))
    logging.basicConfig(stream=sys.stdout, level=LOG_LEVEL, format='%(asctime)s - %(levelname)s %(name)s %(module)s - %(message)s')
