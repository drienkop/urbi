FROM python:3.11-alpine as requirements

ARG POETRY_VERSION=1.3.1

RUN pip install --no-cache-dir "poetry==${POETRY_VERSION}"

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt --without-hashes -o requirements.txt

FROM python:3.11-alpine as webapp

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
WORKDIR /home/appuser/app
USER appuser

COPY --from=requirements /requirements.txt ./

RUN pip install --no-cache-dir --user -r requirements.txt

COPY ./app .

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
