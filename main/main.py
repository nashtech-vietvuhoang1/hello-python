from fastapi import FastAPI
from apis.routers import ping
from configuration import API_ID, PORT, IS_LOCAL, API_VERSION, LOG_LEVEL

# fastAPI Instance
app = FastAPI(
    title="Python FastAPI Template (API ID: "
    + str(API_ID) + ")", docs_url="/", version=API_VERSION
)

app.include_router(ping.router)

def main():
  import uvicorn
  uvicorn.run(app, host='0.0.0.0', port=PORT, reload=IS_LOCAL, log_level=LOG_LEVEL.lower())


# needed to start the application locally for development/debugging purpose. Will never be called on K8s.
if __name__ == '__main__':
  # if run locally, the port might already be in use, just use another one then.
  main()
