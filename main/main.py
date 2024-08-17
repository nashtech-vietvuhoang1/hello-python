from fastapi import FastAPI
from apis.routers import ping
from appconf import API_ID, PORT, IS_LOCAL, API_VERSION, initliazlize_logger, LOG_FORMAT, setting_otlp

initliazlize_logger()

# fastAPI Instance
app = FastAPI(
    title="Python FastAPI Template (API ID: "
    + str(API_ID) + ")", docs_url="/", version=API_VERSION
)

app.include_router(ping.router)
setting_otlp(app)

def main():
  import uvicorn
  log_config = uvicorn.config.LOGGING_CONFIG
  log_config["formatters"]["access"]["fmt"] = LOG_FORMAT
  uvicorn.run(app, host='0.0.0.0', port=PORT, reload=IS_LOCAL, log_config=log_config)

# needed to start the application locally for development/debugging purpose. Will never be called on K8s.
if __name__ == '__main__':
  # if run locally, the port might already be in use, just use another one then.
  main()
