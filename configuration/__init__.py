import logging
import sys
import os
import importlib.metadata

API_ID = "hello-python"
API_VERSION = importlib.metadata.version(API_ID)
PORT = os.environ.get("PORT", 8080)
IS_LOCAL = os.environ.get("IS_LOCAL", False)
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level= logging.getLevelName(LOG_LEVEL))

