FROM python:3.12.4-alpine3.20

# Now install poetry to install our dependencies
RUN pip install "poetry==1.8.3"
RUN pip install "gunicorn==22.0.0"

WORKDIR /code
COPY ./apis /code/apis
COPY ./greetings /code/greetings
COPY ./pyproject.toml /code/pyproject.toml
COPY ./main /code/main
COPY ./poetry.lock /code/poetry.lock

RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080"]
