
import os
from .info import *
from .logconf import *

PORT = os.environ.get("PORT", 8080)
IS_LOCAL = os.environ.get("IS_LOCAL", False)




