import logging
import sys
from fastapi import FastAPI
import os
from apis.routers import ping

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

API_ID = "hello-fastapi"
API_VERSION = "0.0.1"
PORT = os.environ.get("PORT", 8080)

# fastAPI Instance
app = FastAPI(
    title="Python FastAPI Template (API ID: "
    + str(API_ID) + ")", docs_url="/", version=API_VERSION
)

app.include_router(ping.router)

def main():
  import uvicorn
  uvicorn.run(app, host='0.0.0.0', port=PORT)


# needed to start the application locally for development/debugging purpose. Will never be called on K8s.
if __name__ == '__main__':
  # if run locally, the port might already be in use, just use another one then.
  main()
