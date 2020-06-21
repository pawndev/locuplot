FROM python:3.7-alpine

LABEL maintainer="pawndev <coquelet.c@gmail.com>"

ENV MPLLOCALFREETYPE=1

RUN apk update && apk upgrade

RUN apk add --no-cache gcc \
                       g++ \
                       libffi-dev \
                       openssl-dev \
                       python3-dev \
                       libc-dev \
    && rm -rf /var/cache/apk/*


COPY poetry.lock pyproject.toml ./

RUN pip --no-cache-dir install poetry poetry-setup \
    && poetry install --no-dev

WORKDIR /usr/src/app

COPY . .

ENTRYPOINT poetry run locuplot