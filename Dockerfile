FROM python:3.12.4-alpine3.20

# Now install poetry to install our dependencies
RUN pip install "poetry==1.8.3"

WORKDIR /app
COPY ./apis /app/apis
COPY ./greetings /app/greetings
COPY ./pyproject.toml /app/pyproject.toml
COPY ./main /app/main
COPY ./appconf /app/appconf
COPY ./poetry.lock /app/poetry.lock

RUN poetry install

EXPOSE 8080
CMD ["poetry", "run", "main"]
