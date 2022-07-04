FROM python:3.10-slim-bullseye

RUN mkdir /app/
WORKDIR /app/

# poetry
RUN pip install poetry --upgrade
RUN poetry config virtualenvs.create false
# Add poetry files, allows docker to cache installed dependencies between builds
COPY project/pyproject.toml pyproject.toml
COPY project/poetry.lock poetry.lock
# Install dependencies
RUN poetry install --no-interaction

CMD ["tail", "-f", "/dev/null"]

