FROM python:3.12.4-alpine3.20

# Now install poetry to install our dependencies
RUN pip install "poetry==1.8.3"

WORKDIR /code
COPY ./apis /code/apis
COPY ./greetings /code/greetings
COPY ./pyproject.toml /code/pyproject.toml
COPY ./pyproject.toml /
COPY ./main /code/main
COPY ./configuration /code/configuration
COPY ./poetry.lock /code/poetry.lock

RUN poetry install

EXPOSE 8080
CMD ["poetry", "run", "main"]
