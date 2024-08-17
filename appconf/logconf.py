
import logging
import datetime
import os
import sys
from .info import API_ID

LOG_FORMAT = '%(asctime)s - %(levelname)s [trace_id=%(otelTraceID)s span_id=%(otelSpanID)s] %(name)s %(module)s - %(message)s'
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
logger = logging.getLogger(f"{API_ID}")

def initliazlize_logger():
    logging.Formatter.formatTime = (lambda self, record, datefmt=None: datetime.datetime.fromtimestamp(record.created, datetime.timezone.utc).astimezone().isoformat(sep="T",timespec="milliseconds"))
    logging.basicConfig(stream=sys.stdout, level=LOG_LEVEL, format='%(asctime)s - %(levelname)s [trace_id=%(otelTraceID)s span_id=%(otelSpanID)s] %(name)s %(module)s - %(message)s')
