import logging
import sys
from greetings.ocp import *

logger = logging.getLogger(__name__)

def main():
  logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
  logger.info('Started')

  logger.info(f"Greeting: {greet('en', 'Alice')}")

  logger.info('Finished')

if __name__ == '__main__':
  main()
