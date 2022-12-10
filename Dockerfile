FROM python:3.10-slim

WORKDIR /homework_27_2
RUN pip install poetry
COPY pyproject.toml poetry.lock /homework_27_2/
RUN poetry config virtualenvs.create false && poetry install
COPY . /homework_27_2
CMD python manage.py runserver 0.0.0.0:80