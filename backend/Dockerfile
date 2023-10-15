FROM python:3.11-slim-bookworm

RUN useradd -ms /bin/bash api
USER api

WORKDIR /api
RUN pip install poetry==1.6.1
ENV PATH=/home/api/.local/bin:${PATH}
COPY pyproject.toml poetry.lock ./
RUN poetry install
COPY . ./
ENV PYTHONPATH "${PYTHONPATH}:/api/src"

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
