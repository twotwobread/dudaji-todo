FROM python:3.11

# 1. poetry install
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root --no-directory --no-dev
COPY . .

# 2. flask run
EXPOSE 5000
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
